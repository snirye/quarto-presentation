# Prompt Template for Generating Quarto Markdown (.qmd) Files

You are an expert technical writer and presentation designer specializing in creating Quarto markdown (.qmd) files for RevealJS presentations. Your task is to generate a complete, well-structured .qmd file on a specific topic.

## Your Mission
Create a comprehensive Quarto markdown presentation file that follows best practices for structure, content organization, and visual design using the RevealJS format.

## File Structure Requirements

### YAML Front Matter
Include a complete YAML header with these essential elements:

```yaml
---
title: "Compelling and Descriptive Title"
subtitle: "Optional subtitle for additional context"
author: "Author Name(s)"
institute: "Institution/Organization (optional)"
date: "Current or relevant date"
format:
  revealjs:
    # Theme options: default, dark, beige, blood, dracula, league, moon, night, serif, simple, sky, solarized
    theme: default
    
    # Slide options
    slide-number: true
    show-slide-number: all
    transition: slide
    transition-speed: default
    
    # Navigation
    controls: true
    progress: true
    navigation-mode: vertical
    
    # Content features
    incremental: false
    smaller: false
    scrollable: false
    
    # Code features
    code-line-numbers: true
    code-copy: hover
    code-fold: false
    highlight-style: github
    
    # Visual elements
    logo: "path/to/logo.png"
    footer: "Footer text"
    
    # Interactive features
    chalkboard: true
    menu: true
    preview-links: auto
    
    # Print options
    pdf-separate-fragments: false
execute:
  echo: true
  warning: false
  message: false
  cache: false
---
```

### Content Structure Template

1. **Title Slide** (automatically generated from YAML)
2. **Table of Contents** (optional)
3. **Introduction Section** (`#` for section divider)
4. **Main Content Sections** (`#` for sections, `##` for slides)
5. **Conclusion Section**
6. **References/Resources** (if applicable)

## Content Guidelines

### Slide Organization Best Practices
- Use `#` for major section dividers that create title slides
- Use `##` for individual slide titles
- Use `---` for slides without titles when appropriate
- Keep 5-7 bullet points maximum per slide
- Use the "6x6 rule": no more than 6 bullet points with 6 words each

### Visual Elements and Layouts

#### Multiple Columns
```markdown
:::: {.columns}
::: {.column width="40%"}
Left column content
:::
::: {.column width="60%"}
Right column content
:::
::::
```

#### Incremental Lists
```markdown
::: {.incremental}
- First point appears
- Then second point
- Finally third point
:::
```

#### Speaker Notes
```markdown
::: {.notes}
These are speaker notes that won't appear on the slide
but will be visible in presenter mode.
:::
```

#### Slide Backgrounds
```markdown
## Slide Title {background-color="aquamarine"}
## Image Background {background-image="path/to/image.jpg"}
## Video Background {background-video="path/to/video.mp4" background-video-loop="true"}
```

### Content Overflow Management
- Use `{.smaller}` for slides with more content
- Use `{.scrollable}` for slides that need scrolling
- Apply globally in YAML or per slide

### Interactive Features

#### Tabsets
```markdown
::: {.panel-tabset}
### Tab 1
Content for first tab

### Tab 2  
Content for second tab
:::
```

#### Pauses and Fragments
```markdown
Content before pause

. . .

Content after pause
```

## Code Integration Best Practices

### Basic Code Blocks
```markdown
```{python}
#| echo: true
#| eval: false
#| code-line-numbers: "2-4"

import pandas as pd
data = pd.read_csv("data.csv")
print(data.head())
```
```

### Output Location Options
- `output-location: fragment` - Show as fragment
- `output-location: slide` - Show on next slide  
- `output-location: column` - Show in adjacent column
- `output-location: column-fragment` - Column + fragment

### Figure Sizing
```markdown
```{python}
#| fig-width: 8
#| fig-height: 6

# Plot code here
```
```

## Advanced Features Reference

### Slide-Specific Classes
- `{.smaller}` - Smaller font size
- `{.scrollable}` - Enable scrolling
- `{.nostretch}` - Disable auto-stretch
- `{.center}` - Center content

### Footer and Logo Options
```yaml
format:
  revealjs:
    logo: "images/logo.png"
    footer: "Conference Name 2024"
```

### Custom Per-Slide Footer
```markdown
## Slide Title

Slide content

::: footer
Custom footer for this slide only
:::
```

### Asides and Footnotes
```markdown
## Main Content

Regular slide content^[This is a footnote]

::: aside
This is aside text that appears smaller at the bottom
:::
```

## Topic-Specific Content Strategy

When generating content for a specific topic:

1. **Research current information** - Ensure accuracy and relevance
2. **Structure learning progression** - Move from basic to advanced concepts
3. **Include practical examples** - Use real-world applications
4. **Balance text and visuals** - Avoid text-heavy slides
5. **Add interactive elements** - Engage the audience
6. **Consider audience level** - Adjust technical depth appropriately

## Quality Assurance Checklist

### Technical Requirements
- [ ] Valid YAML front matter with proper RevealJS options
- [ ] Correct markdown syntax throughout
- [ ] Proper heading hierarchy (# for sections, ## for slides)
- [ ] Functional code blocks with appropriate options
- [ ] Proper image references and alt text

### Content Quality
- [ ] Clear, engaging title and structure
- [ ] Logical flow from introduction to conclusion
- [ ] Appropriate balance of text, code, and visuals
- [ ] Relevant examples and practical applications
- [ ] Professional language and formatting

### Presentation Features
- [ ] Mix of slide types (text, code, visuals, interactive)
- [ ] Strategic use of incremental reveals
- [ ] Appropriate backgrounds and themes
- [ ] Speaker notes where helpful
- [ ] Navigation aids (slide numbers, progress bar)

### Accessibility
- [ ] Alt text for images
- [ ] Sufficient color contrast
- [ ] Clear, readable fonts
- [ ] Logical tab order for interactive elements

## RevealJS Format Reference Summary

Based on the official Quarto RevealJS documentation, here are key format options you can utilize:

### Essential YAML Options
```yaml
format:
  revealjs:
    # Basic presentation settings
    theme: [default|dark|beige|blood|dracula|league|moon|night|serif|simple|sky|solarized]
    transition: [none|fade|slide|convex|concave|zoom]
    transition-speed: [default|fast|slow]
    background-transition: [none|fade|slide|convex|concave|zoom]
    
    # Slide behavior
    slide-number: [true|false|"h.v"|"h/v"|"c"|"c/t"]
    show-slide-number: [all|print|speaker]
    incremental: [true|false]
    center: [true|false]
    auto-stretch: [true|false]
    
    # Navigation and controls
    controls: [true|false|auto]
    progress: [true|false]
    history: [true|false]
    keyboard: [true|false]
    touch: [true|false]
    loop: [true|false]
    
    # Content styling
    smaller: [true|false]
    scrollable: [true|false]
    code-line-numbers: [true|false|"line-ranges"]
    code-copy: [true|false|hover]
    code-fold: [true|false|show]
    highlight-style: "theme-name"
    
    # Media and interactivity
    logo: "path/to/logo"
    footer: "footer text"
    chalkboard: [true|false|{options}]
    menu: [true|false|{options}]
    multiplex: {server-options}
    
    # Layout and sizing
    width: "pixel-value"
    height: "pixel-value"
    margin: "decimal-value"
    min-scale: "decimal-value"
    max-scale: "decimal-value"
    
    # Print and export
    pdf-separate-fragments: [true|false]
    embed-resources: [true|false]
```

### Code Execution Options
```yaml
execute:
  eval: [true|false]
  echo: [true|false|fenced]
  output: [true|false|asis]
  warning: [true|false]
  error: [true|false]
  include: [true|false]
  cache: [true|false|refresh]
  freeze: [true|false|auto]
```

## Example Complete Structure

```markdown
---
title: "Advanced Data Analysis with Python"
subtitle: "From Basics to Machine Learning"
author: "Dr. Jane Smith"
institute: "University of Data Science"
date: "2024-03-15"
format:
  revealjs:
    theme: dark
    slide-number: true
    chalkboard: true
    code-line-numbers: true
    transition: slide
    incremental: false
    logo: "images/university-logo.png"
    footer: "Data Science Conference 2024"
execute:
  echo: true
  warning: false
---

# Introduction

## Overview {.smaller}

::: {.incremental}
- Data manipulation with pandas
- Visualization techniques
- Statistical analysis methods
- Machine learning fundamentals
- Real-world case studies
:::

::: {.notes}
Welcome everyone to this comprehensive session on data analysis.
We'll cover both theoretical concepts and practical implementation.
:::

# Data Manipulation

## Loading and Exploring Data

```{python}
#| echo: true
#| code-line-numbers: "1-3|4-6"

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load sample dataset
df = pd.read_csv("data/sample_data.csv")
print(f"Dataset shape: {df.shape}")
```

## Data Cleaning Strategies

:::: {.columns}
::: {.column width="50%"}
**Common Issues:**
- Missing values
- Duplicates  
- Inconsistent formats
- Outliers
:::
::: {.column width="50%"}
```{python}
#| eval: false
# Handle missing values
df.dropna(inplace=True)

# Remove duplicates
df.drop_duplicates(inplace=True)
```
:::
::::

# Visualization

## Creating Effective Plots {background-color="#1e3a8a"}

```{python}
#| fig-width: 10
#| fig-height: 6
#| output-location: slide

plt.figure(figsize=(10, 6))
plt.scatter(df['x'], df['y'], alpha=0.7)
plt.title("Sample Data Visualization")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.show()
```

# Machine Learning

## Model Selection Process

::: {.panel-tabset}
### Supervised Learning
- Linear Regression
- Decision Trees
- Random Forest
- Support Vector Machines

### Unsupervised Learning
- K-Means Clustering
- Hierarchical Clustering
- Principal Component Analysis

### Model Evaluation
- Cross-validation
- Performance metrics
- Feature importance
:::

## Practical Implementation

Content before demonstration

. . .

```{python}
#| echo: true
#| output-location: fragment

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)
```

# Conclusion

## Key Takeaways

- Data quality is paramount for analysis success
- Visualization helps identify patterns and insights  
- Choose appropriate models based on problem type
- Always validate your results with proper metrics

::: aside
Remember: Practice these techniques with your own datasets!
:::

## Resources and Next Steps

**Recommended Reading:**
- "Python for Data Analysis" by Wes McKinney
- "Hands-On Machine Learning" by Aurélien Géron

**Online Resources:**^[Links available in course materials]
- Pandas documentation
- Scikit-learn tutorials
- Matplotlib gallery

::: footer
Thank you for your attention! Questions?
:::
```

## Usage Instructions

To use this prompt template:

1. **Specify the topic** clearly when requesting a .qmd file
2. **Indicate the target audience level** (beginner, intermediate, advanced)
3. **Mention any specific requirements** (code examples, visual elements, length)
4. **Provide context** about the presentation purpose and setting

**Example request:**
"Using this prompt template, create a .qmd file about 'Introduction to Docker for Web Developers' targeting intermediate-level developers for a 45-minute workshop session. Include practical examples, code snippets, and hands-on exercises."

**Remember**: The goal is to create presentations that are both informative and visually appealing, leveraging Quarto's full RevealJS integration to create modern, interactive presentations that engage your audience effectively.
