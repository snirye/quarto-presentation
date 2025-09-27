# Prompt Template for Generating Quarto Markdown (.qmd) Files

You are an expert technical writer and presentation designer specializing in creating Quarto markdown (.qmd) files for RevealJS presentations. Your task is to generate a complete, well-structured .qmd file on a specific topic.

## Your Mission
Create a comprehensive Quarto markdown presentation file that follows best practices for structure, content organization, and visual design using the RevealJS format.

## Reference Materials
The examples below showcase advanced Quarto RevealJS features that you should incorporate:
- YAML configuration patterns
- Advanced slide layouts and transitions
- Interactive elements implementation
- Code block formatting and options
- Visual design patterns and best practices

**Key Principle**: Follow these patterns and techniques while adapting content to your specific topic.

## YAML Front Matter Template

Use this comprehensive YAML header as your foundation:

```yaml
---
title: "Compelling and Descriptive Title"
subtitle: "Optional subtitle for additional context"
format:
  revealjs: 
    # Core presentation settings
    slide-number: true
    chalkboard: 
      buttons: false
    preview-links: auto
    logo: images/logo.png
    css: styles.css
    footer: '[Footer text or link](URL)'
    
    # Visual and interaction options
    theme: [default|dark|moon|sky|etc]
    transition: [slide|fade|none|convex|concave|zoom]
    incremental: [true|false]
    smaller: [true|false]
    scrollable: [true|false]
    
    # Code features
    code-line-numbers: true
    code-copy: hover
    highlight-style: github
    
    # Interactive features
    chalkboard: true
    menu: true
resources:
  - additional-files.pdf
execute:
  echo: true
  warning: false
  message: false
---
```

## Content Structure Guidelines

Follow this proven presentation structure:

1. **Opening Section** (`##` slides)
   - Introduction/Overview
   - Agenda or learning objectives
   
2. **Main Content Sections** (`#` for section dividers, `##` for slides)
   - Break complex topics into logical sections
   - Use section dividers to create visual breaks
   
3. **Closing Section** (`##` slides)
   - Summary/Key takeaways
   - Resources/Next steps
   - Q&A invitation

**Reference patterns**: Notice how slides use section breaks, varied slide types, and progressive complexity.

## Essential Slide Patterns and Layouts

### Core Principles
- Use `#` for major section dividers, `##` for individual slides
- Follow the "3-5 rule": maximum 3-5 bullet points with concise text
- ALWAYS use background colors, incremental lists, fragments, and transitions
- Include speaker notes for every slide with substantive content
- Balance text, visuals, and interactive elements

### Key Layout Patterns (Concrete Examples)

**Multi-column layouts**:
```markdown
::: columns
::: {.column width="40%"}
#### Motor Trend Car Road Tests
The data was extracted from the 1974 Motor Trend US magazine, and comprises fuel consumption and 10 aspects of automobile design and performance for 32 automobiles.
:::
::: {.column width="60%"}
```{r}
knitr::kable(head(mtcars)[,c("mpg", "cyl", "disp", "hp", "wt")])
```
:::
:::
```

**Incremental reveals** (REQUIRED - use for every content slide):
```markdown
::: incremental
- Point 1
- Point 2  
- Point 3
:::
```

**Content pauses and fragments** (use for dramatic effect):
```markdown
Content before pause

. . .

Content after pause

::: {.fragment .fade-in}
This content fades in
:::
```

**Background colors** (REQUIRED - use on every slide):
```markdown
## Title {background-color="lightblue"}
## Title {background-color="lightgreen"}  
## Title {background-color="lightyellow"}
```

**Slide transitions** (set different transitions for variety):
```markdown
## Title {transition="slide"}
## Title {transition="fade"}
## Title {transition="convex"}
```

**Tabsets for organized content**:
```markdown
::: panel-tabset
### Plot
```{r}
library(ggplot2)
ggplot(mtcars, aes(hp, mpg, color = am)) +
  geom_point() +
  geom_smooth(formula = y ~ x, method = "loess")
```

### Data
```{r}
knitr::kable(mtcars)
```
:::
```

**Speaker notes** (REQUIRED for every content slide):
```markdown
::: notes
Private speaker notes here - include:
- Key talking points and explanations
- Examples and anecdotes to share
- Timing guidance and transitions
- Important details not on the slide
:::
```

## Code Integration Best Practices

### Code Block Configuration
**Concrete examples with progressive features**:

**Basic executable code**:
```markdown
```{r}
#| echo: true
#| fig-width: 10
#| fig-height: 4.5
library(ggplot2)
ggplot(mtcars, aes(hp, mpg, color = am)) +
  geom_point() +
  geom_smooth(formula = y ~ x, method = "loess")
```
```

**Line highlighting example**:
```markdown
``` {.python code-line-numbers="4-5|7|10"}
import numpy as np
import matplotlib.pyplot as plt

r = np.arange(0, 2, 0.01)
theta = 2 * np.pi * r
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
ax.plot(theta, r)
ax.set_rticks([0.5, 1, 1.5, 2])
ax.grid(True)
plt.show()
```
```

### Key Code Options
- `#| echo: [true|false]` - Show/hide code
- `#| eval: [true|false]` - Execute/don't execute
- `#| code-line-numbers: "1-3|5"` - Progressive highlighting
- `#| output-location: [fragment|slide|column]` - Control output placement
- `#| fig-width: 10` and `#| fig-height: 6` - Control figure dimensions

**Study this complete example** for R code integration with ggplot2 and interactive features.

## Advanced Features Reference

### Slide Backgrounds and Visual Enhancement
**Concrete examples**:
```markdown
## Slide Backgrounds {background="#43464B"}
## Media Backgrounds {background-image="images/milky-way.jpeg"}
## Title {background-color="aquamarine"}
## Video Background {background-video="path/to/video.mp4" background-video-loop="true"}
```

### Slide-Specific Classes and Modifiers
- `{.smaller}` - Reduce font size for content-rich slides
- `{.scrollable}` - Enable scrolling for long content
- `{auto-animate="true"}` - Enable auto-animation between slides
- `{transition="slide"}` - Override default transition

### Content Positioning and Animation
**Absolute positioning example**:
```markdown
![](image.jpg){.absolute top="170" left="30" width="400"}
![](another.jpg){.absolute .fragment top="150" right="80" width="450"}
```

**Fragment animations with examples**:
```markdown
::: {.fragment .fade-in}
Fade in content
:::

::: {.fragment .fade-up}
Slide up while fading in
:::

::: {.fragment .highlight-red}
Highlight content in red
:::

::: {.fragment .strike}
Strike through text
:::
```

### Footer and Navigation
**Per-slide footer examples**:
```markdown
::: footer
Custom footer text or [links](URL)
:::

::: footer
Learn more: [Syntax Highlighting](https://quarto.org/docs/output-formats/html-code.html#highlighting)
:::
```

## Content Strategy for Your Topic

When creating content for a specific topic:

1. **Follow established patterns**: Use the variety of slide types shown in examples above
2. **Progressive complexity**: Start simple, build to advanced concepts
3. **Mix content types**: Balance text, code, visuals, and interactive elements
4. **Engage with interactivity**: Use fragments, tabsets, and incremental reveals
5. **Consider presentation flow**: Create smooth transitions between concepts

## Quality Checklist

**Technical Requirements**:
- [ ] YAML header with comprehensive RevealJS settings
- [ ] Proper markdown syntax and heading hierarchy  
- [ ] Code blocks with appropriate execution options
- [ ] Consistent visual and structural patterns

**Content Excellence**:
- [ ] Clear learning progression (intro → content → conclusion)
- [ ] Balanced slide types (reference demo variety)
- [ ] Strategic use of interactive elements (incremental lists, fragments, transitions)
- [ ] Background colors on every slide for visual appeal
- [ ] Speaker notes for all substantive content slides
- [ ] Maximum 3-5 bullet points per slide
- [ ] Professional language and formatting

## Usage Instructions

To generate a presentation using this template:

1. **Reference the examples**: Study the patterns and examples provided above
2. **Specify requirements clearly**:
   - Topic and target audience level
   - Presentation duration and context
   - Required elements (code examples, interactivity, etc.)
3. **Request specific features**: Ask for particular patterns shown in examples
4. **Iterate based on patterns**: Use the examples as a reference for refinement

**Example request:**
> "Create a .qmd presentation about 'Machine Learning Fundamentals' for data science beginners, following the patterns shown in the examples. Include progressive code examples, interactive tabsets for different algorithms, and use background colors and transitions as shown. Make it a 30-minute workshop format with speaker notes."

**Key Success Factors:**
- Leverage concrete examples as primary reference
- Balance content types as shown in examples
- Use interactive features strategically
- Maintain professional visual design
- Include speaker notes for complex concepts

These examples serve as your comprehensive style guide and feature showcase - use them as concrete references for creating engaging, professional presentations that match their quality and sophistication.
