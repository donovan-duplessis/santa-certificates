#!/usr/bin/env python3
"""
Santa Certificate Generator.

Creates beautiful, personalized Christmas certificates as HTML files
that can be converted to PDF using wkhtmltopdf. Each certificate features
a festive design with custom fonts, a wax seal, Christmas tree icons,
and personalized messages from Santa.

Usage:
    python3 santa_certificates.py

Output:
    - build/<name>_certificate.html for each child
"""

import base64
import sys
from pathlib import Path
from typing import TypedDict


class ChildData(TypedDict):
    """Type definition for child certificate data."""
    name: str
    message: str
    gift: str
    gift_note: str
    filename: str


def load_template(template_path: Path) -> str:
    """Load the HTML template from file."""
    return template_path.read_text(encoding='utf-8')


def load_image_as_base64(image_path: Path, mime_type: str = "image/png") -> str:
    """Load an image file and return as base64 data URI."""
    with open(image_path, "rb") as f:
        encoded = base64.b64encode(f.read()).decode('utf-8')
    return f"data:{mime_type};base64,{encoded}"


def generate_certificate(child_data: ChildData, template: str, tree_image: str, seal_image: str) -> str:
    """
    Generate a personalized Santa certificate as an HTML string.

    Args:
        child_data: Dictionary containing the child's certificate details.
        template: The HTML template string.
        tree_image: Base64-encoded tree image data URI.
        seal_image: Base64-encoded seal image data URI.

    Returns:
        A complete HTML document as a string.

    Raises:
        KeyError: If required keys are missing from child_data.
    """
    required_keys = {"name", "message", "gift", "gift_note", "filename"}
    missing = required_keys - child_data.keys()
    if missing:
        raise KeyError(f"Missing required keys in child_data: {missing}")

    return template.format(
        name=child_data["name"],
        message=child_data["message"],
        gift=child_data["gift"],
        gift_note=child_data["gift_note"],
        tree_image=tree_image,
        seal_image=seal_image,
    )


def main() -> None:
    """
    Generate Santa certificates for children.

    Creates personalized HTML certificate files in the build directory.
    """
    # Define child data
    children: list[ChildData] = [
        {
            "name": "Lia du Plessis",
            "filename": "lia_certificate.html",
            "message": '''
                <p>My dear <span class="highlight">Lia</span>, what a remarkable young lady you have become!</p>

                <p>I've been watching you this year, and my goodness, you have made me SO proud!
                Your <span class="highlight">amazing school report</span> didn't go unnoticed up here at the North Pole -
                the elves were doing a happy dance when they saw your results!</p>

                <p>Now, I hear you're off to <span class="highlight">Paarl Girls' High</span> next year for Grade 8 -
                what an exciting new adventure awaits you! Starting high school AND living in the hostel...
                my dear, you are becoming such a <span class="highlight">brave and independent young lady</span>.
                Mom and Dad will miss you during the week, but they are bursting with pride!</p>

                <p>You're growing up so beautifully, and I know you'll shine bright at your new school.
                Remember, even when you're at the hostel, you carry your family's love with you always.
                And those weekends home? They'll be extra special!</p>

                <p>This gift is for YOU - to <span class="highlight">spoil yourself</span> and get some wonderful things
                for your exciting new chapter ahead. You deserve every bit of it!</p>
            ''',
            "gift": "R3,500",
            "gift_note": "Deposited into your account - treat yourself, superstar!"
        },
        {
            "name": "Daniel du Plessis",
            "filename": "daniel_certificate.html",
            "message": '''
                <p>My dear <span class="highlight">Daniel</span>, what an AWESOME young man you are!</p>

                <p>Ho ho ho! I've been keeping a very close eye on you this year, and WOW -
                your <span class="highlight">amazing school report</span> had the reindeer doing backflips!
                Even Rudolph said "That Dan is going places!"</p>

                <p>I know how much you LOVE your sports - whether it's tackling on the
                <span class="highlight">rugby</span> field, smashing sixes in <span class="highlight">cricket</span>,
                or scoring goals in backyard <span class="highlight">soccer</span> - you give it your ALL!
                That's what champions are made of!</p>

                <p>And those <span class="highlight">doggies</span> of yours? They're lucky to have such a
                caring friend who loves them so much. Your big heart for your family and your furry pals
                makes you extra special!</p>

                <p>Now, here's something important: Next year, with Lia at high school, you'll be
                <span class="highlight">the man of the house</span> during the week! I KNOW you're going to
                step up and be amazing - you've got this, champ! Grade 5 is going to be YOUR year!</p>

                <p>Keep being the incredible, sporty, kind-hearted legend that you are!</p>
            ''',
            "gift": "R2,500",
            "gift_note": "A special stocking stuffer for the amazing DanTheMan!"
        },
    ]

    # Setup paths
    script_dir = Path(__file__).parent.resolve()
    output_dir = script_dir / "build"
    template_path = script_dir / "templates" / "certificate.html"
    tree_path = script_dir / "assets" / "tree.png"
    seal_path = script_dir / "assets" / "wax_seal_small.jpg"

    try:
        output_dir.mkdir(exist_ok=True)
    except OSError as e:
        print(f"Error creating output directory: {e}", file=sys.stderr)
        sys.exit(1)

    # Load template and images once
    try:
        template = load_template(template_path)
        tree_image = load_image_as_base64(tree_path, "image/png")
        seal_image = load_image_as_base64(seal_path, "image/jpeg")
    except OSError as e:
        print(f"Error loading template or assets: {e}", file=sys.stderr)
        sys.exit(1)

    # Generate certificates
    for child in children:
        try:
            html = generate_certificate(child, template, tree_image, seal_image)
            output_path = output_dir / child["filename"]
            output_path.write_text(html, encoding='utf-8')
            print(f"Created {child['name']}'s certificate: {output_path}")
        except (OSError, KeyError) as e:
            print(f"Error creating certificate for {child.get('name', 'unknown')}: {e}", file=sys.stderr)
            sys.exit(1)

    print("\nHo Ho Ho! All certificates are ready!")
    print("Open the HTML files in a browser to view them")
    print("Print to PDF or directly print for physical copies")
    print("\nMerry Christmas!")


if __name__ == "__main__":
    main()
