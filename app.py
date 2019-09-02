import speech_recognition as sr
from os import path
from pprint import pprint

r = sr.Recognizer()

############################## Listening From Microphone ##################################

with sr.Microphone() as src:
    print("Speak Something!")
    
    audio = r.listen(src)

############################## printing what you said ##################################

try:
    text = r.recognize_google(audio)
    print("You Said: {}".format(text))

except:
    print("Sorry! Couldn't Hear You.")

########################## saving wav file of what you said #############################
with open("recorded.wav", "wb") as f:
    f.write(audio.get_wav_data())

########################## Now reading from your audio file #############################

file = path.join(path.dirname(path.realpath(__file__)), "recorded.wav")

with sr.AudioFile(file) as wav_file:
    audio = r.record(wav_file)

try:
    text = r.recognize_google(audio, show_all=True)
    pprint(text)
except:
    print("Sorry! Couldn't Hear You.")
