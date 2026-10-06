import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()
voices = engine.setProperty("voice", engine.getProperty("voices")[1].id)
engine.setProperty("rate", 150)  
engine.setProperty("volume", 1.0)



def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        
        
        audio = recognizer.listen(source, timeout=10)
        
        
    try:
        command = recognizer.recognize_google(audio)
        command =command.lower()
        return command
    except sr.UnknownValueError:
        print("Sorry, I could not understand what you said.")
        return ""
    




def speak(text):
    engine.say(text)
    engine.runAndWait()
