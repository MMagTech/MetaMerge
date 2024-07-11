import os
import json
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PIL import Image
import piexif

def embed_metadata(image_path, output_path, metadata):
    try:
        # Load the image
        image = Image.open(image_path)
        print(f"Opened image: {image_path}")

        # Prepare EXIF data
        try:
            exif_dict = piexif.load(image.info.get('exif', b''))
            print(f"Loaded EXIF data for: {image_path}")
        except Exception as exif_error:
            exif_dict = {"Exif": {}}
            print(f"No EXIF data found for {image_path}: {exif_error}")

        # Convert the metadata to JSON string
        metadata_str = json.dumps(metadata)

        # Embed metadata into EXIF user comment tag
        exif_dict['Exif'][piexif.ExifIFD.UserComment] = metadata_str.encode('utf-8')
        print(f"Embedded metadata into EXIF for: {image_path}")

        # Save the image with the new EXIF data
        exif_bytes = piexif.dump(exif_dict)
        output_image_path = os.path.join(output_path, os.path.relpath(image_path, input_folder))
        
        # Ensure the output directory exists
        output_dir = os.path.dirname(output_image_path)
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        image.save(output_image_path, exif=exif_bytes)
        print(f"Saved image to: {output_image_path}")
    except Exception as e:
        print(f"Error embedding metadata into {image_path}: {e}")

def process_images(input_folder, output_folder):
    print(f"Processing images from {input_folder} to {output_folder}")

    # Initialize the log file
    no_metadata_folder = os.path.join(output_folder, "No MetaData")
    log_file_path = os.path.join(no_metadata_folder, "missing_metadata_log.txt")
    if not os.path.exists(no_metadata_folder):
        os.makedirs(no_metadata_folder)

    with open(log_file_path, 'w') as log_file:
        log_file.write("Images without corresponding metadata JSON:\n\n")

    # Collect all image files
    image_files = []
    for dirpath, _, files in os.walk(input_folder):
        for filename in files:
            if filename.lower().endswith((".jpg", ".jpeg", ".png")):
                image_files.append(os.path.join(dirpath, filename))

    total_files = len(image_files)
    print(f"Total image files found: {total_files}")
    progress_bar['maximum'] = total_files

    for count, image_path in enumerate(image_files, start=1):
        print(f"Processing file {count}/{total_files}: {image_path}")
        json_path = image_path + ".json"
        if not os.path.exists(json_path):
            json_path = os.path.join(os.path.dirname(image_path), os.path.splitext(os.path.basename(image_path))[0] + ".jpg.json")
            print(f"Adjusted JSON path: {json_path}")

        if os.path.exists(json_path):
            print(f"Found corresponding JSON: {json_path}")
            with open(json_path, 'r') as json_file:
                metadata = json.load(json_file)
                print(f"Embedding metadata from {json_path} into {image_path}")
                embed_metadata(image_path, output_folder, metadata)
        else:
            print(f"Metadata file not found for {image_path}")
            with open(log_file_path, 'a') as log_file:
                log_file.write(f"{image_path}\n")

            # Copy image to No MetaData folder
            relative_path = os.path.relpath(image_path, input_folder)
            no_metadata_image_path = os.path.join(no_metadata_folder, relative_path)
            no_metadata_image_dir = os.path.dirname(no_metadata_image_path)
            if not os.path.exists(no_metadata_image_dir):
                os.makedirs(no_metadata_image_dir)
            shutil.copy2(image_path, no_metadata_image_path)

        # Update progress bar
        progress_bar['value'] = count
        root.update_idletasks()

    messagebox.showinfo("Process Completed", "Metadata has been embedded into all images. Check log for missing metadata.")

def select_input_folder():
    folder_path = filedialog.askdirectory()
    input_folder_path.set(folder_path)
    print(f"Selected input folder: {folder_path}")

def select_output_folder():
    folder_path = filedialog.askdirectory()
    output_folder_path.set(folder_path)
    print(f"Selected output folder: {folder_path}")

def start_processing():
    global input_folder  # Ensure input_folder is accessible in embed_metadata
    input_folder = input_folder_path.get()
    output_folder = output_folder_path.get()
    if not input_folder or not output_folder:
        messagebox.showerror("Error", "Please select both input and output folders.")
    else:
        print(f"Starting processing with input: {input_folder}, output: {output_folder}")
        process_images(input_folder, output_folder)

# Create the main window
root = tk.Tk()
root.title("Image Metadata Embedder")

input_folder_path = tk.StringVar()
output_folder_path = tk.StringVar()

# Create and place the widgets
tk.Label(root, text="Select Input Folder:").grid(row=0, column=0, padx=10, pady=10)
tk.Entry(root, textvariable=input_folder_path, width=50).grid(row=0, column=1, padx=10, pady=10)
tk.Button(root, text="Browse", command=select_input_folder).grid(row=0, column=2, padx=10, pady=10)

tk.Label(root, text="Select Output Folder:").grid(row=1, column=0, padx=10, pady=10)
tk.Entry(root, textvariable=output_folder_path, width=50).grid(row=1, column=1, padx=10, pady=10)
tk.Button(root, text="Browse", command=select_output_folder).grid(row=1, column=2, padx=10, pady=10)

tk.Button(root, text="Start Processing", command=start_processing).grid(row=2, column=0, columnspan=3, pady=10)

# Add progress bar
progress_bar = ttk.Progressbar(root, orient='horizontal', length=400, mode='determinate')
progress_bar.grid(row=3, column=0, columnspan=3, pady=20)

# Run the application
root.mainloop()
