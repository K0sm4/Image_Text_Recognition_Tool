# Image Text Recognition Tool

This is a simple Python script that allows you to extract text from images using Optical Character Recognition (OCR). The script utilizes the OpenCV, pytesseract, and Pillow libraries to perform the image processing and text recognition tasks.
 
## Prerequisites

Before running the script, make sure you have the following libraries installed:

OpenCV (cv2)

pytesseract

Pillow (PIL)

You can install these libraries using the following commands:

```bash
pip install opencv-python-headless pytesseract Pillow

```

## Usage

1. Run the script by executing the following command:
```bash
python script.py
```
2. The script will present you with two options:

- Load image from clipboard (Option 1): If you choose this option, the script will attempt to retrieve an image from your clipboard. If an image is found, it will be saved as "lastss.png", and its text content will be recognized using OCR.
- Enter custom image path (Option 2): If you choose this option, you will need to provide the path to the image you want to analyze. The script will then process the image and extract text using OCR.

3. After processing the image, the recognized text will be displayed on the console.

## How It Works

1. The script loads the selected image using the OpenCV library (cv2.imread() function).

2. If the image is successfully loaded, its colors are converted to shades of gray using OpenCV (cv2.cvtColor() function). This step is essential for optimal text recognition.

3. The OCR process is performed using the pytesseract.image_to_string() function from the pytesseract library. This function extracts text from the gray-scale image.

4. The recognized text is then returned by the recognize_text_from_image() function.

5. Depending on the user's choice, the script either captures an image from the clipboard using Pillow's ImageGrab.grabclipboard() function (Option 1), or it prompts the user to provide a custom image path (Option 2).

6. The recognized text is printed to the console.

## Note

- If you choose Option 1 and there's no image in your clipboard, the script will inform you that no image was found.

- The script uses a default filename ("lastss.png") to save the image when capturing from the clipboard. You can modify this behavior by editing the script.

- This script is meant for basic text recognition tasks. The accuracy of OCR can vary depending on factors like image quality, font, and background.

- The pytesseract library requires an installation of Tesseract OCR on your system. Make sure Tesseract is installed and its executable is in your system's PATH.

## Disclaimer
This script was created for educational purposes and basic text recognition needs. It may not provide accurate results for complex images or specific fonts. Always review the recognized text for accuracy and perform additional processing if required.

### examples
input:

![Configuration](https://cdn.discordapp.com/attachments/1135466860003995699/1138588736708423820/tkp.png)

output:

![Configuration](https://cdn.discordapp.com/attachments/1135466860003995699/1138590030596685965/out.png)
