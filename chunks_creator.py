from pydub import AudioSegment
from pydub.silence import split_on_silence


# Parameters to set
req_chunks = 10
sound_file = AudioSegment.from_wav("main_data.wav")


audio_chunks = split_on_silence(sound_file, 
    silence_thresh=-40, min_silence_len=100, keep_silence=100)

numChunks=len(audio_chunks)
print("{} Audio Chunks Found! ".format(numChunks))

for i, chunk in enumerate(audio_chunks):
    if i == req_chunks:
        print("Limit Reached,Sucessfully created {} audio files!".format(req_chunks))
        break
    out_file = ".//splitAudio//{0}.wav".format(i)
    print("exporting", out_file)
    chunk.export(out_file, format="wav")
print('Done!')