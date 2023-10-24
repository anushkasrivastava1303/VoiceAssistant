import pyttsx3 as p
import speech_recognition as sr
from selenium_web import *
from yt_audio import *
from news import *
import randfacts
from jokes import *
from weather import *
import datetime

engine = p.init()
engine.setProperty('rate',170)
engine.setProperty('volume',1)
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>0 and hour<12:
        return("morning")
    elif hour>=12 and hour<16:
        return("afternoon")
    else:
        return("evening")

today_date = datetime.datetime.now()

r=sr.Recognizer()

speak("hey! good" + wishme() + "this is alien your voice assistant")
speak("and today is" + today_date.strftime("%d") + "of" + today_date.strftime("%B") + "and its currently" + today_date.strftime("%I") + today_date.strftime("%p"))
speak("and temperature in new delhi is" + str(temp()) + "degree celcius" + "and with" + str(des()))
speak("how are you?")

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


elif "news" in text2:
    
    speak("sure, here are top five headlines for you")
    arr=news()
    for i in range(len(arr)):
        print(arr[i])
        speak(arr[i])
    

elif "fact" in text2:
    speak("sure,")
    x = randfacts.getFact()
    print(x)
    speak("did you know that," + x)
    

elif "joke" in text2:
    speak("sure,")
    arr=joke()
    print(arr[0])
    speak(arr[0])
    print(arr[1])
    speak(arr[1])
    
else:
    speak("i am sorry, i cannot do this,but i will learn this soon")
    speak("bye have a great day")