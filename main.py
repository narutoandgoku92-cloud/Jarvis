from skills import speak, tell_time, search_web,listen,wake
from commands import process_command
import datetime



def log(command):
    with open("log.txt ", "a") as file:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{timestamp} - {command}\n")
        
while True:
    try: 
        command = listen().lower()
        log(command)

        if "wake" in command:
            command = wake()

            while command != "bye":
                process_command(command)
                command = listen().lower()
                log(command)

            speak("Going back to sleep. Say wake to wake me up again.")

    except Exception as e:
        print("Error:", e)
        speak("I couldn't catch that. Please try again.")
        
        
        
