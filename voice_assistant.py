# VOICE ASSISTANT FROM TEXT-TO-SPEECH
# have to install package for text to speech: pip install pyttsx3 
import pyttsx3
import os
import openai


openai.api_key = "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"

start_sequence = "\nAI:"
restart_sequence = "\nHuman: "

prompt="The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\nHuman: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help you today?\nHuman: "


## Speak Function: 
engine = pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()
    
# speak("Hello, I'm a personal assistant , How can I help you?")

def gpt_output(prompt):
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    temperature=0.9,
    max_tokens=150,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0.6,
    stop=[" Human:", " AI:"]
    )
    data = response.choices[0].text
    #print(data)
    speak(data)
    #return data


while True:
    query = input("Ask a Question: \n")
    gpt_output(query)