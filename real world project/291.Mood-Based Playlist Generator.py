'''
Project Description
    Today, we will build a Mood-Based Playlist Generator with Python that generates a playlist based on the user’s mood. 
    By simply choosing from options like “Happy,” “Sad,” or “Energetic,” the app will provide a selection of songs that match that mood. 
    The app will fetch song recommendations from a mock API (to keep it simple), and you can expand this by integrating it with real music APIs like Spotify or YouTube. 
    We will use the PyQt6 library for this, but you can use any other GUI library

Expected Output
    The GUI lets the user select their mood from a list of three moods (Happy, Sad, and Energetic).
    After selecting a mood, the user can press the “Generate Playlist” button to get a recommendation of songs.
    We are simplifying the code by getting the data from a dictionary stored inside the script:

        
        playlists = {
            "Happy": [
                ("Happy Song 1", "Artist 1"),
                ("Happy Song 2", "Artist 2"),
                ("Happy Song 3", "Artist 3"),
                ("Happy Song 4", "Artist 4"),
                ("Happy Song 5", "Artist 5")
            ],
            "Sad": [
                ("Sad Song 1", "Artist 1"),
                ("Sad Song 2", "Artist 2"),
                ("Sad Song 3", "Artist 3"),
                ("Sad Song 4", "Artist 4"),
                ("Sad Song 5", "Artist 5")
            ],
            "Energetic": [
                ("Energetic Song 1", "Artist 1"),
                ("Energetic Song 2", "Artist 2"),
                ("Energetic Song 3", "Artist 3"),
                ("Energetic Song 4", "Artist 4"),
                ("Energetic Song 5", "Artist 5")
            ]
        }
    Daily Python Projects is a reader-supported publication. To receive new posts and support my work, consider becoming a free or paid subscriber.

Prerequisites
    Required Libraries: sys, random, PyQt6
                        pip install PyQt6
'''

import sys
from PyQt6.QtWidgets import QMainWindow,QLabel,QApplication,QPushButton,QComboBox

playlists = {
"Happy": '''Happy Song 1 Artist 1\nHappy Song 2 Artist 2\nHappy Song 3 Artist 3\nHappy Song 4 Artist 4\nHappy Song 5 Artist 5''',
"Sad":'''Sad Song 1 Artist 1\nSad Song 2 Artist 2\nSad Song 3 Artist 3\nSad Song 4 Artist 4\nSad Song 5 Artist 5''',
"Energetic":'''Energetic Song 1 Artist 1\nEnergetic Song 2 Artist 2\nEnergetic Song 3 Artist 3\nEnergetic Song 4 Artist 4\nEnergetic Song 5 Artist 5'''
        }

def buttonclicked(playlist,combobox):
    text=combobox.currentText()
    if text=="select your emotion":
        playlist.setText("please select a valid mood!")
    else:
        playlist.setText(playlists[text])
    QApplication.processEvents()

app=QApplication(sys.argv)
window=QMainWindow()
window.setGeometry(400,400,400,400)
window.setWindowTitle("mood-based playlist generator")

lable=QLabel("select your mood:",window)
lable.setGeometry(10,10,280,40)

combobox=QComboBox(window)
combobox.addItems(["select your emotion","Happy","Sad","Energetic"])
combobox.setGeometry(10,50,280,35)

playlist=QLabel('',window)
playlist.setGeometry(10,90,280,100)

generatebuttton=QPushButton("generate playlist",window)
generatebuttton.setGeometry(10,180,280,35)

generatebuttton.clicked.connect(lambda:buttonclicked(playlist,combobox))

window.show()
sys.exit(app.exec())