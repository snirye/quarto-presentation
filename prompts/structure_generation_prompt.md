Based on the following article, create a general structure for a Quarto RevealJS presentation with exactly {num_slides} slides.

ARTICLE CONTENT:
{article_content}

INSTRUCTIONS:
1. Analyze the article and identify the main themes and concepts
2. Create a logical flow for a {num_slides}-slide presentation
3. Include an introduction, main content sections, and conclusion
4. For each slide, specify: slide_number, title, type (intro/content/conclusion), and key_points
5. CRITICAL: Limit key_points to maximum 3-4 items per slide to prevent content overload
6. Focus on the most essential concepts for each slide

Return ONLY a valid JSON object (no markdown formatting, no code blocks) with this exact structure:
{{
    "title": "Presentation Title",
    "slides": [
        {{
            "slide_number": 1,
            "title": "Slide Title",
            "type": "intro",
            "key_points": ["point1", "point2", "point3"]
        }},
        {{
            "slide_number": 2,
            "title": "Another Slide",
            "type": "content",
            "key_points": ["point1", "point2"]
        }}
    ]
}}

Make sure to include exactly {num_slides} slides and limit each slide to 3-4 key_points maximum. Return only the JSON, no other text.
