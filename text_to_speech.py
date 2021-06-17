from gtts import gTTS
import os

mytext="This is Hari Krishna from Telanaga and studied from srm duting 2018 to 2022"

language = 'en'

output=gTTS(text=mytext,lang=language,slow=False)

output.save("output.mp3")

os.system("start output.mp3")
