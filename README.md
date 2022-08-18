# Tacotron-2-Dataset-Creator
This code helps to create dataset for Tacotron-2
- Please read the code, to adjust as per your needs 

## Steps to follow

### Installation
```
pip install -r requirements.txt
```
1. Create Chunks of Audio based on Silence:
```
python chunks_creator.py
```

2. Then create Audio to speech:
```
python tts_converter.py
```
