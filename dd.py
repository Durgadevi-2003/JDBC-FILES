import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def whishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning dude")
    elif hour>=12 and hour<18:
        speak("good afternoon dude")
    else:
        speak("good evening dude")

    speak("please tell me how can i help you")

def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Wait for few monents")
        query=r.recognize_google(audio,language='en-in')
        print("user said", query)
    except Exception as e:
        print(e)
        speak("Say that again please")
if __name__=="__main__":
    whishme()
    while True:
        query=takecommand().lower()

        if "wikipedia" in query:
             speak("Searching in wikipedika")
             query=query.replace("wikipedia","")
             results=wikipedia.summary(query,sentences=2)
             speak("According to wikipedia")
             speak(results)