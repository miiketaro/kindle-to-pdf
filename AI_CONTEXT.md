# AI Context for Kindle to PDF Converter

## Project Overview
This project is a tool to capture Kindle for PC books and convert them into PDF files. It works by automating page turns and taking screenshots, then stitching them into a PDF.

## Architecture
The project consists of three main components:
1.  **`main.py`**: The entry point of the application. It handles argument parsing and orchestrates the capture and conversion process.
2.  **`src/capturer.py`**: Handles the interaction with the Kindle for PC application. It automates page turning and screen capturing using `pyautogui`.
3.  **`src/converter.py`**: Handles the conversion of captured screenshots into a single PDF file using `img2pdf`.
4.  **`src/splitter.py`**: (Likely) A utility to split PDFs, though not directly used in the main flow currently.

## Usage
### Prerequisites
-   Windows OS
-   Python installed
-   Kindle for PC installed

### Installation
```powershell
pip install pyautogui img2pdf
```

### Running the Converter
```powershell
python main.py --output my_book.pdf
```
Options:
-   `--output`: Output PDF filename (default: `output.pdf`)
-   `--temp-dir`: Temporary directory for screenshots (default: `screenshots`)
-   `--pages`: Number of pages to capture (optional)
-   `--direction`: Page direction ('ltr' or 'rtl')
-   `--max-size`: Maximum size of generated PDF (default: 180MB)

## Directory Structure
-   `main.py`: Main script.
-   `src/`: Source code directory.
    -   `capturer.py`: Screen capture logic.
    -   `converter.py`: Image to PDF conversion logic.
    -   `splitter.py`: PDF splitting logic.
-   `screenshots/`: Default directory for temporary screenshots (gitignored).
-   `output/`: Default directory for output files (gitignored).
-   `requirements.txt`: Python dependencies.
-   `README.md`: User documentation.
-   `AI_CONTEXT.md`: This file.
