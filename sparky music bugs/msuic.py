import speech_recognition as sr
import os
import random

lsitern = sr.Recognizer()

def red():
    try:
        with sr.Microphone() as src:
            listen = lsitern.listen(src)
            cmd = lsitern.recognize_google(listen)
            at = cmd.lower()
    except:
        pass
    return at

at = red()
print(at)


if 'music' in at:
        music_dir = 'D:\\cp77music'
        songs = os.listdir(music_dir)
        songs_no = random.randint(0,len(music_dir))
        song_name = songs[songs_no]
        # talk("ok, playing"+song_name+'for you')
        os.startfile(os.path.join(music_dir, songs[songs_no]))
        # talk('is it interesting sir?')  
        # complement = taking_command()
        # if 'no' in complement:
        #     # talk('ok, playing another')
        #     anthr_rand = random.randint(0,len(music_dir))
        #     os.startfile(os.path.join(music_dir, songs[anthr_rand]))
        # elif 'yes' in complement or 'yup' in complement or 'yeah' in complement or 'yea' in complement or 'ok' in complement:
        #     talk('okey sir, continuing this')