# Hand Tracking and Mouse Control using OpenCV, MediaPipe, and PyAutoGUI

This project allows you to control your mouse cursor using hand gestures captured by a webcam. It utilizes OpenCV for video capture and processing, MediaPipe for hand landmark detection, and PyAutoGUI for controlling the mouse cursor.

## Features

- Hand tracking using MediaPipe.
- Mouse cursor control by moving your forefinger within a defined trackpad area.
- Mouse click action when forefinger and middle finger are close together.

## Requirements

- Python 3.x
- OpenCV
- MediaPipe
- PyAutoGUI

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/NishanthSamson/MediaPipe-Air-Mouse
    cd MediaPipe-Air-Mouse
    ```

2. Install the required Python packages:

    ```bash
    pip install opencv-python mediapipe pyautogui
    ```

## Usage

1. Run the script:

    ```bash
    python AirMouse.py
    ```

2. Ensure your webcam is working. The script will open a window displaying the webcam feed with the hand tracking overlay.

3. Move your forefinger within the defined trackpad area to control the mouse cursor. Bring your forefinger and middle finger close together to perform a click action.
