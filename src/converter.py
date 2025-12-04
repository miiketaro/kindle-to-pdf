import img2pdf
import os
import glob

class PdfConverter:
    def convert_images_to_pdf(self, image_dir, output_filename, max_size_bytes=None):
        """Converts all images in a directory to a single PDF or multiple PDFs if size limit is exceeded."""
        print(f"Converting images in {image_dir} to {output_filename}...")
        
        # Get all PNG files, sorted by name (page_0001.png, etc.)
        images = sorted(glob.glob(os.path.join(image_dir, "*.png")))
        
        if not images:
            print("No images found to convert.")
            return

        if max_size_bytes is None:
            # No limit, just convert all
            try:
                with open(output_filename, "wb") as f:
                    f.write(img2pdf.convert(images))
                print(f"Successfully created {output_filename}")
            except Exception as e:
                print(f"Error creating PDF: {e}")
            return

        # Split by size
        current_batch = []
        current_size = 0
        part_num = 1
        
        base_name, ext = os.path.splitext(output_filename)
        
        for img_path in images:
            img_size = os.path.getsize(img_path)
            
            # Estimate PDF overhead (very rough, but safe enough)
            # img2pdf wraps the image, so size is roughly image size + overhead.
            # We'll use a conservative estimate or just sum image sizes.
            # Let's just sum image sizes for now as a proxy.
            
            if current_batch and (current_size + img_size > max_size_bytes):
                # Write current batch
                self._write_batch(current_batch, f"{base_name}_part_{part_num}{ext}")
                part_num += 1
                current_batch = []
                current_size = 0
            
            current_batch.append(img_path)
            current_size += img_size
            
        if current_batch:
            self._write_batch(current_batch, f"{base_name}_part_{part_num}{ext}")

    def _write_batch(self, images, output_filename):
        try:
            with open(output_filename, "wb") as f:
                f.write(img2pdf.convert(images))
            print(f"Successfully created {output_filename}")
        except Exception as e:
            print(f"Error creating PDF part {output_filename}: {e}")
