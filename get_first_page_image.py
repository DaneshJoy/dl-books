import os
import fitz  # PyMuPDF

# Open the PDF file
pdf_path = input("Please enter the full path of the PDF file: ")
pdf_document = fitz.open(pdf_path)

# Get the first page
first_page = pdf_document.load_page(0)  # Pages are zero-indexed

# Render the first page as a PNG image
pix = first_page.get_pixmap()

# Save the image
pdf_dir = os.path.dirname(pdf_path)
pdf_name = os.path.splitext(os.path.basename(pdf_path))[0]
img_name = f"{pdf_name}.jpg"
image_path = os.path.join(pdf_dir, img_name)
pix.save(image_path)

print(f"First page saved as: {img_name}")
