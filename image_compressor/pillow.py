from PIL import Image
import os

def compress_images(input_dir, output_dir, quality=85):
    # Ensure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Iterate through all the files in the input directory
    for filename in os.listdir(input_dir):
        if filename.endswith(".jpg") or filename.endswith(".png"):  # Adjust extensions as needed
            file_path = os.path.join(input_dir, filename)
            img = Image.open(file_path)
            
            # Compress and save the image in the output directory
            output_path = os.path.join(output_dir, filename)
            img.save(output_path, optimize=True, quality=quality)
            print(f"Compressed and saved {filename}")

# Example usage
input_directory = "campus_pics\\12th_loc"
output_directory = "campus_pics\\12th_loc"
compress_images(input_directory, output_directory, quality=10)  # Adjust quality to control compression level
