from fastapi import FastAPI, UploadFile, File, HTTPException
import os
import shutil

from services.ocr_service import (
    extract_text_from_image,
    extract_text_from_pdf
)

from services.classifier_service import classify_document
from services.signature_service import detect_signature

app = FastAPI(title="Mini Document AI")

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.get("/")
def home():
    return {
        "message": "Mini Document AI Running"
    }


@app.post("/analyze")
async def analyze(file: UploadFile = File(...)):

    file_path = os.path.join(
        UPLOAD_FOLDER,
        file.filename
    )

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    try:

        if file.filename.lower().endswith(".pdf"):

            text = extract_text_from_pdf(file_path)

            document_type = classify_document(text)

            signature_found = False

        elif file.filename.lower().endswith(
            (".png", ".jpg", ".jpeg")
        ):

            text = extract_text_from_image(file_path)

            document_type = classify_document(text)

            signature_found = detect_signature(file_path)

        else:
            raise HTTPException(
                status_code=400,
                detail="Only PDF, PNG, JPG, JPEG supported"
            )

        return {
            "filename": file.filename,
            "document_type": document_type,
            "signature_found": signature_found,
            "text": text
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )