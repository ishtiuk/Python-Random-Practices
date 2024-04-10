# import datetime
import pyttsx3

alexa = pyttsx3.init()

voices = alexa.getProperty('voices')
alexa.setProperty('voice', voices[1].id)

def talker(dtt):
    alexa.say(dtt)
    alexa.runAndWait()


today = '09/27/21. i was officially launched in that day'
print(today)
print(type(today))

talker(today)