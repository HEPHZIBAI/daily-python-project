'''
Project Description
    Today we will create a beginner-level program dedicated to our Indian friends. 
    India is home to numerous festivals celebrated throughout the year, so in this project, you will create a simple program that reminds users of upcoming Indian festivals. 
    The program will take today’s date as input, compare it with a predefined dictionary of festival dates, and notify the user if a festival is coming up soon.
    Here are the popular festival dates we will use:
    
    festivals = {
    "Diwali": "11-01",
    "Holi": "03-25",
    "Navratri": "10-03",
    "Raksha Bandhan": "08-19",
    "Eid": "04-10",
    "Pongal": "01-14",
    }

Expected Output
    When the user runs the program, it prints out the nearest upcoming festival:

How This Project Matters in the Real-World
    This project introduces how date-based reminders work, which is useful in applications like calendar apps, event scheduling, and automated notifications. Instead of festivals, you could adapt this to set reminders for important deadlines, birthdays, or appointments. Real-world applications include features in banking apps for EMI due dates, HR software for leave tracking, and even e-commerce apps for sale notifications on special occasions. Our program has a simple command line interface, but you could expand this program by coding a GUI interface for making a desktop GUI app or even a web interface using a framework such as Flask or Django to make a web app version.

Prerequisites
    Required Libraries: datetime
'''

import datetime

festivals = {
    "Diwali": "11-01",
    "Holi": "03-25",
    "Navratri": "10-03",
    "Raksha Bandhan": "08-19",
    "Eid": "04-10",
    "Pongal": "01-14",
    }

today = datetime.date.today()
current_year = today.year
festival_dates = []

for festival, date in festivals.items():
    fest_date = datetime.datetime.strptime(f"{current_year}-{date}", "%Y-%m-%d").date()
    festival_dates.append((festival, fest_date))

festival_dates.sort(key=lambda x: x[1])

m=0
for festival, fest_date in festival_dates:
    if fest_date >= today:
        days_left = (fest_date - today).days
        print(f"⏳ {festival} is in {days_left} day(s). Get ready! 🎆")
        m=1
        break
    
if m==0:
    print("No more festivals this year!")