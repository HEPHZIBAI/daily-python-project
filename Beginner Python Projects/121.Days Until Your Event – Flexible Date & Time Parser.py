'''
Your task for today is to build a robust countdown tool that accepts a target date (and optional time) in multiple formats, parses it safely, and shows a live-style summary of how long is left. 
You’ll practice date parsing, error handling, recurrence logic, and human‑friendly formatting.

📝 Project Task
    The program should:
        Ask the user for a target date (e.g., birthday or deadline) and accept multiple input formats, such as:
            YYYY-MM-DD, DD/MM/YYYY, Aug 11, 2025, etc.
        Parse robustly. If parsing fails, reprompt with hints and examples until a valid date (and optional time) is provided.
        If the parsed date/time is in the past, treat it as a recurring annual event and compute time until the next occurrence.
        Output remaining time in days, hours, and minutes.
        Show the weekday name of the target date and whether it’s a weekend.
        Allow an optional time of day (e.g., 15:30) and include it in the countdown calculation.
    This is a practical project for real-life reminders, event trackers, and scheduling utilities.

📌 Expected Output
    When you run the program, it should guide the user through input and produce a clear countdown, e.g.:
    If parsing fails:
'''

from datetime import datetime, timedelta
import re
import time
import sys
