#!/usr/bin/env python3
"""
Prompt Management Utility

This module provides centralized access to all prompts used in the Quarto presentation generator.
"""

import os
from typing import Dict, Optional


class PromptManager:
    """Centralized prompt management for the Quarto presentation generator"""
    
    def __init__(self, prompts_dir: str = "prompts"):
        self.prompts_dir = prompts_dir
        self._prompts_cache = {}
        
    def load_prompt(self, prompt_name: str) -> str:
        """
        Load a prompt from the prompts directory
        
        Args:
            prompt_name: Name of the prompt file (with or without .md extension)
            
        Returns:
            The prompt content as a string
        """
        # Add .md extension if not present
        if not prompt_name.endswith('.md'):
            prompt_name += '.md'
            
        # Check cache first
        if prompt_name in self._prompts_cache:
            return self._prompts_cache[prompt_name]
            
        prompt_path = os.path.join(self.prompts_dir, prompt_name)
        
        try:
            with open(prompt_path, 'r', encoding='utf-8') as f:
                content = f.read().strip()
                
            # Cache the prompt
            self._prompts_cache[prompt_name] = content
            return content
            
        except FileNotFoundError:
            raise FileNotFoundError(f"Prompt file not found: {prompt_path}")
        except Exception as e:
            raise Exception(f"Error loading prompt {prompt_name}: {e}")
    
    def get_system_prompt(self) -> str:
        """Get the system prompt for LLM initialization"""
        return self.load_prompt("system_prompt")
    
    def get_structure_prompt(self, article_content: str, num_slides: int = 20) -> str:
        """
        Get the structure generation prompt with formatted content
        
        Args:
            article_content: The article content to analyze
            num_slides: Number of slides to generate
            
        Returns:
            Formatted prompt for structure generation
        """
        template = self.load_prompt("structure_generation_prompt")
        
        # Limit article content to avoid token limits
        limited_content = article_content[:5000]
        
        return template.format(
            article_content=limited_content,
            num_slides=num_slides
        )
    
    def get_slide_content_prompt(self, article_content: str, structure: str, 
                               slide_number: int, slide_title: str, 
                               slide_type: str, key_points: list, 
                               quarto_reference: str) -> str:
        """
        Get the slide content generation prompt with formatted content
        
        Args:
            article_content: The original article content
            structure: The presentation structure (JSON string)
            slide_number: Current slide number
            slide_title: Title of the current slide
            slide_type: Type of slide (intro/content/conclusion)
            key_points: List of key points for this slide
            quarto_reference: Quarto reference documentation
            
        Returns:
            Formatted prompt for slide content generation
        """
        template = self.load_prompt("slide_content_generation_prompt")
        
        # Limit content lengths to avoid token limits
        limited_content = article_content[:3000]
        limited_reference = quarto_reference[:2000]
        
        return template.format(
            article_content=limited_content,
            structure=structure,
            slide_number=slide_number,
            slide_title=slide_title,
            slide_type=slide_type,
            key_points=key_points,
            quarto_reference=limited_reference
        )
    
    def get_quarto_template(self) -> str:
        """Get the main Quarto generation template"""
        return self.load_prompt("quarto_generation_template")
    
    def list_available_prompts(self) -> list:
        """List all available prompt files"""
        try:
            return [f for f in os.listdir(self.prompts_dir) if f.endswith('.md')]
        except FileNotFoundError:
            return []
    
    def reload_prompts(self) -> None:
        """Clear the prompt cache to reload all prompts"""
        self._prompts_cache.clear()


# Global prompt manager instance
prompt_manager = PromptManager()


# Convenience functions for backward compatibility
def get_system_prompt() -> str:
    """Get system prompt (convenience function)"""
    return prompt_manager.get_system_prompt()


def get_structure_prompt(article_content: str, num_slides: int = 20) -> str:
    """Get structure generation prompt (convenience function)"""
    return prompt_manager.get_structure_prompt(article_content, num_slides)


def get_slide_content_prompt(article_content: str, structure: str, 
                           slide_number: int, slide_title: str, 
                           slide_type: str, key_points: list, 
                           quarto_reference: str) -> str:
    """Get slide content generation prompt (convenience function)"""
    return prompt_manager.get_slide_content_prompt(
        article_content, structure, slide_number, slide_title, 
        slide_type, key_points, quarto_reference
    )


if __name__ == "__main__":
    # Demo and testing
    print("🎯 Prompt Manager Utility")
    print(f"\nAvailable prompts: {prompt_manager.list_available_prompts()}")
    
    # Test loading prompts
    try:
        system_prompt = prompt_manager.get_system_prompt()
        print(f"\n✅ System prompt loaded ({len(system_prompt)} characters)")
        
        quarto_template = prompt_manager.get_quarto_template()
        print(f"✅ Quarto template loaded ({len(quarto_template)} characters)")
        
        print("\n🚀 Prompt manager ready for use!")
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
