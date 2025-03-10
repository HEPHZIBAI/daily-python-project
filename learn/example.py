from PyQt6.QtWidgets import QApplication,QMainWindow,QLabel
import sys

app=QApplication(sys.argv)
window=QMainWindow()
window.setWindowTitle("example")
window.setGeometry(400,400,400,400)

lable=QLabel("text",window)
lable.move(50,50)

window.show()

sys.exit(app.exec())