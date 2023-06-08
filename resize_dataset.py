from PIL import Image
import os
import shutil

# Path to the directory containing the images
source_directory = "./raw-img"

# Path to the directory where the resized images will be saved
destination_directory = "./resized-images"

# Desired width and height for the resized images
new_width = 40
new_height = 40

# Recursively iterate over each file and folder in the source directory
for root, dirs, files in os.walk(source_directory):
    for category in dirs:
        source_category_path = os.path.join(root, category)
        destination_category_path = os.path.join(destination_directory, os.path.relpath(source_category_path, source_directory))

        # Create the corresponding subfolders in the destination directory
        os.makedirs(destination_category_path, exist_ok=True)

    for filename in files:
        if filename.endswith((".jpg", ".png", ".jpeg")):
            # Open the image file
            source_image_path = os.path.join(root, filename)
            image = Image.open(source_image_path)

            # Resize the image
            resized_image = image.resize((new_width, new_height))

            # Save the resized image in the destination directory
            destination_image_path = os.path.join(destination_directory, os.path.relpath(source_image_path, source_directory))
            os.makedirs(os.path.dirname(destination_image_path), exist_ok=True)
            resized_image.save(destination_image_path)

# Copy non-image files from the source directory to the destination directory
shutil.copytree(source_directory, destination_directory, dirs_exist_ok=True, ignore=shutil.ignore_patterns("*.jpg", "*.png", "*.jpeg"))
