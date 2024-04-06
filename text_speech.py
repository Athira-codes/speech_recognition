

import pyttsx3

txt_sp = pyttsx3.init()
text = input("Enter the text...\n")
voices = txt_sp.getProperty('voices')
for voice in voices:
    print("ID:", voice.id)
txt_sp.setProperty('voice', voices[0].id)  # Setting the voice to the first one in the list
txt_sp.say(text)
txt_sp.runAndWait()
