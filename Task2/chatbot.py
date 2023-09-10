from datetime import datetime

# Respones for msg
responses =[
    {
        'keywords': ['hi', 'hello', 'hey'],
        'response': 'Good day there.'
    },
    {
        'keywords': ['how are you','how are you?'],
        'response': "Thank you. I'm doing great. So, how about you?"
    },
    {
        'keywords': ['good', 'well', 'fine'],
        'response': 'That is wonderful to hear!'
    },
    {
        'keywords': ['what is your name', 'who are you','whats your name','your name'],
        'response': 'I am a simple chatbot. My name is JOJO'
    },
    {
        'keywords': ['bye', 'goodbye'],
        'response': 'Goodbye, It was nice to have you'
    },
    {
        'keywords': ['thank you','thankyou'],
        'response': "You're welcome"
    },
    {
        'keywords': ['what is the weather like','how is the weather','how is weather'],
        'response': "I'm sorry , I am incapable for providing weather information.."
    },
    {
        'keywords': ['what time is it','what is time','time?','tell me time','what is time'],
        'response': f"The current time is {datetime.now().strftime('%H:%M:%S')}."
    },
    {
        'keywords': ['what date is it','what is date','date?','tell me todays date','what is todays date','what date today is'],
        'response': f"The current date is {datetime.now().strftime('%Y-%m-%d')}."
    },
    {
        'keywords': ['can you tell me a joke','tell me a joke','you know some joke'],
        'response': "Why couldn't the sunflower ride its bike? It lost its petals."
    },
    {
        'keywords': ['what can you do','what you do'],
        'response': "I'm a simple Chatbot.I can try to Answer some simple Questions.I can tell you date and time."
    },
    {
        'keywords': ['are you alive','are you living'],
        'response': "No, I'm just a computer programmed Chatbot"
    },
    {
        'keywords': ['suggest me a song','do you like songs'],
        'response': "Imagine Dragons: Bones "
    },
    {
        'keywords': ['suggest me a movie','do you like movies','suggest me a movies'],
        'response': " Dune-1 "
    },
    {
        'keywords': ['suggest me a book','do you like books','suggest me a books'],
        'response': " Song of Ice and Fire: Game of Thrones."
    }
]

fallback_response = "I'm sorry, I can't understand. Can you please rephrase your Question ?"

# Finding a Response

def find_response(message):
    # Convertting message to lowercase
    message = message.lower()

    for response in responses:
        if any(keyword in message for keyword in response['keywords']):
            return response['response']

    # Send the response
    return fallback_response
