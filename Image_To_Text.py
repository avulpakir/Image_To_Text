import os
from PIL import Image
import pytesseract

# Specify the path where your images are stored
image_folder = '/home/pc/Desktop/Images'
output_folder = '/home/pc/Desktop/Images1'

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Iterate over each image file in the specified folder
for file_name in os.listdir('/home/pc/Desktop/Images'):
    if file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp')):
        # Full path of the image
        image_path = os.path.join(image_folder, file_name)
        
        # Open image using Pillow
        image = Image.open(image_path)
        
        # Use pytesseract to do OCR on the image
        text = pytesseract.image_to_string(image)

        # Define the output text file name
        output_file_name = os.path.splitext(file_name)[0] + '.txt'
        output_file_path = os.path.join(output_folder, output_file_name)

        # Save the text to a .txt file
        with open(output_file_path, 'w', encoding='utf-8') as text_file:
            text_file.write(text)

        print(f'Saved {output_file_name} with extracted text.')

print('Text extraction completed.')
