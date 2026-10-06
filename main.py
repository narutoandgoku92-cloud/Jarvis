from skills import speak, tell_time, search_web,listen,wake
from commands import process_command
import datetime


while True:
    try: 
        command = listen().lower()

        if "wake" in command:
            command = wake()

            while command != "bye":
                process_command(command)
                command = listen().lower()

            speak("Going back to sleep. Say wake to wake me up again.")

    except Exception as e:
        print("Error:", e)
        speak("I couldn't catch that. Please try again.")
        
        
        
def log(command):
    with open("log.txt ", "a") as file:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{timestamp} - {command}\n")
        