'''
Project Description
    Today, we will build a Focus Tracker App. 
    This app will help users stay productive during focus sessions by 
        tracking the time spent on tasks, 
        giving motivational messages, and 
        allowing break reminders. 
    It’s a simple desktop app with a graphical user interface containing a timer and task management features to boost productivity.

Expected Output
    The app lets the user type in a task and press the “Start Focus Session” button.
    The time next to the “Time Elapsed” lable will start ticking. 
    When the user has completed the task, they can press the “Complete Task” button. 
    The completed tasks are listed in the white text area
    The app is simple but very useful to keep you focus whenever you start doing a task.

Prerequisites
    Required Libraries: sys, time, PyQt6
                        pip install PyQt6
'''


import sys
from PyQt6.QtWidgets import QMainWindow,QLabel,QApplication,QLineEdit,QBoxLayout

app=QApplication(sys.argv)
window=QMainWindow()
window.setWindowTitle("Focus Tracker")
window.setGeometry(400,400,400,400)

label=QLabel("Enter your task",window)
text=QLabel("gg",window)

layout = QBoxLayout(window)
layout.addWidget(label)
layout.addWidget(text)

window.show()
sys.exit(app.exec())
