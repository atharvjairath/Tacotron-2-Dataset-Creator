#import library
import os
import glob
import speech_recognition as sr

# Initialize recognizer class (for recognizing the speech)
r = sr.Recognizer()

# Google Cloud creds
#GOOGLE_CLOUD_SPEECH_CREDENTIALS = r"""{}"""

print('Converting audio transcripts into text ...')
basepath = 'splitAudio/'

file = open('list.txt', 'w')
for i in range(201):
    audio_file = str(i)+".wav"
    with sr.AudioFile('splitAudio\{}'.format(audio_file)) as source:
        audio_text = r.listen(source)
        try:
            # if you want to try free Speech to text use this code:
            # file.write("wavs/{}".format(entry)+"|"+ r.recognize_google(audio_text)+".\n")

            text = r.recognize_google_cloud(audio_text, credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS)
            file.write("wavs/{}".format(audio_file)+"|"+text+".\n")
            print(audio_file," : ",text)
        except sr.UnknownValueError:
            print("Google Cloud Speech could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Cloud Speech service; {0}".format(e))
file.close()