import pyttsx3 as p
import speech_recognition as sr
import selenium_web
from YT_auto import *
from News import *
import randfacts
from Jokes import *
from weather import *
import datetime

engine = p.init()
engine.setProperty("rate", 140)
voice = engine.getProperty("voices")
engine.setProperty("voice", voice[1].id)

rate = engine.getProperty("rate")


def speak(text):
    engine.say(text)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if 8 < hour < 12:
        return "morning"
    elif 12 <= hour <= 16:
        return "Afternoon"
    else:
        return "Evening"


today_date = datetime.datetime.now()
r = sr.Recognizer()
speak("hello sir good,"+wishme()+"I am your voice assistant")
speak("Today is " + today_date.strftime("%d") + "of" + today_date.strftime("%B") + ", And its currently" + (
    today_date.strftime("%I")) + (today_date.strftime("%M") + (today_date.strftime("%p"))))
speak("Temperature in chennai is " + str(temp()) + " degree celsius along with the" + str(des()))
speak("Ask me anything sir..")
with sr.Microphone() as source:
    r.energy_threshold = 100
    r.adjust_for_ambient_noise(source, 1.2)
    print("listening..")
    audio = r.listen(source)
    text = r.recognize_google(audio)
    print(text)
if "what" and "about" and "you" in text:
    speak("I have goog day sir")
speak("What can I do for you sir?")
with sr.Microphone() as source:
    r.energy_threshold = 100
    r.adjust_for_ambient_noise(source, 1.2)
    print("listening..")
    audio = r.listen(source)
    text2 = r.recognize_google(audio)

if "information" in text2:
    speak("you need information relate to which topic?")
    with sr.Microphone() as source:
        r.energy_threshold = 100
        r.adjust_for_ambient_noise(source, 1)
        print("listening..")
        audio = r.listen(source)
        infor = r.recognize_google(audio)
    speak("search in {} in wikipedia".format(infor))
    print("search in {} in wikipedia".format(infor))
    assist = selenium_web.infow()
    assist.get_info(infor)
elif "play" and "video" in text2:
    speak("you want me to play which video?")
    with sr.Microphone() as source:
        r.energy_threshold = 100
        r.adjust_for_ambient_noise(source, 1)
        print("listening..")
        audio = r.listen(source)
        vid = r.recognize_google(audio)
        print("playing video {} in youtube".format(vid))
        speak("playing  {} in youtube".format(vid))
        assist = music()
        assist.play(vid)
elif "news" in text2:
    print("I will read the following news..")
    arr = news()
    for i in range(len(arr)):
        print(arr[i])
        speak(arr[i])

elif "fact" in text2:
    speak("Sure sir, ")
    x = randfacts.get_fact()
    print(x)
    speak("DID YOU KNOW THAT" + x)

elif "jokes" in text2:
    speak("Ready for some chuckles")
    a = joke()
    print(a[0])
    speak(a[0])
    print(a[1])
    speak(a[1])
