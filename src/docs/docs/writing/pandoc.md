
# Pandoc

## Awesome links

- [Pandoc ->](https://pandoc.org/)

## Basic Usage

### Converting a File

```sh
# Convert a file from markdown to HTML
pandoc input.md -o output.html
```

### Specifying Input and Output Formats

```sh
# Convert a file from markdown to PDF
pandoc -f markdown -t pdf input.md -o output.pdf
```

### Adding Metadata

```sh
# Add title and author metadata
pandoc input.md -o output.html -M title="Document Title" -M author="Author Name"
```

## Common Conversions

### Markdown to PDF

```sh
pandoc input.md -o output.pdf
```

### Markdown to Word

```sh
pandoc input.md -o output.docx
```

### HTML to Markdown

```sh
pandoc input.html -o output.md
```

### LaTeX to Word

```sh
pandoc input.tex -o output.docx
```

## Advanced Options

### Table of Contents

```sh
# Generate a table of contents
pandoc input.md -o output.html --toc
```

### Numbered Sections

```sh
# Generate numbered sections
pandoc input.md -o output.html --number-sections
```

### Citations and Bibliography

```sh
# Add citations and bibliography
pandoc input.md -o output.pdf --bibliography=biblio.bib
```

### Templates

```sh
# Use a custom template
pandoc input.md -o output.pdf --template=template.tex
```

### Filters

```sh
# Apply a custom filter
pandoc input.md -o output.html --filter=myfilter.py
```

## Styling and Formatting

### Custom CSS

```sh
# Use custom CSS for HTML output
pandoc input.md -o output.html --css=style.css
```

### Highlighting Code

```sh
# Highlight code syntax
pandoc input.md -o output.html --highlight-style=pygments
```

## Combining Multiple Files

### Merging Files

```sh
# Merge multiple files into one
pandoc part1.md part2.md -o output.pdf
```

### Including Files

```markdown
<!-- Include another file in markdown -->
\input{file.md}
```

## Math and Equations

### LaTeX Math

```sh
# Convert markdown with LaTeX math to PDF
pandoc input.md -o output.pdf --mathjax
```

## Example Commands

### Markdown to HTML with Table of Contents

```sh
pandoc input.md -o output.html --toc
```

### Markdown to PDF with Numbered Sections

```sh
pandoc input.md -o output.pdf --number-sections
```

### Markdown to Word with Citations

```sh
pandoc input.md -o output.docx --bibliography=biblio.bib
```

### HTML to Markdown with Custom Filter

```sh
pandoc input.html -o output.md --filter=myfilter.py
```

### LaTeX to PDF with Custom Template

```sh
pandoc input.tex -o output.pdf --template=template.tex
```
