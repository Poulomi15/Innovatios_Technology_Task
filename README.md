# Innovatios_Technology_Task

Write code in Python3 using lib: PyQt & OpenCV to display live camera video feed from your webcam/ipcam/local video file on GUI: main.ui
Start Button: to start video feed display
Stop Button: to stop video feed display.

# Video Display App

## Overview
This project is a simple Python application that uses PyQt5 for the GUI and OpenCV for displaying a live camera video feed. The application allows users to start and stop the video feed using buttons.

## Requirements
- Python 3.x
- PyQt5
- OpenCV

## Installation
1. Install the required Python packages:
    ```bash
    pip install PyQt5
    pip install opencv-python
    ```

2. Save the provided Python code in a file (e.g., `main.py`).

3. Create a UI file (e.g., `main.ui`) using a tool like Qt Designer, ensuring it has a QLabel for video display and buttons for starting and stopping the video feed.

## Running the Application
1. Open a terminal or command prompt.

2. Navigate to the directory where the Python script is saved.

3. Run the script:
    ```bash
    python main.py
    ```

4. The GUI window should appear with "Start" and "Stop" buttons. Click "Start" to initiate the video feed.

## Notes
- Adjust the camera index or video file path in the `cv2.VideoCapture` constructor in the code if needed.
- Make sure the UI file path in the `loadUi` function corresponds to the actual path of your UI file.

## Author
Poulomi Chowdhury 

Feel free to contact me if you have any questions or need further assistance!
