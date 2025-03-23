'''
Project Description
    Create a command-line tool that monitors the health of a list of websites. 
    The app reads a website.txt file where you have listed the websites you want to check. 
    For example:
        websites.txt content:
            https://www.google.com
            https://www.github.com
            https://www.nonexistentwebsite12345.com
            https://www.wikipedia.org
    When executed, the program prints out the status of each website:
    Optionally, the program logs the response time and HTTP status code and outputs results into a log.csv file. 
    Here is how generated log.csv file should look like after running the program:

Prerequisites
    Required Libraries: requests, csv, datetime
                        pip install requests
    Required Files: You need to create a website.txt file in your project directory and add some websites URLs there.
'''

