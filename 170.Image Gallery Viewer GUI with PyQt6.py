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
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QListWidget, QVBoxLayout, QFileDialog ,QMainWindow
from PyQt6.QtGui import QPixmap

class app(QApplication):
    def __app__(self):
        


def display(box,image_files):
    i=image_files.index()

def imageget(folder_path):
    image_files = [f for f in os.listdir(folder_path) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]

    for i in image_files:
        box.addItem(i)
    display(box,image_files)

def folder():
    folder_path = QFileDialog.getExistingDirectory()
    if folder_path:
        imageget(folder_path)

app=QApplication(sys.argv)
window=QMainWindow()

window.setWindowTitle("image gallery viewer")
window.setGeometry(400,400,400,400)

label=QLabel("images",window)
label.setGeometry(10,10,180,20)

box=QListWidget(window)
box.setGeometry(10,40,350,200)

prev=QPushButton("previous",window)
prev.setGeometry(10,250,180,40)

next=QPushButton("next",window)
next.setGeometry(200,250,180,40)

select=QPushButton("select folder",window)
select.setGeometry(10,300,360,40)

folder_path=select.clicked.connect(lambda:folder())

window.show()
sys.exit(app.exec()) 