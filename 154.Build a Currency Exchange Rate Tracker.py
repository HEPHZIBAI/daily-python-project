'''
Project Description
    Create a Python command-line application that fetches real-time currency exchange rates and 
    displays the conversion rates between a base currency (like USD) and 
    a list of user-selected target currencies. 
    The app will also allow users to convert amounts between currencies and 
    save the results to a file for later reference.
    In the example above, the user enters USD as the base currency and EUR as the target currency and they submit an amount of 10 USD and the program returns 9.6 EUR. The exchange event is saved in a text file:
    Tip: You can use the Exchange Rate API for free to get real-time exchange rates with Python. You don’t need an API key.

Learning Benefits
    Work with APIs to fetch real-time data.
    Practice parsing JSON responses and working with Python’s requests library.
    Learn about user input validation and file operations.
    Enhance knowledge of financial data handling.

Prerequisites
    Required Libraries: datetime, requests
                        pip install requests
'''
import requests
import datetime

def exchange_rate(currency,target):
    url = f"https://api.exchangerate-api.com/v4/latest/{currency}"
    response = requests.get(url)
    
    if response.status_code != 200:
        print("Error fetching data. Please check your internet connection or currency code.")
        return None

    data = response.json()
    if target not in data['rates']:
        print(f"Invalid target currency: {target}")
        return None

    return data['rates'][target]

def convert(currency,target,amount):
    rate=exchange_rate(currency,target)
    if rate is None:
        return None

    return round(amount*rate,2)

def save(current,target,amount,ans):
    with open("154.Build a Currency Exchange Rate Tracker.txt",'a') as f:
        time=datetime.datetime.now().strftime("%Y-%m-%D %H:%M:%S")
        f.write(f"{time} |{amount} {current} = {ans} {target}\n")

print("Welcome to the currency exchange rate tracker!")
currency=input("enter the base currency (e.g., USD): ").upper()

print("available currencies : USD, AED, ALL, AMD, ANG, AOA, ARS, AUD, AWG ...")
target=input("enter target currencies (comma-separated, e.g., EUR, GBP): ").upper()
amount=float(input("enter the amount in USD:"))

ans=convert(currency,target,amount)

if ans is not None:
    print("conversion results:")
    print(f"{amount} {currency} = {ans} {target}")
    save(currency,target,amount,ans)
    print("results saved to 154.Build a Currency Exchange Rate Tracker.txt.")