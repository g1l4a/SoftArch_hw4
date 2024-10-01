# Software Architecture - Team 16 - Homework 4

# Video Filter Processing Application

## Overview

This application captures video from webcam in real-time and applies image processing filters to the video frames. It utilizes Python's OpenCV library for video capture and processing.

### Features

- **Real-Time Video Processing**: Capture live video feed from the webcam.
- **Filters**: Apply various filters to the video stream:
  - **Mirror Filter**: Flip the video frame horizontally.
  - **Black and White Filter**: Convert the video frame to grayscale.
  - **Resize Filter**: Change the dimensions of the video frame to a specified size (default resizing is 640x480).
  - **Rotate 180 Filter**: Rotate the video frame by 180 degrees.

## Prerequisites

To run this application, you need to have the following installed on your machine:

- **Python 3.8.x+**: Make sure you have Python installed. You can download it from [python.org](https://www.python.org/downloads/).
  ```bash
  pip install -r requirements.txt
  ```

## Getting Started

### Cloning the Repository

1. Clone this repository to your local machine using:
   ```bash
   git clone https://github.com/g1l4a/SoftArch_hw4.git
   cd SoftArch_hw4
   ```

### Running the Application

2. Ensure your webcam is connected and accessible by your computer.
3. Run the application:

   ```bash
   python main.py
   ```

4. The application will open two windows:

   - **Original Video**: Displays the live video feed from your webcam.
   - **Output**: Displays the processed video frame with the applied filters.

5. To exit the application, simply press the Ctrl + C.

## Code Explanation

### Key Components

- **Filter Classes**: The application defines several filter classes (`MirrorFilter`, `BlackAndWhiteFilter`, `ResizeFilter`, `Rotate180Filter`) in the `processing` module. Each class has an `apply` method that takes a video frame as input and processes it.

- **Multiprocessing**: The application uses the `multiprocessing` module to run filters in separate processes.

### Code Structure

- **apply_filter_process(filter_class, queue)**: A function that runs in a separate process to apply the specified filter on frames retrieved from the input queue.

- **main()**: The main function that handles video capture, initiates filter processes, and manages the flow of frames between processes.
