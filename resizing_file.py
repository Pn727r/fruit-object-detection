import os
import cv2

def resize_images_in_place(folder_path, new_width=128, new_height=128):
    # Loop through each file in the folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        
        # Check if the file is an image (by extension)
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff')):
            # Read the image using OpenCV
            img = cv2.imread(file_path)
            
            if img is not None:  # Check if image loading was successful
                # Resize the image
                resized_img = cv2.resize(img, (new_width, new_height))
                
                # Save the resized image with the same filename, overwriting it
                cv2.imwrite(file_path, resized_img)
                
    print("All images resized to 128x128 and saved in place.")

folder_path = 'C:/Users/LENOVO/Desktop/fruit object detection/val/images/' 
resize_images_in_place(folder_path, new_width=128, new_height=128)
