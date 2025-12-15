import argparse
import os
import sys
from src.capturer import KindleCapturer
from src.converter import PdfConverter

def parse_size(size_str):
    """Parses a size string like '1.8MB' into bytes."""
    size_str = size_str.upper()
    units = {"KB": 1024, "MB": 1024**2, "GB": 1024**3}
    for unit, factor in units.items():
        if size_str.endswith(unit):
            try:
                return int(float(size_str[:-len(unit)]) * factor)
            except ValueError:
                pass
    try:
        return int(size_str)
    except ValueError:
        return None

def main():
    parser = argparse.ArgumentParser(description="Kindle for PC to PDF Converter")
    parser.add_argument("--output", default="output.pdf", help="Output PDF filename")
    parser.add_argument("--temp-dir", default="screenshots", help="Temporary directory for screenshots")
    parser.add_argument("--pages", type=int, help="Number of pages to capture (optional, default: infinite until Ctrl+C)")
    parser.add_argument("--direction", choices=['ltr', 'rtl'], default='ltr', help="Page direction: 'ltr' (Left-to-Right) or 'rtl' (Right-to-Left)")
    parser.add_argument("--max-size", default="180MB", help="Maximum size of generated PDF (e.g., '1.8MB', '100KB'). Default: 180MB")
    
    args = parser.parse_args()
    
    capturer = KindleCapturer(direction=args.direction)
    converter = PdfConverter()
    
    print("=== Kindle for PC to PDF Converter ===")
    print("1. Open Kindle for PC and open your book.")
    print("2. Enter Full Screen mode (usually F11).")
    print("3. Make sure the mouse cursor is hidden or out of the way.")
    print("4. This script will start capturing in 5 seconds after you press Enter.")
    
    input("Press Enter to start the countdown...")
    
    try:
        capturer.wait_for_focus(5)
        capturer.capture_loop(args.temp_dir, args.pages)
        
        # Convert to PDF　f
        max_size_bytes = parse_size(args.max_size) if args.max_size else None
        converter.convert_images_to_pdf(args.temp_dir, args.output, max_size_bytes)
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
