'''
Project Brief
    Your task for this project is to create a desktop program that converts kilometers to miles. 
    The program should have a desktop GUI. 
    You can use any Python GUI library, but the code given in the solution section uses the Tkinter library.

Project Expected Output
    Note that your GUI might look different, but its functionality should be similar to the following snapshot.

Environment Setup Instructions (in your local IDE)
    👉 Skip to the next step if you prefer to code this project in an online browser-based IDE or from your mobile phone.
    If you use Tkinter you don’t need to install anything.
    Execute the main.py file once you have finished coding.

Resources
    You can learn about creating GUIs with Tkinter in this post:
    https://pythonhow.com/how/create-a-simple-tkinter-app/

'''

from tkinter import Tk,Label,Entry,Button

window=Tk()
window.title("KM to Miles Converter")

label=Label(window,text="enter distance in kilometers : ")
label.pack()

km_entry = Entry(window)
km_entry.pack()

def change():
  km = km_entry.get()  # Get the text from the entry box
  greeting = f"distance in miles : {float(km)*0.621371}!"
  greeting_label = Label(window, text=greeting)
  greeting_label.pack()

button = Button(window, text="convert", command=change)
button.pack()

window.mainloop() 