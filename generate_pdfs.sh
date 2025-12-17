#!/bin/bash
set -euo pipefail

# Generate Santa Certificates for Lia and Daniel du Plessis

# Change to script's directory
cd "$(dirname "$0")"

# Check dependencies
check_dependency() {
    if ! command -v "$1" >/dev/null 2>&1; then
        echo "Error: $1 is required but not installed." >&2
        exit 1
    fi
}

check_dependency python3
check_dependency wkhtmltopdf

# Ensure build directory exists
mkdir -p build

echo "Generating HTML certificates..."
python3 santa_certificates.py

# Common wkhtmltopdf options
WKHTMLTOPDF_OPTS=(
    --enable-local-file-access
    --page-size A4
    --margin-top 0
    --margin-bottom 0
    --margin-left 0
    --margin-right 0
    --dpi 300
    --print-media-type
    --disable-smart-shrinking
)

echo "Converting Lia's certificate to PDF..."
wkhtmltopdf "${WKHTMLTOPDF_OPTS[@]}" "build/lia_certificate.html" "build/lia_certificate.pdf"

echo "Converting Daniel's certificate to PDF..."
wkhtmltopdf "${WKHTMLTOPDF_OPTS[@]}" "build/daniel_certificate.html" "build/daniel_certificate.pdf"

echo ""
echo "Done! PDFs created in build/:"
echo "  - build/lia_certificate.pdf"
echo "  - build/daniel_certificate.pdf"
