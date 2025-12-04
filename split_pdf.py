import argparse
import os
from src.splitter import PdfSplitter

def main():
    parser = argparse.ArgumentParser(description="Split PDF into chunks")
    parser.add_argument("input_pdf", help="Path to the input PDF file")
    parser.add_argument("--chunk-size", type=int, required=True, help="Number of pages per split file")
    parser.add_argument("--output-dir", help="Directory to save split files (optional)")
    
    args = parser.parse_args()
    
    splitter = PdfSplitter()
    
    try:
        splitter.split_pdf(args.input_pdf, args.chunk_size, args.output_dir)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
