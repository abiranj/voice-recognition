from gtts import gTTS
import speech_recognition as sr
import os
import webbrowser


def talktome(audio):
    print(audio)
    tts = gTTS(text=audio, lang='en')
    tts.save('audio.mp3')
    os.system('mpg123 audio.mp3')


def mycommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('im ready for your command')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

        try:
            command = r.recognize_google(audio)
            print('you said :' + command + '\n')

        except sr.UnknownValueError:
            assistant(mycommand())
            return command


def assistant(command):
    if 'open reddit python' in command:
        chrome_path = 'C:\\Program Files\\Internet Explorer'
        url = 'https://www.python.org'
        webbrowser.get(chrome_path).open(url)

    if 'what\'s up' in command:
        talktome('chilling bro')
        talktome('im ready for your next command')


while True:
    assistant(mycommand())
