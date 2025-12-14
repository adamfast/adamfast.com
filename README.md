# adamfast.com
Personal Static Site

## About

This is a personal website for Adam Fast, built with [Pelican](https://getpelican.com/), a Python-based static site generator.

## Setup

1. Install Python dependencies:
```bash
pip install -r requirements.txt
```

2. Generate the site:
```bash
make html
```

3. Serve the site locally:
```bash
make serve
```

The site will be available at http://localhost:8000

## Building for Production

To generate the site with production settings:
```bash
make publish
```

The generated files will be in the `output/` directory.

## Project Structure

- `content/` - Content files (Markdown)
- `themes/simple/` - Custom theme
- `pelicanconf.py` - Development configuration
- `publishconf.py` - Production configuration
- `output/` - Generated static site (not in git)

## Features

- Single-page personal website
- Responsive design
- Clean, professional styling
- Easy to customize and extend
