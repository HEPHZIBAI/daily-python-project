'''
Project Description
    Your project for today is to build a small real-world Python app that downloads all images from a webpage.

You’ll write a script that:
    takes any URL,
    finds all the image elements on the page
    downloads each image to a folder on your computer.
    Our code in the Solution page works for multiple URLs. 
    Here are two URL examples you can use and download the images inside them:
        https://books.toscrape.com/
        https://en.wikipedia.org/wiki/Tomato

    This is the kind of small utility script that’s super handy in real life, for example:
    Downloading a full image gallery from a documentation page or design portfolio
    Saving sample product photos from a public catalog for analysis
    Grabbing icon or asset sets to build a local library

In this project, you’ll use:
    requests to fetch the HTML content,
    BeautifulSoup to parse the HTML and find all <img> tags,
    and urllib.parse.urljoin to build full image URLs.

Expected Output
    When you run your program, it should create a folder like downloaded_images and print out something like:
    Downloaded: 710e0dff-efdb-417c-bd73-04a6c22307f9.jpg
    Downloaded: 5b77ee93-3f60-42f3-bf55-77ff9509c232.jpg
    ...
    ✅ All images downloaded!
    And you’ll find the image files neatly saved in the downloaded_images folder. 
    Here are the images from the https://books.toscrape.com/ webpage:
'''