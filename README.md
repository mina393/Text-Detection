# Text Detection with OpenCV and EasyOCR

This project demonstrates text detection and recognition in images using OpenCV and EasyOCR. The script reads an image file, detects any text present, and displays the image with bounding boxes around detected text along with the recognized text.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Code Explanation](#code-explanation)
- [Future Improvements](#future-improvements)

## Overview

The project utilizes EasyOCR for optical character recognition (OCR) and OpenCV for image processing. It identifies text in an image, draws bounding boxes around the detected text, and displays the recognized text on the image.

## Features

- **Text detection**: Identifies and extracts text from images.
- **Bounding boxes**: Draws rectangles around detected text for easy visualization.
- **Text recognition**: Displays the recognized text directly on the image.
- **Confidence score filtering**: Allows filtering of detected text based on a confidence score threshold.

## Requirements

- Python 3.x
- OpenCV (`cv2`)
- Matplotlib (`matplotlib`)
- EasyOCR

You can install the required packages by running:
```bash
pip install opencv-python matplotlib easyocr
```

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/text-detection-opencv.git
   ```
   
2. **Navigate to the project directory**:
   ```bash
   cd text-detection-opencv
   ```
   
3. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Modify the image path** in the script to point to your image file:
   ```python
   image_path = r"path_to_your_image.png"
   ```

2. **Run the main Python script**:
   ```bash
   python main.py
   ```
   
3. The processed image will be displayed with bounding boxes around detected text and the recognized text shown on the image.

## Code Explanation

- The script begins by importing necessary libraries: OpenCV for image processing, Matplotlib for displaying images, and EasyOCR for text detection and recognition.
- It specifies the path to the image file and reads the image using OpenCV.
- An instance of EasyOCR's `Reader` is created to support English text detection using CPU processing.
- The text is detected in the image using EasyOCR's `readtext()` method.
- A confidence score threshold is set to filter out less reliable detections.
- For each detected text item, the script draws a bounding box around the text and overlays the recognized text if its confidence score exceeds the threshold.
- Finally, the image is converted to RGB format for display with Matplotlib and shown to the user.

## Future Improvements

- **Multi-language support**: Expand text detection to support multiple languages.
- **Text extraction to file**: Save recognized text to a text file for further processing.
- **Enhanced visualization**: Improve the display of results with additional information or formatting.