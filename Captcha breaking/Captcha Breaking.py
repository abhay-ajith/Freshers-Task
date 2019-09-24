from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
txt = pytesseract.image_to_string(Image.open('download.png'))
x = eval(txt)
print(x)
