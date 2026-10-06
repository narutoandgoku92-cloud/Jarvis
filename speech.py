import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()
voices = engine.setProperty("voice", engine.getProperty("voices")[1].id)
engine.setProperty("rate", 150)  
engine.setProperty("volume", 1.0)



def listen():
    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            print("Listening....")
            audio = recognizer.listen(source, timeout=10)

        command = recognizer.recognize_google(audio)
        return command.lower()

    except sr.WaitTimeoutError:
        print("No speech detected.")
        return ""

    except sr.UnknownValueError:
        print("Sorry, I could not understand what you said.")
        return ""

    except sr.RequestError:
        print("Speech recognition service is unavailable.")
        speak("I am having trouble connecting to the speech recognition service.")
        return ""

    except OSError:
        print("Microphone error.")
        speak("I could not access the microphone.")
        return ""



def speak(text):
    engine.say(text)
    engine.runAndWait()
