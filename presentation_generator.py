#!/usr/bin/env python3
"""
Quarto Presentation Generator

This script generates a Quarto RevealJS presentation from an article by:
1. Taking an article as input
2. Asking an LLM to create a general structure (20 slides)
3. Generating content for each slide using the LLM
4. Saving the complete presentation as a .qmd file
"""

import os
import json
from typing import List, Dict, Optional
from datetime import datetime
import argparse

# Import actual LLM clients
from llm_clients import LangChainLLMClient
# Import prompt management
from prompts.prompt_manager import get_structure_prompt, get_slide_content_prompt, prompt_manager


def create_llm_client(model: str = "gpt-4") -> object:
    """
    Create unified LLM client using LangChain framework
    
    Args:
        model: The model name (e.g., "gpt-4", "claude-3-sonnet-20240229", "llama2")
    
    Returns:
        LangChainLLMClient instance
    """
    try:
        return LangChainLLMClient(model=model)
    except (ImportError, ValueError) as e:
        print(f"⚠️ LangChain LLM client unavailable: {e}")
        print("⚠️ Falling back to placeholder client - API responses will be simulated")
        return PlaceholderLLMClient(model=model)


class PlaceholderLLMClient:
    """Fallback placeholder LLM client for testing when no real client is available"""
    
    def __init__(self, model: str = "placeholder"):
        self.model = model
        print(f"🔧 Using placeholder client for model: {model}")
        
    def generate_response(self, prompt: str) -> str:
        """
        Generate placeholder response for testing
        """
        print(f"[Placeholder LLM] Prompt length: {len(prompt)} characters")
        print(f"[Placeholder LLM] Using model: {self.model}")
        
        # Provide more sophisticated placeholder responses
        if "general structure" in prompt.lower():
            return """
            {
                "title": "Understanding the Article Topic",
                "slides": [
                    {"slide_number": 1, "title": "Introduction", "type": "intro", "key_points": ["Welcome", "Overview", "Objectives"]},
                    {"slide_number": 2, "title": "Background", "type": "content", "key_points": ["Context", "Problem statement"]},
                    {"slide_number": 3, "title": "Main Concept 1", "type": "content", "key_points": ["Key idea", "Examples"]},
                    {"slide_number": 4, "title": "Main Concept 2", "type": "content", "key_points": ["Another key idea", "Applications"]},
                    {"slide_number": 5, "title": "Conclusion", "type": "conclusion", "key_points": ["Summary", "Takeaways"]}
                ]
            }
            """
        else:
            # Extract slide number from prompt to generate contextual content
            slide_number = "Unknown"
            slide_title = "Sample Slide"
            
            # Try to extract slide info from prompt
            if "slide" in prompt.lower():
                lines = prompt.split('\n')
                for line in lines:
                    if "slide_number" in line.lower() and ":" in line:
                        try:
                            slide_number = line.split(':')[1].strip().rstrip(',')
                        except:
                            pass
                    elif "title" in line.lower() and ":" in line:
                        try:
                            slide_title = line.split(':')[1].strip().replace('"', '').rstrip(',')
                        except:
                            pass
            
            return f"""## {slide_title}

### Key Points

- This is placeholder content for slide {slide_number}
- Generated using {self.model} model (placeholder mode)
- Please review and customize this content

### Example Content

:::: {{.columns}}

::: {{.column width="50%"}}
- Main concept
- Supporting details
- Examples
:::

::: {{.column width="50%"}}
- Additional insights
- Related topics
- Applications
:::

::::

*Note: This content was generated in placeholder mode. For actual LLM-generated content, configure your API keys and use a supported model.*"""


class QuartoGenerator:
    """Main class for generating Quarto presentations"""
    
    def __init__(self, llm_client):
        self.llm_client = llm_client
        self.quarto_reference = self._load_quarto_reference()
        
    def _load_quarto_reference(self) -> str:
        """Load the Quarto reference template"""
        try:
            return prompt_manager.get_quarto_template()
        except FileNotFoundError:
            # Fallback minimal reference
            return """
            # Quarto RevealJS Reference
            
            ## YAML Front Matter
            ```yaml
            ---
            title: "Presentation Title"
            author: "Author Name"
            format:
              revealjs:
                theme: default
                slide-number: true
                transition: slide
            ---
            ```
            
            ## Slide Structure
            - Use `#` for section dividers
            - Use `##` for individual slides
            - Use `---` for slides without titles
            """
    
    def generate_structure(self, article_content: str, num_slides: int = 20) -> Dict:
        """Generate the general structure of the presentation"""
        
        structure_prompt = get_structure_prompt(article_content, num_slides)
        
        print(f"📋 Generating presentation structure...")
        response = self.llm_client.generate_response(structure_prompt)
        
        try:
            # Additional cleanup for JSON parsing
            cleaned_response = response.strip()
            if cleaned_response.startswith('```') or cleaned_response.endswith('```'):
                # Remove any remaining markdown code blocks
                import re
                cleaned_response = re.sub(r'^```[a-zA-Z]*\n?', '', cleaned_response)
                cleaned_response = re.sub(r'\n?```$', '', cleaned_response)
                cleaned_response = cleaned_response.strip()
            
            structure = json.loads(cleaned_response)
            print(f"✅ Generated structure with {len(structure.get('slides', []))} slides")
            return structure
        except json.JSONDecodeError as e:
            print(f"❌ Failed to parse structure JSON: {e}")
            print(f"Raw response: {response[:200]}...")
            return self._create_fallback_structure(num_slides)
    
    def _create_fallback_structure(self, num_slides: int) -> Dict:
        """Create a fallback structure if LLM response fails"""
        slides = []
        for i in range(1, num_slides + 1):
            slide_type = "intro" if i == 1 else "conclusion" if i == num_slides else "content"
            slides.append({
                "slide_number": i,
                "title": f"Slide {i}",
                "type": slide_type,
                "key_points": ["Point 1", "Point 2", "Point 3"]
            })
        
        return {
            "title": "Generated Presentation",
            "slides": slides
        }
    
    def generate_slide_content(self, article_content: str, structure: Dict, slide_info: Dict) -> str:
        """Generate content for a specific slide"""
        
        slide_prompt = get_slide_content_prompt(
            article_content=article_content,
            structure=json.dumps(structure, indent=2),
            slide_number=slide_info['slide_number'],
            slide_title=slide_info['title'],
            slide_type=slide_info['type'],
            key_points=slide_info['key_points'],
            quarto_reference=self.quarto_reference
        )
        
        print(f"🎨 Generating content for slide {slide_info['slide_number']}: {slide_info['title']}")
        content = self.llm_client.generate_response(slide_prompt)
        return content.strip()
    
    def generate_presentation(self, article_content: str, num_slides: int = 20, 
                            output_file: str = None) -> str:
        """Generate the complete Quarto presentation"""
        
        # Create output directory if it doesn't exist
        output_dir = "out"
        os.makedirs(output_dir, exist_ok=True)
        
        if output_file is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_file = f"{output_dir}/generated_presentation_{timestamp}.qmd"
        else:
            # If user provided a path, ensure it's in the out directory
            if not output_file.startswith(output_dir + "/"):
                output_file = f"{output_dir}/{output_file}"
        
        print(f"🚀 Starting presentation generation...")
        print(f"📄 Article length: {len(article_content)} characters")
        print(f"🎯 Target slides: {num_slides}")
        print(f"💾 Output file: {output_file}")
        
        # Step 1: Generate structure
        structure = self.generate_structure(article_content, num_slides)
        
        # Step 2: Create YAML front matter
        yaml_header = f"""---
title: "{structure['title']}"
author: "Generated by Quarto Presentation Generator"
date: "{datetime.now().strftime('%Y-%m-%d')}"
format:
  revealjs:
    theme: default
    slide-number: true
    transition: slide
    chalkboard: true
    code-line-numbers: true
    incremental: false
    navigation-mode: vertical
    controls: true
    progress: true
execute:
  echo: true
  warning: false
  message: false
---

"""
        
        # Step 3: Generate slides
        presentation_content = [yaml_header]
        
        for slide_info in structure['slides']:
            slide_content = self.generate_slide_content(article_content, structure, slide_info)
            presentation_content.append(slide_content)
            presentation_content.append("")  # Empty line between slides
        
        # Step 4: Save to file
        full_content = "\n".join(presentation_content)
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(full_content)
        
        print(f"✅ Presentation saved to {output_file}")
        print(f"📊 Generated {len(structure['slides'])} slides")
        
        return output_file


def main():
    """Main function to run the presentation generator"""
    parser = argparse.ArgumentParser(description="Generate Quarto presentation from article")
    parser.add_argument("input_file", help="Path to the input article file")
    parser.add_argument("--output", "-o", help="Output .qmd file path")
    parser.add_argument("--slides", "-s", type=int, default=20, help="Number of slides to generate")
    parser.add_argument("--model", "-m", default="gpt-4", 
                        help="LLM model to use (e.g., 'gpt-4', 'gpt-3.5-turbo', 'claude-3-sonnet-20240229', 'llama2')")
    
    args = parser.parse_args()
    
    # Read input article
    try:
        with open(args.input_file, 'r', encoding='utf-8') as f:
            article_content = f.read()
    except FileNotFoundError:
        print(f"❌ Error: Could not find input file: {args.input_file}")
        return
    except Exception as e:
        print(f"❌ Error reading input file: {e}")
        return
    
    # Initialize components
    llm_client = create_llm_client(model=args.model)
    generator = QuartoGenerator(llm_client)
    
    # Generate presentation
    try:
        output_file = generator.generate_presentation(
            article_content=article_content,
            num_slides=args.slides,
            output_file=args.output
        )
        
        print(f"\n🎉 Success! Presentation generated: {output_file}")
        print("\n📝 Next steps:")
        print("1. Review the generated .qmd file in the 'out/' directory")
        print("2. Edit content as needed")
        print("3. Render with: quarto render {output_file}")
        
    except Exception as e:
        print(f"❌ Error generating presentation: {e}")


if __name__ == "__main__":
    # If run without arguments, show usage example
    import sys
    if len(sys.argv) == 1:
        print("📖 Quarto Presentation Generator")
        print("\nUsage:")
        print("  python presentation_generator.py article.txt")
        print("  python presentation_generator.py article.txt --slides 15 --output my_presentation.qmd")
        print("\nOptions:")
        print("  --slides, -s    Number of slides to generate (default: 20)")
        print("  --output, -o    Output .qmd file path (saved in 'out/' directory)")
        print("  --model, -m     LLM model to use")
        print("                  OpenAI: 'gpt-4', 'gpt-3.5-turbo'")
        print("                  Anthropic: 'claude-3-sonnet-20240229', 'claude-3-haiku-20240307'")
        print("                  Local: 'llama2', 'mixtral', etc. (requires Ollama or similar)")
        print("\nOutput:")
        print("  Generated presentations are saved in the 'out/' directory")
        print("\nSetup:")
        print("  1. Install dependencies: pip install -r requirements.txt")
        print("  2. For additional providers: pip install anthropic")
        print("  3. Set API keys as environment variables:")
        print("     export OPENAI_API_KEY='your-openai-key'")
        print("     export ANTHROPIC_API_KEY='your-anthropic-key'")
        print("\nExample:")
        print("  python presentation_generator.py sample_article.txt --slides 25")
        
        # Create a sample input file for testing
        sample_content = """
        # Sample Article: Introduction to Machine Learning
        
        Machine learning is a subset of artificial intelligence (AI) that provides systems 
        the ability to automatically learn and improve from experience without being 
        explicitly programmed.
        
        ## Types of Machine Learning
        
        1. **Supervised Learning**: Learning with labeled examples
        2. **Unsupervised Learning**: Finding patterns in unlabeled data
        3. **Reinforcement Learning**: Learning through interaction and feedback
        
        ## Applications
        
        Machine learning is used in various domains including:
        - Image recognition
        - Natural language processing
        - Recommendation systems
        - Fraud detection
        - Autonomous vehicles
        
        ## Conclusion
        
        Machine learning continues to evolve and impact various industries, 
        making it an essential technology for the future.
        """
        
        with open("sample_article.txt", "w") as f:
            f.write(sample_content)
        
        print("\n📄 Created sample_article.txt for testing")
        print("Try: python presentation_generator.py sample_article.txt")
    else:
        main()
