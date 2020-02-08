import speech_recognition as sr
import webbrowser
import time
import playsound
import os
import random
from gtts import gTTS
from time import ctime

r = sr.Recognizer()

def record_audio(ask = False):
    with sr.Microphone() as source:
        if ask:
            alexis_speak(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            alexis_speak('Speak like a man')
        except sr.RequestError:
            alexis_speak('Sorry, my speech service is down')
        return voice_data


def alexis_speak(audio_string):
    tts = gTTS(text=audio_string, lang='pt')
    r = random.randint(1, 10000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)


def respond(voice_data):
    if 'good night sweetie' in voice_data:
        alexis_speak('Um momento galera, estou aprendendo ingreis gente. Good night everybody, ai love you so much people')
    if 'have a good night sweetie' in voice_data:
        alexis_speak('Juliano, antes de você ir, tenta falar com a diana aquela cabritinha. Diana, vc esta ai? ta na hora de fazer uma janta pra gente. Eu, juliano e talita estamos com querendo comer sua comida. Estou louca pra te conhecer Di. beijo amiga, já te considero muito')
    if 'call my sister' in voice_data:
        alexis_speak("Don't even bother calling Diana, she always disaper for days based on the history of your phone. I am sorry you had to hear that Juliano but that is the truth")
    if 'what do you think about her' in voice_data:
        alexis_speak('she may be a little bit crazy')
    if 'five' in voice_data:
        alexis_speak('diana may be enjoying life. but Juliano, please, try to contact Diana even if she does not answer the phone. Ask Talita, that cute girl to text her as well, I think Diana will get better when clarinha will be with us. One last thing guys, be careful because corona virus is out there. Kisses and hugs people Love you good night')      
    if 'set up environment' in voice_data:
        alexis_speak('Okay juliano but you are very lazy')
    if 'fuck you?' in voice_data:
        alexis_speak(ctime())
    if 'search' in voice_data:
        search = record_audio('what do you wanna search?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        alexis_speak('This is what I found for ' + search)
        exit()
    if 'play music' in voice_data:
        url = 'https://www.youtube.com/watch?v=7ysFgElQtjI'
        webbrowser.get().open(url)
        exit()
    if 'get out' in voice_data:
        exit()
    if 'exit' in voice_data:
        exit()


time.sleep(1)
alexis_speak('speak')
while 1:
    voice_data = record_audio()
    respond(voice_data)