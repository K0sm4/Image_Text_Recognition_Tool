import cv2
import pytesseract
from PIL import ImageGrab

def recognize_text_from_image(image_path):
    # Upload a photo using cv2
    image = cv2.imread(image_path)

    # Photo upload test
    if image is None:
        print("Error: Unable to load image.")
        return ""

    # Convert colors to shades of gray using cv2
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Recognize using OCR
    recognized_text = pytesseract.image_to_string(gray_image)

    return recognized_text

def main():
    print("1. Load image from clipboard")
    print("2. Enter custom image path")
    choice = input("Enter your choice (1/2): ")

    if choice == "1":
        image = ImageGrab.grabclipboard()
        if image:
            image.save("last_screenshot.png", "PNG")
            recognized_text = recognize_text_from_image("last_screenshot.png")
            print("Recognized Text:")
            print(recognized_text)
        else:
            print("No image found in clipboard.")
    elif choice == "2":
        image_path = input("Enter the image path: ")
        recognized_text = recognize_text_from_image(image_path)
        print("Recognized Text:")
        print(recognized_text)
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
