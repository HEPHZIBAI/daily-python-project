'''
Level: Real-World
	This project is designed for learners who know Python fundamentals and are learning to build real-world programs.

Project Description
	Today, we will build a Voice-Controlled Notepad using Python and the PyQt6 library! 
    This app allows users to dictate text and saves it to a file. 
    It's an innovative project that combines speech recognition with a graphical text editor, making it perfect for productivity enthusiasts.

Prerequisites
	Required Libraries: sys, speechrecognition, PyQt6
'''

import sys
from PyQt6.QtWidgets import QMainWindow,QLabel,QApplication
import speech_recognition as sr
'''
app=QApplication(sys.argv)
window=QMainWindow()
window.setWindowTitle("voice typing notepad")
window.setGeometry(400,400,400,400)
window.show()
sys.exit(app.exec())
'''
r=sr.Recognizer()
mic = sr.Microphone()

# print(sr.Microphone.list_microphone_names())  to print micphone avaliable

with mic as source:
    print("Adjusting for ambient noise... Please wait")
    r.adjust_for_ambient_noise(source)
    print("Listening...")
    audio = r.listen(source, timeout=5)  
    print("Processing...")
    text = r.recognize_google(audio)
    print("You said:", text)
'''    except sr.UnknownValueError:
        print("Sorry, I couldn't understand the audio.")
    except sr.RequestError:
        print("Could not request results, check your internet connection.")
    except sr.WaitTimeoutError:
        print("Listening timed out. Try speaking again.")'''


'''
notes:
Each Recognizer instance has seven methods for recognizing speech from an audio source using various APIs. These are:

recognize_bing(): Microsoft Bing Speech
recognize_google(): Google Web Speech API
recognize_google_cloud(): Google Cloud Speech - requires installation of the google-cloud-speech package
recognize_houndify(): Houndify by SoundHound
recognize_ibm(): IBM Speech to Text
recognize_sphinx(): CMU Sphinx - requires installing PocketSphinx
recognize_wit(): Wit.ai

Of the seven, only recognize_sphinx() works offline with the CMU Sphinx engine. 
The other six all require an internet connection.

'''