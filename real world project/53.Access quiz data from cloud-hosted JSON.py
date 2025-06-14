'''

Project Brief
Let’s start the week by practicing data structures. Take a minute to look at these JSON data. Here is an excerpt of the data:

{
  "quizzes": [
    {
      "quizTitle": "Country Capitals",
      "questions": [
        {
          "id": 1,
          "question": "What is the capital of France?",
          "choices": {
            "Paris": true,
            "London": false,
            "Berlin": false,
            "Madrid": false
          }
        },
        {
          "id": 2,
          "question": "What is the capital of Japan?",
          "choices": {
            "Beijing": false,
            "Seoul": false,
            "Tokyo": true,
            "Bangkok": false
          }
        },
        {
          "id": 3,
          "question": "What is the capital of Canada?",
          "choices": {
            "Toronto": false,
            "Vancouver": false,
            "Ottawa": true,
            "Montreal": false
          }
        }
      ]
    },
    {
      "quizTitle": "Continents and Countries",
      "questions": [
        {
          "id": 4,
          "question": "Which continent is Brazil located in?",
          "choices": {
            "Africa": false,
            "Asia": false,
            "South America": true,
            "Europe": false
          }
        },
        {
          "id": 5,
          "question": "Which continent is Egypt located in?",
          "choices": {
            "Europe": false,
            "Asia": false,
            "Africa": true,
            "Australia": false
          }
        },
        {
          "id": 6,
          "question": "Which continent is Australia located in?",
          "choices": {
            "Asia": false,
            "South America": false,
            "Australia": true,
            "Africa": false
          }
        }
      ]
    },
    {
      "quizTitle": "Rivers and Mountains",
      "questions": [
        {
          "id": 7,
          "question": "Which is the longest river in the world?",
          "choices": {
            "Amazon": false,
            "Nile": true,
            "Yangtze": false,
            "Mississippi": false
          }
        },
        {
          "id": 8,
          "question": "Which is the highest mountain in the world?",
          "choices": {
            "K2": false,
            "Kangchenjunga": false,
            "Lhotse": false,
            "Mount Everest": true
          }
        },
        {
          "id": 9,
          "question": "Which river flows through Paris?",
          "choices": {
            "Thames": false,
            "Seine": true,
            "Danube": false,
            "Rhone": false
          }
        }
      ]
    }
  ]
}
Create a Python program that asks the user to enter the ID of a question in the command line. Then, the program returns the correct answer for that question.


'''