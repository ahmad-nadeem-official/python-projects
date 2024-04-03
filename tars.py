import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import pyaudio
import os


engin = pyttsx3.init('sapi5')
voices = engin.getProperty('voices')
engin.setProperty('voices',voices[0].id) #if you select 1 instead of 0 it will give the voice of a lady
# print(voices[0].id)

def speak(audio):
    engin.say(audio)
    engin.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        speak("good morning")
    elif hour >= 12 and hour <= 18:
        speak("good afternoon")
    else:
        speak("good evening")

    speak("I'm tars, how may i help you sir !")          

def takecommand():# it will allow user to give a microphone command and return string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

        try:
            print("recognising your voice...")
            query = r.recognize_google(audio, language='en-in')
            print(f"user said : {query}\n")
            return query

        except Exception as e:
            print("I'm sorry sir! Please say that again....")
            return ""

if __name__ == "__main__":
    wishme()
    
    while True:
        query = takecommand().lower()         # logic on executing task base on query
        if "can you open my projects" in query:
            projects_dir = 'D:\\projects'
            print(query)

        elif "tell me a joke" in query:
            print(query)
            print("Why don't scientists trust atoms? Because they make up everything!")

        elif 'it was not good' in query:
            print(query)
            print("can i tell you another ?")

        elif ' no ' in query:
            print(query)
            print("any other service for me ?")

        elif 'open google' in query:
            print(query)
            webbrowser.open('google.com')
            

        elif 'what is the time now' in query:
            print(query)
            time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(F'Sir, the time is {time} now')  
            
                       
    # print(query)  # or do whatever you want with the query
