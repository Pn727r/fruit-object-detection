import os
import shutil

def move_txt_files(source_folder, destination_folder):
    if not os.path.exists(source_folder):
        print(f"Source folder '{source_folder}' does not exist.")
        return
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
        print(f"Created destination folder '{destination_folder}'.")

    for filename in os.listdir(source_folder):
        if filename.endswith(".txt"):
            source_path = os.path.join(source_folder, filename)
            destination_path = os.path.join(destination_folder, filename)
            
            shutil.move(source_path, destination_path)
            print(f"Moved '{filename}' to '{destination_folder}'.")

# Usage example
source_folder = f"C:/Users/LENOVO/Desktop/fruit object detection/tomato/"  
destination_folder = "C:/Users/LENOVO/Desktop/fruit object detection/lbl/"  

move_txt_files(source_folder, destination_folder)
