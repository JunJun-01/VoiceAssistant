import speech_recognition as sr
import pyaudio
import time
import webbrowser
import pyttsx3

r = sr.Recognizer()
r.energy_threshold = 4000

#detect user speech into text
def record_audiodata(ask=False):
    with sr.Microphone() as source:
        if ask:
            baymax_speak(ask)
        audio = r.listen(source)
        voicedata = ''
        # Detect English and help with noise interruption that would give Unknown Value
        try:
            voicedata = r.recognize_google(audio)
            print(voicedata)
        except sr.UnknownValueError:
            baymax_speak('Please repeat. I did not get that.')
        except sr.RequestError:
            baymax_speak('Speech service down.')
        return voicedata

#text to speech
def baymax_speak(x):
    speak = pyttsx3.init()
    print(x)
    speak.say(x)
    speak.runAndWait()
    speak.stop()
    
#user respond on specific topics
def respond(voicedata):
    if 'what is your name' in voicedata:
        baymax_speak('My name is BAYMAX. Your virtual assistant.')
    if 'time' in voicedata:
        baymax_speak(time.ctime())
    if 'Google' in voicedata:
        search = record_audiodata('What do you want to search for?')
        url = 'https://www.google.com/search?q=' + search
        webbrowser.get().open(url)
        baymax_speak('Here is the result from Google for ' + search)
        print("Directing to:" + url)
    if 'locate' in voicedata:
        location = record_audiodata('Which location?')
        url = 'https://www.google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        baymax_speak('Here is the result from Google for ' + location)
        print("Directing to:" + url)
    if 'exit' in voicedata:
        exit()

#repeating function to continue message.
time.sleep(1)
baymax_speak('Hey User, How can I help you?')
while 1:
    voicedata=record_audiodata()
    respond(voicedata)
