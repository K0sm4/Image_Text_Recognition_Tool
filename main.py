import cv2
import pytesseract
from PIL import ImageGrab

image = ImageGrab.grabclipboard()
image.save("dupa.png", "PNG")
def recognize_text_from_image(image_path):
    # wczytanie fotki za pomocą cv2
    image = cv2.imread(image_path)

    # test poprawnego wczytania zdjęcia
    if image is None:
        print("Błąd: Nie można wczytać obrazu.")
        return ""

    # za pomocą cv2 zamieniamy kolory na odcienie szarośći
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Rozpoznajemy text za pomocą Tesseract OCR
    recognized_text = pytesseract.image_to_string(gray_image)

    return recognized_text


image_path = 'dupa.png'
recognized_text = recognize_text_from_image(image_path)
print(recognized_text)
