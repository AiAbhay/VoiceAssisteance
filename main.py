import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import os
import time

def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")  # code is ready to run
        recognizer.adjust_for_ambient_noise(source)  # remove noise
        audio = recognizer.listen(source)
        try:
            print("recognizing...")
            data = recognizer.recognize_google(audio)
            return data
        except sr.UnknownValueError:
            print("Not Understood")

def speechtx(x):        #jarvis voice
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)#male or female voice
    rate = engine.getProperty('rate')
    engine.setProperty('rate',150)
    engine.say(x)
    engine.runAndWait()

if __name__ == '__main__':

    #if sptext().lower == "hey peter":
    while True :
        data1 = sptext().lower()
        if "your name" in data1:
            name = "my name is jarvis"
            speechtx(name)

        elif "old are you" in data1:
            age = "i am just one month year old"
            speechtx(age)

        elif 'time' in data1:
            time = datetime.datetime.now().strftime("%I%M%p")
            speechtx(time)
        elif 'youtube' in data1:
            webbrowser.open("https://www.youtube.com/")
        elif 'instagram' in data1:
            webbrowser.open("https://www.instagram.com/")
        elif "joke" in data1:
            joke_1 = pyjokes.get_joke(language="en",category="nautral")
            print(joke_1)
            speechtx(joke_1)
        # elfi 'song' in data1:
        #     add = ""
        #     list1 = os.listdir(add)
        #     print(list1)
        #     os.startfile(os.path.join(add,list1[1]))
        # elif "exit" in data1:
        #     speechtx("thankyou")
        #     break

       # time.sleep(2)
    #else:
     #   print("thanks")