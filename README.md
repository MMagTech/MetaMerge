# Image Metadata Embedder

A Python-based application to embed JSON metadata into image files. As recieved from Google Takeout. The application supports recursive directory traversal, logging, and a progress bar to track the embedding process.

## Features

- Embed JSON metadata into the EXIF data of image files.
- Supports JPEG and PNG image formats.
- Recursively processes images in subdirectories.
- Progress bar to track the processing of images.
- Logs images that do not have corresponding metadata JSON files into the output folder.

## Requirements

- Python 3.x
- Required Python packages: `Pillow`, `piexif`, `tkinter`

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/yourusername/imagemetadataembedder.git
    cd imagemetadataembedder
    ```

2. **Install the required packages:**

    ```sh
    pip install pillow piexif
    ```

## Usage

1. **Run the script:**

    ```sh
    python metamerge.py
    ```

2. **Use the GUI to select the input and output folders:**

    - **Input Folder:** The folder containing the images and their corresponding JSON metadata files.
    - **Output Folder:** The folder where the processed images will be saved.

3. **Start Processing:**

    - Click on the "Start Processing" button to begin embedding metadata into the images.

4. **Check the Log:**

    - After processing, a log file named `missing_metadata_log.txt` will be created in the output folder. This log file contains the list of images that did not have corresponding metadata JSON files.

## JSON Metadata Format

The JSON metadata file should have the same base name as the image file. For example, for an image named `example.jpg`, the metadata file should be named `example.jpg.json` or `example.json`.

## Example

Given the following directory structure:

input_folder/
├── subfolder1/
│ ├── image1.jpg
│ ├── image1.jpg.json
│ └── image2.png
│ └── image2.png.json
├── subfolder2/
│ ├── image3.jpg
│ └── image3.jpg.json
└── image4.jpg
└── image4.json


The script will embed the metadata from `image1.jpg.json`, `image2.png.json`, `image3.jpg.json`, and `image4.json` into their corresponding images.

## Optional 
Use the included MetaMerge.exe on Windows if you are not familiar with python. Just download it and run.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


