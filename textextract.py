from PIL import Image
import pytesseract
import re

def extract_text_from_image(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    print(text)
    
    # Mencari ID QRIS
    id_match = re.search(r'ID(\d+)', text)

    if not id_match or len(id_match.group(1)) != 15:
        #search for ID with different format starting with I or i or 1
        id_match = re.search(r'1D(\d+)', text)

    id_text = "ID" + id_match.group(1) if id_match else ''
    
    return [id_text]
