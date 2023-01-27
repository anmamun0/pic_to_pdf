from PIL import Image
import os

# List of JPG files to be converted
jpg_files = ["image1.jpg", "image2.jpg", "image3.jpg","image4.jpg"]

# Create a new PDF file with PIL
pdf_file = Image.open(jpg_files[0])
pdf_file.save("images.pdf", save_all=True, append_images=[Image.open(jpg) for jpg in jpg_files[1:]])

# Print confirmation
print("Images converted to PDF and saved as 'images.pdf'.")

