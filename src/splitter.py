import os
from pypdf import PdfReader, PdfWriter

class PdfSplitter:
    def split_pdf(self, input_path, chunk_size, output_dir=None):
        """
        Splits a PDF file into chunks of specified size.
        
        Args:
            input_path (str): Path to the input PDF file.
            chunk_size (int): Number of pages per split file.
            output_dir (str, optional): Directory to save split files. Defaults to input file's directory.
        """
        if not os.path.exists(input_path):
            raise FileNotFoundError(f"Input file not found: {input_path}")
            
        if output_dir is None:
            output_dir = os.path.dirname(input_path)
            
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
            
        reader = PdfReader(input_path)
        total_pages = len(reader.pages)
        
        base_name = os.path.splitext(os.path.basename(input_path))[0]
        
        print(f"Splitting {input_path} ({total_pages} pages) into chunks of {chunk_size} pages...")
        
        for i in range(0, total_pages, chunk_size):
            writer = PdfWriter()
            end_page = min(i + chunk_size, total_pages)
            
            for page_num in range(i, end_page):
                writer.add_page(reader.pages[page_num])
                
            output_filename = f"{base_name}_part_{i // chunk_size + 1}.pdf"
            output_path = os.path.join(output_dir, output_filename)
            
            with open(output_path, "wb") as f:
                writer.write(f)
                
            print(f"Created {output_filename} (pages {i+1}-{end_page})")
            
        print("Splitting complete.")
