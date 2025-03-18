# BASE64-API

## Introduction

Welcome to the Base64 API Project! This project provides a simple API for encoding and decoding text using Base64 format. It is built using FastAPI.

## Project Structure

.gitignore README.md api/ └── v1/ ├── routes/ │ ├── init.py │ └── base64_routes.py └── schemas/ ├── base64_schemas.py └── response_model.py main.py requirements.txt

### Key Files and Directories

- **main.py**: Initializes the FastAPI application and sets up the root endpoint that returns a welcome message.
- **api/v1/routes/base64_routes.py**: Contains routes for encoding and decoding text to and from Base64 format.
  - `text_to_base64`: Converts text to Base64 encoding and returns a success response or error details.
  - `base64_to_text`: Converts Base64 encoding back to text and returns a success response or error details.
- **api/v1/schemas/**: Contains Pydantic models for request and response validation.

## Features

- **Encode Text**: Convert plain text to Base64 encoded format.
- **Decode Text**: Convert Base64 encoded text back to plain text.
- **FastAPI Integration**: Leverages FastAPI for quick and efficient API development.

## Installation

To set up the project locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:
   ```bash
   uvicorn main:app --reload
   ```