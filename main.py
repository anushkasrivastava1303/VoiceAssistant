import pyttsx3 as p
import speech_recognition as sr
from selenium_web import *
from yt_audio import *


engine = p.init()
engine.setProperty('rate',170)
engine.setProperty('volume',1)
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()


r=sr.Recognizer()
speak("hey! this is alien your voice assistant,  how are you")
mic = sr.Microphone(device_index=2)
with mic as source:
    r.energy_threshold=10000
    r.adjust_for_ambient_noise(source,1.2)
    print("listening...")
    audio = r.listen(source)
    text = r.recognize_google(audio)
    print(text)
if "what"  and "you" in text:
    speak("i am doing good")
speak("how can i help you?")


mic = sr.Microphone(device_index=2)
with mic as source:
    r.energy_threshold=10000
    r.adjust_for_ambient_noise(source,1.2)
    print("listening...")
    audio = r.listen(source)
    text2 = r.recognize_google(audio)
    print(text2)


if "information" and "know" and "data" and "info" in text2:
    speak("okay! about which topic?")
    
    mic = sr.Microphone(device_index=2)
    with mic as source:
        r.energy_threshold=10000
        r.adjust_for_ambient_noise(source,1.2)
        print("listening...")
        audio = r.listen(source)
        infor = r.recognize_google(audio)
        print(infor)
        
    print("searching in wikipedia")
    speak("searching in wikipedia")
    assist=infow()
    assist.get_info(infor)


elif "play" and "video" in text2:
    speak("okay! which video")
    mic = sr.Microphone(device_index=2)
    with mic as source:
        r.energy_threshold=10000
        r.adjust_for_ambient_noise(source,1.2)
        print("listening...")
        audio = r.listen(source)
        vid = r.recognize_google(audio)
        print(vid)
    
    print("playing video in youtube")
    speak("playing video  in youtube")
    assist=music()
    assist.play(vid)
    


