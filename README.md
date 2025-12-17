# Santa Certificates

Generate personalized Santa Nice List certificates as HTML/PDF files.

## Features

- Beautiful festive certificate design with custom fonts
- Personalized messages for each child
- Embedded images (Christmas tree, wax seal) as base64
- Generates both HTML and PDF output

## Requirements

- Python 3.12+
- wkhtmltopdf (for PDF generation)

## Usage

### Quick Start

```bash
./generate_pdfs.sh
```

This generates HTML certificates in `build/` and converts them to PDF.

### Using Make

```bash
make setup      # Install dev dependencies
make generate   # Generate certificates
make clean      # Remove build artifacts
```

## Development

```bash
make format     # Format code with black/isort
make lint       # Lint with ruff
make type       # Type check with mypy
make quality    # Run all checks
```

## Project Structure

```
santa-certificates/
├── assets/              # Images (tree, wax seal)
├── build/               # Generated HTML and PDF files
├── templates/           # HTML template
├── generate_pdfs.sh     # Shell script to generate PDFs
├── santa_certificates.py # Main Python script
├── Makefile             # Development commands
└── pyproject.toml       # Project configuration
```
