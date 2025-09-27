<INSTRUCTIONS>
1. Create slide content using proper Quarto markdown syntax with a `##` header.
2. CONTENT LIMITS: Maximum 3-5 bullet points per slide. Keep bullets to 8-10 words each.
3. VISUAL ENHANCEMENTS: Include one or more of the following when appropriate:
   - Background colors: use `{{background-color="lightblue"}}` (or similar).
   - Incremental lists: wrap bullets in `::: incremental` / `:::`.
   - Content fragments: use `. . .` or `::: {{.fragment}}` blocks for staged reveals.
   - Slide transitions: add `{{transition="slide"}}` or `{{transition="fade"}}` to the slide header.
4. SPEAKER NOTES: Always include detailed speaker notes using `::: notes` blocks.
5. Focus on the top-level insights from the provided key points and avoid adding unrelated content.
6. Output must start with a `##` slide header and contain only the slide content and notes.
</INSTRUCTIONS>

<CONTEXT>
<ARTICLE_CONTENT>
{article_content}
</ARTICLE_CONTENT>

<PRESENTATION_STRUCTURE>
{structure}
</PRESENTATION_STRUCTURE>

<CURRENT_SLIDE>
<NUMBER>{slide_number}</NUMBER>
<TITLE>{slide_title}</TITLE>
<TYPE>{slide_type}</TYPE>
<KEY_POINTS>{key_points}</KEY_POINTS>
</CURRENT_SLIDE>

<QUARTO_REFERENCE>
{quarto_reference}
</QUARTO_REFERENCE>

<OUTPUT_RULES>
Generate ONLY the slide content (starting with `##`) and the speaker notes block. No additional text, explanation, or metadata.
</OUTPUT_RULES>
