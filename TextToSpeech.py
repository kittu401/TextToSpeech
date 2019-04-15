#importing Required libraries
import speech_recognition as sr
import pyttsx3
import time
import os
import win32com.client
# initialisation
voice = sr.Recognizer()
voice.energy_threshold = 1000
engine = pyttsx3.init()
user = "Kishore"
t = str(time.ctime())
en_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
# testing
with sr.Microphone() as source:
    print("Please say something")
    audio = voice.listen(source)
    try:
        x = format(voice.recognize_google(audio))
        engine.setProperty('rate', 125)
        engine.setProperty('voice', en_voice_id)
        engine.say("Hello" + user + "Very Good Morning present time is " + t)
        engine.say("Let me know if you need any help")
        engine.say("Have a good Day,Thank you")
        engine.runAndWait()

    except:
        pass

