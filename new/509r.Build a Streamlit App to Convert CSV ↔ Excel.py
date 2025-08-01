'''

Build Real Python Skills, One Practical App at a Time 🚀

Every small app you build gives you more power to automate and solve everyday problems — which is exactly why these daily Python projects matter.
Today’s challenge is a perfect example of a real-world tool you might actually use at work or in your side projects: you’ll build a simple Streamlit web app that lets users upload a CSV file and convert it to Excel, or upload an Excel file and convert it to CSV.

This is the kind of small utility that companies build for internal teams to make file conversions easy without manually opening spreadsheets.
You’ll practice working with file uploads, reading and writing data with pandas, generating downloadable files on the fly, and building a clean web interface — all essential real-world Python skills.

Daily Python Projects is a reader-supported publication. To receive new posts and support my work, consider becoming a free or paid subscriber.

Project Task
Build a Streamlit app that:

✅ Lets users upload either a CSV or an Excel (.xlsx) file.
✅ Detects which type of file they uploaded.
✅ Converts:

CSV → Excel

Excel → CSV
✅ Displays the data in a nice table.
✅ Provides a download button so they can instantly get the converted file.

This is an awesome way to practice:

File uploads and downloads in Streamlit,

Working with pandas DataFrames,

Converting data formats (CSV ↔ Excel),

And giving users a polished, interactive experience.

Expected Output
When the app runs in the browser, it might look like:


Then after uploading a file, it shows the data in a table and provides a download button:


The same happens if the user provides an .xlsx file instead of CSV, but this time the Excel is converted to CSV instead of the other way around.

💡 Hint
Not sure where to start? Click the Show Hint button.
It will show you how to use st.file_uploader() to get the file, load it with pandas.read_csv() or pandas.read_excel(), and then generate a downloadable file in memory with BytesIO.

Show Hint


It also explains how to use st.download_button() to give users a quick download link.

'''

