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
from PyQt6.QtWidgets import QMainWindow,QLabel,QApplication,QTextEdit,QPushButton
import speech_recognition as sr

def filesave(text,savelabel,savedtext):
    if text.strip()=="":
        savelabel.setText("no text to save!")
        return
    
    with open('293.Voice Controlled Notepad.txt','a',encoding="utf-8") as f:
        f.write(text+'\n')

    savelabel.setText("File saved successfully!")
    QApplication.processEvents()
    print("file saved")

    with open('293.Voice Controlled Notepad.txt','r',encoding="utf-8") as f:
        notes=f.read()

    if notes.strip():
        savedtext.setText(notes)
    else:
        savedtext.setText("no saved notes yet.")

def hear(label,textbox):
    r=sr.Recognizer()
    mic = sr.Microphone()

    # print(sr.Microphone.list_microphone_names())  to print micphone avaliable

    with mic as source:
        label.setText("Adjusting for ambient noise... Please wait")
        QApplication.processEvents() 
        print("Adjusting for ambient noise... Please wait")
        
        r.adjust_for_ambient_noise(source)
        
        label.setText("Listening...")
        QApplication.processEvents() 
        print("Listening...")
        
        audio = r.listen(source, timeout=10) 
        
        label.setText("Processing...") 
        QApplication.processEvents() 
        print("Processing...")

        try:
            text = r.recognize_google(audio)
            
            label.setText("Recognition Complete ✅")
            QApplication.processEvents() 
            print("You said:", text)
            
            textbox.append(text)
            return 
        except sr.UnknownValueError:
            print("Could not understand audio ❌")
            label.setText("Could not understand audio ❌")
        except sr.RequestError:
            print("No internet connection! 🌐")
            label.setText("No internet connection! 🌐")
        except sr.WaitTimeoutError:
            print("Listening timed out ⏳")
            label.setText("Listening timed out ⏳")
        QApplication.processEvents()

def cwindow():
    app=QApplication(sys.argv)

    window=QMainWindow()
    window.setWindowTitle("voice typing notepad")
    window.setGeometry(500,500,600,700)

    lable=QLabel("voise typing notepad",window)
    lable.setGeometry(10,10,400,30)

    textbox=QTextEdit(window)
    textbox.setGeometry(10,50,580,250)

    listenbutton=QPushButton("start listening 🎤",window)
    listenbutton.setGeometry(10,320,580,40)

    savebutton=QPushButton("save to file 💾",window)
    savebutton.setGeometry(10,370,580,40)

    exitbutton=QPushButton("exit ❌",window)
    exitbutton.setGeometry(10,420,580,40)

    savelable=QLabel('',window)
    savelable.setGeometry(10,470,580,30)

    savedtext=QLabel("saved notes:",window)
    savedtext.setGeometry(10,500,580,180)
    savedtext.setWordWrap(True)

    listenbutton.clicked.connect(lambda: hear(lable,textbox))  
    savebutton.clicked.connect(lambda:filesave(textbox.toPlainText(),savelable,savedtext))
    exitbutton.clicked.connect(app.quit)

    window.show()
    sys.exit(app.exec())

cwindow()


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