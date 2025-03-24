# image-processing-python
Python script to rotate, resize, and convert images using PIL.

🖼️ Image Processing Script (Python + PIL)

📌 Overview

This Python script automates the process of rotating, resizing, and converting images to the required format.
It was developed as part of a hands-on lab to process a batch of images efficiently using the Pillow (PIL) library.

🔧 Features

✔ Rotates images 90° clockwise

✔ Resizes images from 192x192 → 128x128

✔ Converts images from .tiff → .jpeg

✔ Processes multiple images in a batch

✔ Saves output files in /opt/icons/ directory

🚀 Installation & Setup

1️⃣ Install Dependencies
Make sure you have Python 3 installed. Then, install the required package:

pip3 install pillow

2️⃣ Clone the Repository

git clone https://github.com/YOUR-USERNAME/image-processing-python.git

cd image-processing-python

3️⃣ Run the Script

Execute the script to process images:

python3 process_images.py

📂 Directory Structure

/image-processing-python
│── process_images.py   # Main Python script
│── README.md           # Project documentation
└── images/             # Folder containing input images

🔗 How It Works
The script iterates through each image in the /images/ folder.

Applies transformations (rotate, resize, convert format).

Saves the modified images to /opt/icons/.

🛠️ Technologies Used

Python 3

Pillow (PIL) Library
