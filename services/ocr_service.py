import easyocr
import fitz
import os

# Initialize OCR once
reader = easyocr.Reader(['en'])


def extract_text_from_image(image_path):
    """
    Extract text from image using EasyOCR
    """

    result = reader.readtext(image_path)

    extracted_text = " ".join(
        [item[1] for item in result]
    )

    return extracted_text


def extract_text_from_pdf(pdf_path):
    """
    Convert PDF pages to images
    and run OCR on each page
    """

    doc = fitz.open(pdf_path)

    extracted_text = ""

    os.makedirs("temp", exist_ok=True)

    for page_num in range(len(doc)):

        page = doc[page_num]

        pix = page.get_pixmap(
            matrix=fitz.Matrix(2, 2)
        )

        temp_image = f"temp/page_{page_num}.png"

        pix.save(temp_image)

        result = reader.readtext(temp_image)

        page_text = " ".join(
            [item[1] for item in result]
        )

        extracted_text += page_text + "\n"

        if os.path.exists(temp_image):
            os.remove(temp_image)

    doc.close()

    return extracted_text