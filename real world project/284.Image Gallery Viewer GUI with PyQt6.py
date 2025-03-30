'''
Project Description
    In this project, we will build a simple image gallery viewer where users can browse through images stored in a folder. 
    The app will allow the user to select a folder from their computer and display the images of that folder:
    This project is useful for building a GUI application using one of the best GUI libraries such as PyQt6, and 
    it introduces users to managing file systems, working with images, and handling GUI events.

Learning Benefits
    Learn how to create a basic PyQt6 GUI with interactive elements.
    Implement image navigation and display logic.
    Practice handling user input (button clicks, list selections).

Prerequisites
    Required Libraries:PyQt6
                        pip install PyQt6

'''

import sys
import os
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QListWidget, QListWidgetItem, QFileDialog
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtCore import QSize, Qt

class ImageGallery(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Image Gallery Viewer")
        self.setGeometry(300, 200, 800, 600)

        lable=QLabel("images",self)
        lable.setGeometry(10,10,130,30)

        self.image_label = QLabel(self)
        self.image_label.setGeometry(200, 20, 400, 250)

        self.prev_button = QPushButton("Previous", self)
        self.prev_button.setGeometry(50, 450, 150, 40)
        self.prev_button.clicked.connect(self.prev_image)

        self.next_button = QPushButton("Next", self)
        self.next_button.setGeometry(600, 450, 150, 40)
        self.next_button.clicked.connect(self.next_image)

        select = QPushButton("Select Folder", self)
        select.setGeometry(250, 450, 300, 40)
        select.clicked.connect(self.folder)

    def folder(self):
        self.folder_path = QFileDialog.getExistingDirectory(self, "Select Folder")

        if self.folder_path:
            self.image_files = [f for f in os.listdir(self.folder_path) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
            self.image_files.sort()

            if self.image_files:
                for img in self.image_files:
                    img_path = os.path.join(self.folder_path, img)
                    pixmap = QPixmap(img_path).scaled(100, 100, Qt.AspectRatioMode.KeepAspectRatio)  # Thumbnail
                    item = QListWidgetItem(QIcon(pixmap), img)

                self.current_index = 0
                self.image_selected()
            else:
                self.image_label.setText("No images found")

    def image_selected(self):
        if self.image_files and self.current_index >= 0:
            img_path = os.path.join(self.folder_path, self.image_files[self.current_index])
            pixmap = QPixmap(img_path).scaled(400, 250, Qt.AspectRatioMode.KeepAspectRatio)
            self.image_label.setPixmap(pixmap)

    def prev_image(self):
        """Displays the previous image in the list."""
        if self.image_files and self.current_index > 0:
            self.current_index -= 1
            self.image_selected()

    def next_image(self):
        if self.image_files and self.current_index < len(self.image_files) - 1:
            self.current_index += 1
            self.image_selected()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ImageGallery()
    window.show()
    sys.exit(app.exec())
