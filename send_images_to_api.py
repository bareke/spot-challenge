"""
This code iterates over a list of image filenames and sends each image file to
an API endpoint as a Base64-encoded string in JSON format.

It reads each image file, encodes it using Base64, and constructs a JSON payload
containing the current date, a camera ID, and the encoded image.

The code then makes a POST request to the specified URL with the JSON payload
and prints the response text and status code.
"""

import json
from base64 import b64encode
from datetime import datetime
from os import getcwd
from random import randint

import requests

encoded_string = None
path = getcwd()

url = "http://localhost:8000/api/images"

images = ["pycon.jpg", "flask.jpg", "django.jpg"] * 1000

for filename in images:
    with open(f"{path}/images_test/{filename}", "rb") as image_file:
        encode_string = b64encode(image_file.read()).decode("utf-8")

    data = {
        "date": str(datetime.utcnow()),
        "idCamera": randint(1, 10),
        "imageBase64": encode_string,
    }

    response = requests.post(url=url, json=data)
    print(response.text, response.status_code)
