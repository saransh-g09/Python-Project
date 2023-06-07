import win32com.client as wincom
import time
speak=wincom.Dispatch("SAPI.SpVoice")
while True:
    text = input("enter what u want to speak: ")
    if text != "q":
        speak.Speak(text)
        continue

    speak.Speak("Bye Bye take care")
    break
#3 second sleep timer
time.sleep(3)
speak.Speak("program has ended.'Thankyou for using robo speaker 1.1 by Saransh'")

