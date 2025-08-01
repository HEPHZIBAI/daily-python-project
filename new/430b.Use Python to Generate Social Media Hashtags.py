'''
Project Description
    💡 Imagine effortlessly creating the perfect hashtags for your social media posts—without racking your brain! 
    With this project, you’ll build a smart hashtag generator that transforms phrases into viral-ready tags. 
    Next time you see trending hashtags online, you’ll know the logic behind them!

How the Program Works
    Your program should start by prompting the user to submit a phrase. 
    For example, below the user has entered “take life easy”:
    After the user presses Enter, your program should concatenate the user's words, 
    capitalize the first letter of each word, and add a hashtag in front:
    There you go! Good luck with coding this!
    Optional: If you want to make the program more complex, print out “Error: Hashtag too long!" 
    if the user enters a phrase longer than 280 characters.

How This Project Matters in the Real-World
    Social media platforms, SEO tools, and marketing software all rely on text formatting algorithms like this. 
    Brands and influencers use similar automation to generate catchy, optimized hashtags that boost engagement. 
    By building this, you’ll understand how text manipulation is used in digital marketing and content creation.

'''

tag=input("Enter a phrase for your hashtag : ").strip()
if len(tag)>280:
    print("Error: Hashtag too long!")
else:
    tag=tag.title()
    tag=tag.replace(' ','')
    print("#"+tag)