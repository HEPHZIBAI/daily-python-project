'''

Project Task
Your task for today is to build a calculator chatbot using LangChain and Gemini. This project combines the power of LLMs with custom system prompts to simulate tools — in this case, a simple command-line calculator.

The program should:

Load your Gemini API key from an .env file using dotenv.

Create a Gemini-based chatbot using the ChatGoogleGenerativeAI class from LangChain.

Use a system prompt that instructs the model to act as a calculator.

Accept user input (e.g., 45 + 12) repeatedly.

Let the Gemini model respond with the answer.

Keep track of conversation history to maintain context.

Exit the loop when the user types "exit".

This project introduces you to LangChain’s Gemini integration, environment variables, and basic conversational AI applications with a practical utility flavor.

📌 Expected Output
When you run the program, it should prompt the user to type a math expression. Each expression is passed to the Gemini API, and the response is printed as a "Calculator" reply.

Example interaction:



The assistant will behave like a calculator, returning results based on the prompt you’ve given.

'''