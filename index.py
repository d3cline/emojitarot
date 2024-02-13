#!/usr/bin/env python3.6
import cgi
import cgitb
import json
import sys

# Enable error tracebacks in the browser
cgitb.enable()

# Import your Tarot script
from tarot import get_cards

# Set the content type to JSON
print("Content-type: application/json")

# Define the Content Security Policy (CSP) header
csp_header = "Content-Security-Policy: default-src *;\n"

# Print the CSP header
print(csp_header)

# Read JSON data from stdin
try:
    data = json.load(sys.stdin)
except ValueError:
    response = {"error": "Invalid JSON data"}
    print(json.dumps(response))
    sys.exit(1)

# Check if the 'card_numbers' field exists in the JSON data
if "card_numbers" not in data:
    response = {"error": "No card_numbers parameter provided"}
else:
    # Get the 'card_numbers' parameter as a list of integers
    try:
        card_numbers = [int(card_number) for card_number in data["card_numbers"]]
    except ValueError:
        response = {"error": "Invalid input. All values must be integers."}
    else:
        # Call the get_cards function from your Tarot script
        cards = get_cards(card_numbers)
        response = {"cards": cards}

# Serialize the response as JSON
print(json.dumps(response))

