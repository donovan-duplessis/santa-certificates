#!/bin/bash

# Generate Santa Certificates for Lia and Daniel du Plessis

# Change to script's directory
cd "$(dirname "$0")"

echo "Generating HTML certificates..."
python3 santa_certificates.py

echo "Converting Lia's certificate to PDF..."
wkhtmltopdf --enable-local-file-access --page-size A4 --margin-top 0 --margin-bottom 0 --margin-left 0 --margin-right 0 --dpi 300 --print-media-type --disable-smart-shrinking build/lia_certificate.html lia_certificate.pdf

echo "Converting Daniel's certificate to PDF..."
wkhtmltopdf --enable-local-file-access --page-size A4 --margin-top 0 --margin-bottom 0 --margin-left 0 --margin-right 0 --dpi 300 --print-media-type --disable-smart-shrinking build/daniel_certificate.html daniel_certificate.pdf

echo ""
echo "Done! PDFs created:"
echo "  - lia_certificate.pdf"
echo "  - daniel_certificate.pdf"
