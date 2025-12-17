#!/usr/bin/env python3
"""
Santa Certificate Generator for Lia and Daniel du Plessis.

Creates beautiful, personalized Christmas certificates as HTML files
that can be converted to PDF using wkhtmltopdf. Each certificate features
a festive design with custom fonts, a wax seal, Christmas tree icons,
and personalized messages from Santa.

Usage:
    python3 santa_certificates.py

Output:
    - build/lia_certificate.html
    - build/daniel_certificate.html
"""

from pathlib import Path


def generate_certificate(child_data: dict) -> str:
    """
    Generate a personalized Santa certificate as an HTML string.

    Creates a complete HTML document with embedded CSS styling for an A4-sized
    certificate. The design includes festive fonts, a red border, gradient
    background, gift box section, and placeholders for Christmas tree icons
    and a wax seal image.

    Args:
        child_data: A dictionary containing the child's certificate details.
            Required keys:
                - name (str): The child's full name.
                - message (str): HTML-formatted personalized message from Santa.
                - gift (str): The gift amount (e.g., "R3,500").
                - gift_note (str): A short note about the gift.

    Returns:
        A complete HTML document as a string, ready to be written to a file
        or converted to PDF.
    """

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Santa's Special Certificate - {child_data["name"]}</title>
    <link href="https://fonts.googleapis.com/css2?family=Mountains+of+Christmas:wght@400;700&family=Dancing+Script:wght@400;700&family=Quicksand:wght@400;500;600&display=swap" rel="stylesheet">
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        img.emoji {{
            height: 1.2em;
            width: 1.2em;
            margin: 0 .1em 0 .1em;
            vertical-align: -0.15em;
            object-fit: contain;
        }}

        @page {{
            size: A4;
            margin: 0;
        }}

        html, body {{
            font-family: 'Quicksand', 'Noto Color Emoji', 'Apple Color Emoji', 'Segoe UI Emoji', sans-serif;
            background: #ffffff;
            margin: 0;
            padding: 0;
            height: 297mm;
            width: 210mm;
            box-sizing: border-box;
        }}

        .spacer-top {{
            height: 8mm;
            width: 100%;
        }}

        .certificate {{
            background: linear-gradient(180deg, #fffef5 0%, #fff9e6 50%, #fffef5 100%);
            background-color: #fffef5 !important;
            width: calc(210mm - 16mm);
            height: 281mm;
            margin: 0 8mm 0 8mm;
            padding: 20px 30px;
            border: 8px solid #c41e3a;
            border-color: #c41e3a !important;
            border-radius: 12px;
            box-sizing: border-box;
            position: relative;
            overflow: hidden;
            -webkit-print-color-adjust: exact;
            print-color-adjust: exact;
            display: flex;
            flex-direction: column;
        }}

        .certificate::before {{
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background-image:
                radial-gradient(circle at 10% 10%, rgba(196, 30, 58, 0.05) 0%, transparent 50%),
                radial-gradient(circle at 90% 90%, rgba(22, 91, 51, 0.05) 0%, transparent 50%);
            pointer-events: none;
        }}

        .snowflakes {{
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            pointer-events: none;
            overflow: hidden;
        }}

        .snowflake {{
            position: absolute;
            color: rgba(200, 200, 220, 0.3);
            font-size: 20px;
            animation: fall linear infinite;
        }}

        @keyframes fall {{
            0% {{ transform: translateY(-100px) rotate(0deg); opacity: 1; }}
            100% {{ transform: translateY(800px) rotate(360deg); opacity: 0.3; }}
        }}

        .header {{
            text-align: center;
            margin-bottom: 12px;
            margin-top: -10px;
        }}

        .santa-image {{
            font-size: 16px;
            margin-bottom: 5px;
            filter: drop-shadow(2px 2px 4px rgba(0,0,0,0.2));
        }}

        .santa-image img.emoji {{
            height: 80px !important;
            width: 80px !important;
        }}

        .ho-ho-ho {{
            font-family: 'Mountains of Christmas', cursive;
            font-size: 34px;
            color: #c41e3a;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
            margin-bottom: 12px;
            letter-spacing: 3px;
            margin-left: -70px;
        }}

        .north-pole {{
            font-family: 'Dancing Script', cursive;
            font-size: 15px;
            color: #165b33;
            margin-bottom: 8px;
        }}

        .title {{
            font-family: 'Mountains of Christmas', cursive;
            font-size: 28px;
            color: #165b33;
            margin-bottom: 3px;
            text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
        }}

        .recipient {{
            font-family: 'Dancing Script', cursive;
            font-size: 38px;
            color: #c41e3a;
            margin: 8px 0;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        }}

        .divider {{
            display: flex;
            align-items: center;
            justify-content: center;
            margin: 10px 0;
        }}

        .divider-line {{
            flex: 1;
            height: 2px;
            background: linear-gradient(90deg, transparent, #c41e3a, transparent);
        }}

        .divider-icon {{
            margin: 0 15px;
            font-size: 20px;
        }}

        .message {{
            font-size: 15px;
            line-height: 1.75;
            color: #2c3e50;
            text-align: center;
            padding: 0 15px;
            margin-bottom: 15px;
            flex-grow: 1;
        }}

        .message p {{
            margin-bottom: 12px;
        }}

        .highlight {{
            color: #c41e3a;
            font-weight: 600;
        }}

        .gift-box {{
            background: #c41e3a;
            background-color: #c41e3a !important;
            color: #ffffff !important;
            padding: 12px 20px;
            border-radius: 12px;
            margin: 15px auto;
            max-width: 420px;
            text-align: center;
            box-shadow: 0 6px 20px rgba(196, 30, 58, 0.3);
            position: relative;
            -webkit-print-color-adjust: exact;
            print-color-adjust: exact;
        }}

        .gift-box::before {{
            content: '🎁';
            position: absolute;
            top: -10px;
            left: 50%;
            transform: translateX(-50%);
            font-size: 18px;
            background: #fffef5;
            padding: 2px 6px;
            border-radius: 50%;
        }}

        .gift-title {{
            font-family: 'Mountains of Christmas', cursive;
            font-size: 18px;
            margin-bottom: 5px;
            margin-top: 8px;
            color: #ffffff !important;
        }}

        .gift-amount {{
            font-family: 'Dancing Script', cursive;
            font-size: 30px;
            font-weight: bold;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
            color: #ffffff !important;
        }}

        .gift-note {{
            font-size: 12px;
            margin-top: 5px;
            color: #ffffff !important;
        }}

        .gift-snowflake {{
            position: absolute;
            top: 4px;
            left: 8px;
            font-size: 42px;
            color: #ffffff !important;
            opacity: 0.85;
            font-family: serif;
            font-weight: bold;
        }}

        .closing {{
            text-align: center;
            margin-top: 25px;
        }}

        .merry-christmas {{
            font-family: 'Mountains of Christmas', cursive;
            font-size: 26px;
            color: #165b33;
            margin-bottom: 5px;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 10px;
        }}

        .tree-icon {{
            height: 30px;
            width: auto;
            vertical-align: middle;
            margin-top: -6px;
        }}

        .signature {{
            font-family: 'Dancing Script', cursive;
            font-size: 28px;
            color: #c41e3a;
            margin: 8px 0;
        }}

        .from-line {{
            font-size: 12px;
            color: #666;
            margin-bottom: 3px;
        }}

        .footer-icons {{
            font-size: 22px;
            margin-top: 8px;
            letter-spacing: 8px;
        }}

        .seal {{
            position: absolute;
            bottom: 25px;
            right: 25px;
            width: 90px;
            height: 90px;
        }}

        .seal img {{
            width: 100%;
            height: 100%;
            object-fit: contain;
        }}

        .corner-decor {{
            position: absolute;
            font-size: 30px;
            opacity: 0.15;
        }}

        .corner-tl {{ top: 10px; left: 10px; }}
        .corner-bl {{ bottom: 10px; left: 10px; }}
        .corner-br {{ bottom: 10px; right: 10px; }}

        .year {{
            font-family: 'Mountains of Christmas', cursive;
            font-size: 14px;
            color: #165b33;
            margin-top: 5px;
        }}

        @media print {{
            body {{
                background: white;
                padding: 0;
            }}
            .certificate {{
                box-shadow: none;
                border: 8px solid #c41e3a;
            }}
        }}
    </style>
</head>
<body>
    <div class="spacer-top"></div>
    <div class="certificate">

        <!-- Header -->
        <div class="header">
            <div class="ho-ho-ho">Ho Ho Ho!</div>
            <div class="north-pole">Official Letter from the North Pole</div>
            <div class="title">Santa's Special Certificate</div>
            <div class="title" style="font-size: 24px;">for an Amazing Child</div>
        </div>

        <div class="divider">
            <div class="divider-line"></div>
        </div>

        <!-- Recipient Name -->
        <div style="text-align: center;">
            <div class="recipient">{child_data["name"]}</div>
        </div>

        <div class="divider">
            <div class="divider-line"></div>
        </div>

        <!-- Personalized Message -->
        <div class="message">
            {child_data["message"]}
        </div>

        <!-- Gift Box -->
        <div class="gift-box">
            <div class="gift-snowflake">❄</div>
            <div class="gift-title">Santa's Special Gift</div>
            <div class="gift-amount">{child_data["gift"]}</div>
            <div class="gift-note">{child_data["gift_note"]}</div>
        </div>

        <!-- Closing -->
        <div class="closing">
            <div class="merry-christmas"><img src="../assets/tree.png" class="tree-icon"> Merry Christmas! <img src="../assets/tree.png" class="tree-icon"></div>
            <div class="from-line">With love and Christmas magic from</div>
            <div class="signature">Santa Claus</div>
        </div>

        <!-- Wax Seal -->
        <div class="seal">
            <img src="../assets/wax_seal_small.jpg" alt="Official Santa Seal">
        </div>
    </div>
</body>
</html>'''


# Lia's personalized data
lia_data = {
    "name": "Lia du Plessis",
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
}

# Daniel's personalized data
daniel_data = {
    "name": "Daniel du Plessis",
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
}


def main() -> None:
    """
    Generate Santa certificates for Lia and Daniel du Plessis.

    Creates personalized HTML certificate files in the build directory
    using the predefined child data dictionaries. Prints progress messages
    to stdout as each certificate is generated.

    Returns:
        None
    """

    output_dir = Path("/home/donovan/code/santa/build")

    # Generate Lia's certificate
    lia_html = generate_certificate(lia_data)
    lia_path = output_dir / "lia_certificate.html"
    lia_path.write_text(lia_html, encoding='utf-8')
    print(f"✨ Created Lia's certificate: {lia_path}")

    # Generate Daniel's certificate
    daniel_html = generate_certificate(daniel_data)
    daniel_path = output_dir / "daniel_certificate.html"
    daniel_path.write_text(daniel_html, encoding='utf-8')
    print(f"✨ Created Daniel's certificate: {daniel_path}")

    print("\n🎅 Ho Ho Ho! Both certificates are ready!")
    print("📄 Open the HTML files in a browser to view them")
    print("🖨️  Print to PDF or directly print for physical copies")
    print("\n🎄 Merry Christmas to the du Plessis family! 🎄")


if __name__ == "__main__":
    main()
