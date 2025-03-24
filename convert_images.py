#!/usr/bin/env python3


import os
from PIL import Image



input_dir = os.path.expanduser("~/images")
output_dir = "/opt/icons"


if not os.path.exists(output_dir):
    os.makedirs(output_dir)


for filename in os.listdir(input_dir):

    input_filepath = os.path.join(input_dir, filename)

    output_filepath = os.path.join(output_dir, os.path.splitext(filename)[0] + ".jpeg")



    try:

        with Image.open(input_filepath) as img:

            print(f"Processing: {filename}")  # Debugging

            img = img.rotate(-90).resize((128, 128)).convert("RGB")

            img.save(output_filepath, "JPEG")

            print(f"Saved: {output_filepath}")  # Debugging

    except Exception as e:

        print(f"Error processing {filename}: {e}")



print("Image processing complete!")