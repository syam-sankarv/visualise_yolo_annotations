# YOLO Polygon Annotation Visualizer

## Overview

This project provides a Python script to visualize YOLO polygon annotations on images. The YOLO polygon annotations are expected to be stored in text files with normalized coordinates (values between 0 and 1) relative to the image dimensions. Each annotation file corresponds to an image file and contains one or more polygons, where each polygon is represented by a class ID followed by pairs of normalized x, y coordinates for its vertices.

The script reads images and their corresponding annotation files, converts normalized polygon points into pixel coordinates, draws the polygons on the images, and displays the result for easy visual verification.

---

## Features

- Supports polygon annotations of arbitrary number of vertices.
- Reads annotations in YOLO format with normalized coordinates.
- Visualizes polygons with class labels directly on the image.
- Handles multiple images and annotations in bulk from specified directories.
- Accepts input paths via command line arguments for flexibility.

---

## Installation and Dependencies

Make sure you have Python 3.x installed. You will need the following Python packages:

- `opencv-python` (for image processing and drawing)
- `matplotlib` (for displaying images)
- `numpy` (for numerical operations)
- `argparse` (for parsing command line arguments)

You can install the required packages using pip:

pip install opencv-python matplotlib numpy
