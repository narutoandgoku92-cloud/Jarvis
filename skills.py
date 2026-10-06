import datetime
import webbrowser
import urllib.parse
from speech import speak, listen
import os
import psutil
import pyautogui
import json
from pathlib import Path

JARVIS_FOLDER = Path.home() / "Music" / "jarvis"

def open_notepad():
    os.startfile("notepad.exe")
    speak("Opening Notepad")
    
def open_calculator():
    os.startfile("calc.exe")
    speak("Opening Calculator")

def open_visual_studio():
    os.startfile(r"C:\Users\gbola\AppData\Local\Programs\Microsoft VS Code\Code.exe")
    speak("Opening Visual Studio Code")

def search_web():
    speak("What are the keywords you want to search for?")
    key_word = listen()
    search = urllib.parse.quote(key_word)
    url = f'https://www.google.com/search?q={search}'
    
    webbrowser.open(url)    
    

def tell_time():
    current_time = datetime.datetime.now()
    speak(f"The current time is {current_time.strftime('%H:%M')}")


def date():
    current_date = datetime.datetime.now()
    speak(f"Today's date is {current_date.strftime('%B %d, %Y')}")
    
    
def hello():
    speak("Hello! How can I assist you today?")
    
    
def screenshot():
    screenshot =pyautogui.screenshot()
    name = datetime.    datetime.now().strftime("%Y-%m-%d_%H-%M-%S") 
    screenshot.save(name + ".png") 


def check_battery():
    battery = psutil.sensors_battery()
    percentage = battery.percent
    speak(f'Your Battery percentage is {percentage} percent')
    
    
    
def create_note():
    speak("What would you like to name the note?")
    note_name = listen()
    with open(JARVIS_FOLDER / f"{note_name}.txt", "w") as f:
        speak("What would you like to write in the note?")
        note_content =listen()
        
        f.write(note_content)
    speak("Note created successfully.")
    
    
def read_note():
    speak("What note would you like to read?")
    note_name = listen()
    with open(f"C:\\Users\\gbola\\Music\\jarvis\\{note_name}.txt", "r") as file:
        content = file.read()
        
        speak(content)
        
        
def add_note():
    speak("What is the name of the note you want to add to?")
    note_add_name = listen()
    
    with open(f"C:\\Users\\gbola\\Music\\jarvis\\{note_add_name}.txt", "a") as file:
        speak("What would you like to add to the note?")
        note_add =listen()
        file.write(note_add)
        
        
        
def search_files():
    speak("What file may i help you find?")
    
    search_file = listen()
    for files in  os.listdir(r"C:\\Users\\gbola\\Music\\jarvis"):
    
        if search_file in files:
            speak(f"File found: {search_file}")
        else:
            speak("File not found.Would like to create a new file with that name?")
            response = listen()
            response = response.lower()
            if "yes" in response:
                with open(f"C:\\Users\\gbola\\Music\\jarvis\\{search_file}.txt", "w") as file:
                    speak("File created successfully.")
                speak("What would you like to write in the new file?")
                new_file_answer = listen().lower()
                if "yes" in new_file_answer:
                    add_note()
                elif "no" in new_file_answer:
                    speak("Okay, I will not add anything to the new file.")
            elif "no" in response:
                speak("Okay, I will not create a new file.")
                


def create_folder():
    speak("What would you like to name the new folder?")
    folder_name = listen().lower()
    if not os.path.exists(f"C:\\Users\\gbola\\Music\\{folder_name}"):
        os.makedirs(f"C:\\Users\\gbola\\Music\\{folder_name}")
        speak("Folder created successfully.")
    else:
        speak("A folder with that name already exists.")
        
        
def dial():
    speak("What name would you like to dial?")
    name_dial = listen()
    os.startfile("WhatsApp.exe")
    speak("Opening WhatsApp")
    


def memory():
    speak("What would you like for me to remember?")
    memory_name = listen()
    speak("What would you like me to remember about that?")
    memory_content = listen()
    speak(f"Okay, I will remember that {memory_name} is {memory_content}.")
    try:
        with open("memory.json", "r") as file:
            memory_data = json.load(file)
    except:
        memory_data = {}
    
    memory_data[memory_name] = memory_content
    with open("memory.json", "w") as file:
        json.dump(memory_data, file,indent=3)
    speak("I will remember that for you.")



def recall_memory():
    try:
        with open("memory.json", "r") as file:
            remembered_content = json.load(file)

        speak("What would you like me to recall?")

        recall_content = listen().lower()

        if recall_content in remembered_content:

            answer = remembered_content.get(recall_content)

            speak(f"{recall_content} is {answer}")

        else:
            speak("I don't remember that.")
        
    except FileNotFoundError:
        speak("Files doesn't Exist")
def wake():
    speak("Hey . I am Jarvis your personal assistant. How may i help you today?")
    return listen()


def list_files():
    files = os.listdir(r"C:\\Users\\gbola\\Music\\jarvis")
    speak(files)
    
def select():
    speak("What file would you like to select?")
    selected = listen()
    if selected in os.listdir(r"C:\\Users\\gbola\\Music\\jarvis"):
        speak(f'Opening {selected}')
        os.startfile(selected)
        speak(f"{selected} has been opened")

def delete_file():
    speak("What file would you like to delete?")
    file_to_delete = listen()
    if file_to_delete in os.listdir(r"C:\\Users\\gbola\\Music\\jarvis"):
        os.remove(f"C:\\Users\\gbola\\Music\\jarvis\\{file_to_delete}")
        speak(f"{file_to_delete} has been deleted.")
    else:
        speak("File not found.")