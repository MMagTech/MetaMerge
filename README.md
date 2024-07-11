# Image Metadata Embedder

A Python-based application to embed JSON metadata into image files. The application supports recursive directory traversal, logging, and a progress bar to track the embedding process.

## Features

- Embed JSON metadata into the EXIF data of image files.
- Supports JPEG and PNG image formats.
- Recursively processes images in subdirectories.
- Progress bar to track the processing of images.
- Logs images that do not have corresponding metadata JSON files.

## Requirements

- Python 3.x (if running the script directly)
- Required Python packages: `Pillow`, `piexif`, `tkinter` (if running the script directly)

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

### Running the Script Directly

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

### Using the Pre-compiled Executable

If you are not familiar with Python, you can use the included `MetaMerge.exe` executable:

1. **Download the executable:**

    - Locate the `MetaMerge.exe` file in the `dist` folder or download it from the repository's releases page.

2. **Run the executable:**

    - Double-click on `MetaMerge.exe` to launch the application.

3. **Follow the same steps as above** to select the input and output folders, start processing, and check the log.

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

## Handling Photos Without a JSON Metadata File

- Photos without corresponding JSON metadata files are not modified or saved in the output folder.
- These photos' paths are logged in a file named `missing_metadata_log.txt` located in the output folder.

## Compiling to an Executable

To compile the Python script into a standalone executable on Windows, follow these steps:

1. **Install PyInstaller:**

    Open a command prompt and install PyInstaller using pip:
    ```sh
    pip install pyinstaller
    ```

2. **Navigate to Your Script's Directory:**

    Use the `cd` command to navigate to the directory where your `metamerge.py` script is located. For example:
    ```sh
    cd path\to\your\script
    ```

3. **Create the Executable:**

    Run PyInstaller with the `--onefile`, `--windowed`, and `--name` options to create a single executable named `metamerge` without a console window:
    ```sh
    pyinstaller --onefile --windowed --name metamerge metamerge.py
    ```

4. **Locate the Executable:**

    After PyInstaller completes, you will find the executable named `metamerge.exe` in the `dist` folder inside your project directory. The path will be something like:
    ```
    path\to\your\script\dist\metamerge.exe
    ```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
