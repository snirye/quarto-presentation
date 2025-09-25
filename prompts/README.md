# Prompts Directory

This directory contains all prompts used by the Quarto Presentation Generator, organized for easy maintenance and modification.

## Files

### Core Prompts

- **`system_prompt.md`** - System prompt that defines the AI assistant's role and expertise
- **`structure_generation_prompt.md`** - Template for generating presentation structure from articles
- **`slide_content_generation_prompt.md`** - Template for generating individual slide content
- **`quarto_generation_template.md`** - Comprehensive guide for creating Quarto RevealJS presentations

### Utility

- **`prompt_manager.py`** - Python utility for loading and managing prompts programmatically

## Usage

### In Python Code

```python
from prompts.prompt_manager import get_system_prompt, get_structure_prompt

# Load system prompt
system_prompt = get_system_prompt()

# Load formatted structure prompt
structure_prompt = get_structure_prompt(article_content, num_slides=20)
```

### Direct Access

```python
from prompts.prompt_manager import PromptManager

pm = PromptManager()
content = pm.load_prompt("system_prompt")
```

## Prompt Template Format

Prompts support Python string formatting with named placeholders:

```markdown
Generate content for slide {slide_number}.

ARTICLE: {article_content}
INSTRUCTIONS: {instructions}
```

## Modifying Prompts

1. Edit the relevant `.md` file in this directory
2. Test changes by running the presentation generator
3. The prompt manager automatically reloads prompts (no restart required)

## Adding New Prompts

1. Create a new `.md` file in this directory
2. Add a method to `prompt_manager.py` to load it
3. Update this README with documentation

## Best Practices

- Keep prompts focused and specific
- Use clear, actionable instructions
- Include examples when helpful
- Test prompts with different content types
- Document any special formatting requirements
