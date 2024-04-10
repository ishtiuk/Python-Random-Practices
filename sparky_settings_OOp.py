import pyttsx3
import time

alexa = pyttsx3.init()

class alexa_function_settings:
    def __init__(self):
        self.rating = 190
        self.voice = 0

    def change_rate_set(self, rate_value):
        self.rating = rate_value
    def change_voice_id(self, voice_id_value):
        self.voice = voice_id_value

yr = alexa_function_settings()
print(yr.rating)

mian = input('''<<======== to Continue enter C ========>>
<<======== to Settings enter S ========>>
::--> ''')
print('\n')

if mian == 'C':
    pass
elif mian == 'S':
    setti = input('''<<======== Settings ========>>
    <<== Enter R to change Talking rate ==>>
    <<==   Enter V to change Voice id   ==>> 
    ::--> ''')
    if setti == 'R':
        voiRT = int(input('''
        <<== Enter any Rate between 150 to 500
        ::--> '''))
        if voiRT >= 150 and voiRT <= 500:
            yr.change_rate_set(voiRT)
        else:
            print('Sorry, Sir. Invalid Selection')

    elif setti == 'V':
        voiID = int(input('''
        <<== Enter 0 for Male AI voice   ==>>
        <<== Enter 1 for Female AI voice ==>>
        ::--> '''))
        if voiID == 0 or voiID == 1:
            yr.change_voice_id(voiID)
        else:
            print('Sorry, Sir. Invalid Selection')

def taler(tt):
    alexa.say(tt)
    alexa.runAndWait()

rate = alexa.getProperty('rate')
alexa.setProperty('rate', yr.rating)

voice = alexa.getProperty('voices')
alexa.setProperty('voice', voice[yr.voice].id)

i = 0
while i < 2:
    taler('hello sir, welcome to nightcity. have a nice journey')
    time.sleep(1)
    i += 1

