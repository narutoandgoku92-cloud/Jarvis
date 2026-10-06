from skills import list_files,speak,dial,tell_time,memory,recall_memory ,search_web,create_folder ,date,open_calculator,open_notepad,open_visual_studio, hello,screenshot,check_battery,read_note,create_note,search_files,add_note







commands = {
    "dial": dial,
    "recall memory": recall_memory,
    "memory": memory,
    "create folder" : create_folder,
    "calculator": open_calculator,
    "visual studio": open_visual_studio,
    "open notepad": open_notepad,
    "read note": read_note,
    "search files": search_files,
    "add note": add_note,
    "screenshot": screenshot,
    "battery": check_battery,
    "time": tell_time,
    "search": search_web,
    "date": date,
    "hello": hello,
    "list files": list_files
    
}


def process_command(command):
    for value,key in commands.items():
        if key in command:
            value()
            return
    speak("Sorry, I did not understand that command.")