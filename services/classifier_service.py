def classify_document(text):
    """
    Classify document based on extracted OCR text
    """

    text = text.lower()

    # Resume
    if any(keyword in text for keyword in [
        "skills",
        "education",
        "experience",
        "projects",
        "certifications",
        "internship"
    ]):
        return "Resume"

    # Invoice
    elif any(keyword in text for keyword in [
        "invoice",
        "invoice number",
        "gst",
        "tax invoice",
        "total amount"
    ]):
        return "Invoice"

    # Aadhaar
    elif any(keyword in text for keyword in [
        "aadhaar",
        "government of india",
        "unique identification authority"
    ]):
        return "Aadhaar Card"

    # PAN
    elif any(keyword in text for keyword in [
        "income tax department",
        "permanent account number"
    ]):
        return "PAN Card"

    # Bank Statement
    elif any(keyword in text for keyword in [
        "account number",
        "opening balance",
        "closing balance",
        "transaction"
    ]):
        return "Bank Statement"

    return "Unknown"