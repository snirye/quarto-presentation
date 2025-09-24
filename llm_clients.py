#!/usr/bin/env python3
"""
Enhanced LLM Client for Quarto Presentation Generator

This module provides real LLM integration examples for the presentation generator.
Replace the placeholder LLMClient in presentation_generator.py with one of these implementations.
"""

import os
import json
from typing import Optional
from dotenv import load_dotenv

load_dotenv()

class OpenAIClient:
    """OpenAI GPT integration for presentation generation"""
    
    def __init__(self, api_key: Optional[str] = None, model: str = "gpt-4"):
        try:
            import openai
        except ImportError:
            raise ImportError("OpenAI library not installed. Run: pip install openai")
            
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("OpenAI API key required. Set OPENAI_API_KEY environment variable.")
            
        self.client = openai.OpenAI(api_key=self.api_key)
        self.model = model
        
    def generate_response(self, prompt: str) -> str:
        """Generate response using OpenAI API"""
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {
                        "role": "system", 
                        "content": "You are an expert presentation designer specializing in educational content and Quarto RevealJS presentations."
                    },
                    {"role": "user", "content": prompt}
                ],
                max_tokens=2000,
                temperature=0.7
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            print(f"❌ OpenAI API error: {e}")
            return self._fallback_response(prompt)
    
    def _fallback_response(self, prompt: str) -> str:
        """Provide fallback response if API fails"""
        if "general structure" in prompt.lower():
            return '''
            {
                "title": "Article Analysis Presentation",
                "slides": [
                    {"slide_number": 1, "title": "Introduction", "type": "intro", "key_points": ["Welcome", "Overview", "Objectives"]},
                    {"slide_number": 2, "title": "Main Topic", "type": "content", "key_points": ["Key concept", "Background"]},
                    {"slide_number": 3, "title": "Analysis", "type": "content", "key_points": ["Deep dive", "Examples"]},
                    {"slide_number": 4, "title": "Conclusion", "type": "conclusion", "key_points": ["Summary", "Takeaways"]}
                ]
            }
            '''
        else:
            return "## Fallback Slide\n\n- Content generation failed\n- Using fallback response\n- Please review and edit"


class AnthropicClient:
    """Anthropic Claude integration for presentation generation"""
    
    def __init__(self, api_key: Optional[str] = None, model: str = "claude-3-sonnet-20240229"):
        try:
            import anthropic
        except ImportError:
            raise ImportError("Anthropic library not installed. Run: pip install anthropic")
            
        self.api_key = api_key or os.getenv("ANTHROPIC_API_KEY")
        if not self.api_key:
            raise ValueError("Anthropic API key required. Set ANTHROPIC_API_KEY environment variable.")
            
        self.client = anthropic.Anthropic(api_key=self.api_key)
        self.model = model
        
    def generate_response(self, prompt: str) -> str:
        """Generate response using Anthropic Claude API"""
        try:
            response = self.client.messages.create(
                model=self.model,
                max_tokens=2000,
                temperature=0.7,
                system="You are an expert presentation designer specializing in educational content and Quarto RevealJS presentations.",
                messages=[{"role": "user", "content": prompt}]
            )
            return response.content[0].text.strip()
        except Exception as e:
            print(f"❌ Anthropic API error: {e}")
            return self._fallback_response(prompt)
    
    def _fallback_response(self, prompt: str) -> str:
        """Provide fallback response if API fails"""
        if "general structure" in prompt.lower():
            return '''
            {
                "title": "Article Analysis Presentation",
                "slides": [
                    {"slide_number": 1, "title": "Introduction", "type": "intro", "key_points": ["Welcome", "Overview", "Objectives"]},
                    {"slide_number": 2, "title": "Main Topic", "type": "content", "key_points": ["Key concept", "Background"]},
                    {"slide_number": 3, "title": "Analysis", "type": "content", "key_points": ["Deep dive", "Examples"]},
                    {"slide_number": 4, "title": "Conclusion", "type": "conclusion", "key_points": ["Summary", "Takeaways"]}
                ]
            }
            '''
        else:
            return "## Fallback Slide\n\n- Content generation failed\n- Using fallback response\n- Please review and edit"


class LocalLLMClient:
    """Local LLM integration (e.g., Ollama, LM Studio)"""
    
    def __init__(self, base_url: str = "http://localhost:11434", model: str = "llama2"):
        self.base_url = base_url
        self.model = model
        
    def generate_response(self, prompt: str) -> str:
        """Generate response using local LLM endpoint"""
        try:
            import requests
            
            payload = {
                "model": self.model,
                "prompt": prompt,
                "stream": False,
                "options": {
                    "temperature": 0.7,
                    "max_tokens": 2000
                }
            }
            
            response = requests.post(
                f"{self.base_url}/api/generate",
                json=payload,
                timeout=60
            )
            
            if response.status_code == 200:
                raw_response = response.json()["response"].strip()
                
                # Clean up response - remove markdown code blocks if present
                if "```json" in raw_response or "```" in raw_response:
                    # Extract JSON from markdown code blocks
                    import re
                    json_match = re.search(r'```(?:json)?\s*(\{.*?\})\s*```', raw_response, re.DOTALL)
                    if json_match:
                        return json_match.group(1).strip()
                    else:
                        # If no proper JSON block found, remove all ``` markers
                        cleaned = re.sub(r'```[a-zA-Z]*\n?', '', raw_response)
                        cleaned = re.sub(r'\n?```', '', cleaned)
                        return cleaned.strip()
                
                return raw_response
            else:
                raise Exception(f"HTTP {response.status_code}: {response.text}")
                
        except Exception as e:
            print(f"❌ Local LLM error: {e}")
            return self._fallback_response(prompt)
    
    def _fallback_response(self, prompt: str) -> str:
        """Provide fallback response if API fails"""
        if "general structure" in prompt.lower():
            return '''
            {
                "title": "Article Analysis Presentation",
                "slides": [
                    {"slide_number": 1, "title": "Introduction", "type": "intro", "key_points": ["Welcome", "Overview", "Objectives"]},
                    {"slide_number": 2, "title": "Main Topic", "type": "content", "key_points": ["Key concept", "Background"]},
                    {"slide_number": 3, "title": "Analysis", "type": "content", "key_points": ["Deep dive", "Examples"]},
                    {"slide_number": 4, "title": "Conclusion", "type": "conclusion", "key_points": ["Summary", "Takeaways"]}
                ]
            }
            '''
        else:
            return "## Fallback Slide\n\n- Content generation failed\n- Using fallback response\n- Please review and edit"


# Example usage and integration instructions
if __name__ == "__main__":
    print("🔧 LLM Client Integration Guide")
    print("\nTo integrate with presentation_generator.py:")
    print("\n1. Replace the LLMClient class in presentation_generator.py with one of:")
    print("   - OpenAIClient (for OpenAI GPT models)")
    print("   - AnthropicClient (for Claude models)")  
    print("   - LocalLLMClient (for local models like Ollama)")
    
    print("\n2. Set up your API keys:")
    print("   export OPENAI_API_KEY='your-key-here'")
    print("   # or")
    print("   export ANTHROPIC_API_KEY='your-key-here'")
    
    print("\n3. Install required dependencies:")
    print("   pip install openai  # for OpenAI")
    print("   pip install anthropic  # for Claude")
    print("   pip install requests  # for local LLM")
    
    print("\n4. Example replacement in presentation_generator.py:")
    print("""
    # Replace this line:
    llm_client = LLMClient(model=args.model)
    
    # With one of these:
    llm_client = OpenAIClient(model=args.model)
    llm_client = AnthropicClient(model=args.model)
    llm_client = LocalLLMClient(model=args.model)
    """)
    
    # Test if API keys are available
    print("\n🔍 Checking API keys:")
    if os.getenv("OPENAI_API_KEY"):
        print("✅ OpenAI API key found")
    else:
        print("❌ OpenAI API key not found")
        
    if os.getenv("ANTHROPIC_API_KEY"):
        print("✅ Anthropic API key found")
    else:
        print("❌ Anthropic API key not found")
