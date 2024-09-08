import pyttsx3
txt_spch=pyttsx3.init()
q=input("Enter the text you want to convert : ")
txt_spch.say(q)
txt_spch.runAndWait()
