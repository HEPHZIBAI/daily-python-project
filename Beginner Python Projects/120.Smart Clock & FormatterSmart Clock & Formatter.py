'''
Your task for today is to build a Python script that prints a mini time dashboard for “right now.” 
You’ll practice working with datetime, formatting strings, and user input while exposing multiple useful time representations for everyday scripts.

📝 Project Task
    The program should:
        Daily Python Projects is a reader-supported publication. To receive new posts and support my work, consider becoming a free or paid subscriber.
        Show the current local date/time in two formats, e.g.
        Monday, August 11, 2025 – 14:35
        ISO 2025-08-11 14:35:00 
        Provide a 12h/24h toggle via user input (e.g., 12 or 24).
        Display the ISO week number and the day of year.
        Print the date with an ordinal day, e.g., August 11th, 2025.

    This is a practical way to master Python’s date/time APIs and produce clean, readable outputs for dashboards or logs.

📌 Expected Output
    When you run the program, it should ask whether you want 12h or 24h format, then print a dashboard similar to:
        Choose time format (12/24): 24
        Current Local Time (Verbose): Monday, August 11, 2025 – 14:35
        Current Local Time (ISO): 2025-08-11 14:35:00
        ISO Week Number: 33
        Day of Year: 223
        Date with Ordinal: August 11th, 2025
    If the user chooses 12, the verbose time should display in hh:mm AM/PM format (e.g., 02:35 PM).
'''

from datetime import datetime

def get_ordinal(n):
    """Return ordinal string for a number (e.g., 1 -> '1st')."""
    if 11 <= n % 100 <= 13:
        suffix = "th"
    else:
        suffix = {1: "st", 2: "nd", 3: "rd"}.get(n % 10, "th")
    return f"{n}{suffix}"

now = datetime.now()
formate=int(input("choose time format (12/24): "))

if format== 12:
    print("\ncurrent local time (verbose): ",now.strftime("%A, %B %d, %Y – %I:%M %p"))
else:
    print("\ncurrent local time (verbose): ",now.strftime("%A, %B %d, %Y – %H:%M"))
print("current Local Time(ISO): ",now.strftime("%Y-%m-%d %H:%M:%S"))
print("ISO week number: ",now.isocalendar()[1])
print("day of year: ",now.timetuple().tm_yday)
print("date with ordinal: ",f"{now.strftime('%B')} {get_ordinal(now.day)}, {now.year}")