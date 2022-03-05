import pyttsx3 
import playsound
import speech_recognition as sr
from gtts import gTTS

def get_audio():
   r = sr.Recognizer()
   with sr.Microphone() as source:
      audio = r.listen(source)
      said = ""

      try:
         said = r.recognize_google(audio)
         print(said)
      except Exception as e:
         print("Exception: " + str(e))

   return said

import wikipedia
from tkinter import *
from tkinter.messagebox import showinfo
import keyboard
engine = pyttsx3.init() 
search=get_audio()
answer=wikipedia.summary(search)
engine.say(answer) 
engine.runAndWait() 
