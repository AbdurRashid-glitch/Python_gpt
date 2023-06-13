# VOICE ASSISTANT FROM SPEECH-TO-TEXT
#install the package : pip install SpeechRecognition
#install audio module:  pip install pyaudio

import os
import openai
import pyttsx3
import speech_recognition as sr

openai.api_key = "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"

start_sequence = "\nAI:"
restart_sequence = "\nHuman: "

prompt="The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\nHuman: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help you today?\nHuman: "

engine = pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()


def speech_to_text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-BD")
        print("Human Said: " + query)
    except Exception as e:
        print(e)
        speak("Say that again please...")
        return "None"
    return query

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
    print(data)
    speak(data)
    #return data


while True:
    query = speech_to_text()
    gpt_output(query)
