'''

Your task for today is to build a terminal-based stopwatch that supports lap timing, pausing/resuming, and a final summary. You’ll practice timing with Python, command parsing in a loop, and generating a clean session report—with an optional CSV autosave.

📝 Project Task
The program should:

Provide commands: start, lap, pause, resume, stop, reset, quit.

Record laps and print each lap entry with lap number, lap duration, and total elapsed.

On stop, print a summary showing: total time, number of laps, fastest lap, slowest lap, average lap.

(Optional) Autosave the session to stopwatch_sessions.csv (append mode) with columns:
date, start_time, total_duration, laps, fastest, slowest, average.

This project is a hands-on way to master time deltas, state management in a REPL-style loop, and producing user-friendly summaries.

📌 Expected Output
A typical interaction should look like:

Command (start/lap/pause/resume/stop/reset/quit): start
Started at 14:32:10
Command: lap
Lap 1 — 00:00:12.34 (Total: 00:00:12.34)
Command: lap
Lap 2 — 00:00:08.91 (Total: 00:00:21.25)
Command: pause
Paused at 00:00:21.25
Command: resume
Resumed.
Command: lap
Lap 3 — 00:00:05.10 (Total: 00:00:26.35)
Command: stop

Summary
-------
Total time:   00:00:26.35
Laps:         3
Fastest lap:  00:00:05.10 (Lap 3)
Slowest lap:  00:00:12.34 (Lap 1)
Average lap:  00:00:08.45
If autosave is enabled, the program should append a new row to stopwatch_sessions.csv like:

2025-08-11,14:32:10,00:00:26.35,3,00:00:05.10,00:00:12.34,00:00:08.45

'''

