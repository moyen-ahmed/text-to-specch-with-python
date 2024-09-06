from gtts import gTTS
import os
with open('b.txt', 'r') as f:
    a = f.read()
language = 'en'
audio = gTTS(text=a, lang=language, slow=False)
audio.save("b.wav")

if os.name == 'nt':  
    os.system("start b.wav")
elif os.name == 'posix': 
    os.system("afplay b.wav") 

