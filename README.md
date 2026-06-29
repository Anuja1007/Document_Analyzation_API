# AI-Powered Signature Verification API

A FastAPI-based REST API for verifying handwritten signatures using image processing techniques.

## 🚀 Features

- Upload reference and test signatures
- Image preprocessing with OpenCV
- Signature similarity comparison using SSIM
- RESTful API endpoints
- Interactive Swagger API documentation
- JSON responses

## 🛠️ Tech Stack

- Python
- FastAPI
- OpenCV
- Scikit-image
- Uvicorn

## 📂 Project Structure

```
signature-api/
│── app.py
│── signature_model.py
│── uploads/
│── requirements.txt
│── README.md
```

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/<your-username>/<repo-name>.git
```

Move into the project directory:

```bash
cd <repo-name>
```

Create and activate a virtual environment:

```bash
python -m venv venv

# Windows
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
uvicorn app:app --reload
```

## 📖 API Documentation

After starting the server, visit:

```
http://127.0.0.1:8000/docs
```

## 📌 Sample Response

```json
{
    "similarity_score": 89.34,
    "match": true
}
```

## 👩‍💻 Author

Anuja Pandey