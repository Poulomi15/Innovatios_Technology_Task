import sys
import cv2
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
from main_ui import Ui_MainWindow

class VideoDisplayApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # Load the GUI layout from the .ui file
        loadUi('main.ui', self)

        # Initialize variables
        self.cap = None
        self.timer = QTimer(self)

        # Connect buttons to functions
        self.startButton.clicked.connect(self.start_video_feed)
        self.stopButton.clicked.connect(self.stop_video_feed)

    def start_video_feed(self):
        if not self.cap or not self.cap.isOpened():
            # Open the default camera (you can change the index for a different camera)
            self.cap = cv2.VideoCapture(0)

            # Set the timer timeout (ms) to update the video feed
            self.timer.timeout.connect(self.update_video_feed)
            self.timer.start(30)  # You can adjust the time interval as needed

    def stop_video_feed(self):
        if self.cap and self.cap.isOpened():
            self.timer.stop()
            self.cap.release()
            self.videoLabel.clear()

    def update_video_feed(self):
        ret, frame = self.cap.read()
        if ret:
            # Convert OpenCV BGR image to RGB
            rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Convert to QImage
            h, w, ch = rgb_image.shape
            bytes_per_line = ch * w
            q_image = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)

            # Convert to QPixmap and set it to the QLabel
            pixmap = QPixmap.fromImage(q_image)
            self.videoLabel.setPixmap(pixmap)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = VideoDisplayApp()
    window.show()
    sys.exit(app.exec_())
