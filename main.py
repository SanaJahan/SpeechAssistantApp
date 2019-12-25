import playsound
import speech_recognition as sr
import webbrowser
import time
import os
import random
from gtts import gTTS
from time import ctime

# remove the file that is created by the playsound using os module
# initialize the recognizer
r = sr.Recognizer()


def speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 1000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    os.remove(audio_file)


def record_audio(ask=False):
    with sr.Microphone() as source:
        if ask:
            speak(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            speak('Sorry, I did not get that')
        except sr.RequestError:
            speak('Sorry, my speech service is down')
        return voice_data


def respond(voice_data):
    if 'what is your name' in voice_data:
        speak('My name is Sana')
    if 'what time is it' in voice_data:
        print(ctime())
    if 'search' in voice_data:
        search = record_audio('What do you want to search for?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        speak('Here is what I found for ' + search)
    if 'find location' in voice_data:
        location = record_audio('What is the location?')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        speak('Here is the location ' + location)
    if 'exit' in voice_data:
        speak('Ok take care')
        exit(0)


time.sleep(1)
while 1:
    speak('How can I help you?')
    voice_data = record_audio()
    print(voice_data)
    respond(voice_data)
