"""
Prompts package for Quarto Presentation Generator

This package provides centralized prompt management for the presentation generator.
"""

from .prompt_manager import (
    PromptManager,
    prompt_manager,
    get_system_prompt,
    get_structure_prompt,
    get_slide_content_prompt
)

__all__ = [
    'PromptManager',
    'prompt_manager',
    'get_system_prompt',
    'get_structure_prompt',
    'get_slide_content_prompt'
]
