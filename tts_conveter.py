#import library
import os
import glob
import speech_recognition as sr

#Configs
folder_name = 'splitAudio'
chunk_size = 10
txt_file_name = 'list.txt'



# Initialize recognizer class (for recognizing the speech)
r = sr.Recognizer()

# Google Cloud creds
#GOOGLE_CLOUD_SPEECH_CREDENTIALS = r"""{}"""

print('Converting audio transcripts into text ...')

file = open(txt_file_name, 'w')

for i in range(chunk_size):
    audio_file = str(i)+".wav"
    with sr.AudioFile('{}/{}'.format(folder_name,audio_file)) as source:
        audio_text = r.listen(source)
        try:

            # if you want to try free Speech to text use this code:
            text = r.recognize_google(audio_text)
            file.write("wavs/{}".format(audio_file)+"|"+text+".\n")

            # gloogle cloud is paid
            # text = r.recognize_google_cloud(audio_text, credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS)
            # file.write("wavs/{}".format(audio_file)+"|"+text+".\n")
            print(audio_file," : ",text)

        except sr.UnknownValueError:
            print("Google Cloud Speech could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Cloud Speech service; {0}".format(e))
file.close()