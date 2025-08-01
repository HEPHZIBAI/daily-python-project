'''
Today’s project is a fun one: 
    you’ll create a simple text-based chatbot.
    It won’t use any AI or machine learning — instead, it’s a rule-based chatbot that replies based on keywords.
    This is exactly how many early chat systems worked, and it’s a great way to practice string matching, conditionals, and loops.

Project Description
    Your task is to build a basic text chatbot that runs in the terminal.
    The user can type any message, and your bot will look for certain keywords to decide how to respond.

For example:
    If the user says “hello”, the bot could reply with “Hi there! How can I help you today?”
    If the user says “bye”, the bot could say “Goodbye! Have a nice day.”
    If the message doesn’t contain any known keywords, the bot can say “I’m not sure how to respond to that.”

This is an awesome way to practice:
    Loops (to keep the conversation going),
    Conditionals (to check for keywords),
    Basic string handling (like .lower() and in).

Expected Output

🤖 It also suggests using .lower() so you can match keywords case-insensitively.

'''

g={"hello":"Hi there! How can I help you today?",
   "bye":"Goodbye! Have a nice day."}
print("hello! i am a simple chatbot. type something to start talking (or type 'exit' to quit).")
c=input("you: ").strip().lower()

while c!="quit":
    if c in g:
        print("chatbot:",g[c])
    else:
        print("chatbot: i'm not sure how to respond to that.")
    c=input("you: ").strip().lower()