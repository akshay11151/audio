import speech_recognition as sr
import os
import datetime
import requests

def transcribe_audio(file_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(file_path) as source:
        audio_text = recognizer.recognize_google(source)
    return audio_text.lower()

def categorize_text(audio_text):
    if 'idea' in audio_text.split() or 'suggestion' in audio_text.split():
        return 'ideas'
    elif 'hate' in audio_text.split() or 'anger' in audio_text.split() or 'illogical' in audio_text.split() or 'simping' in audio_text.split():
        return 'behavioral improvements'
    else:
        return 'casual talk'

def upload_file_to_drive(file_path):
    upload_url = 'https://www.example.com/upload'
    with open(file_path, 'rb') as f:
        r = requests.post(upload_url, files={'file': f})
    if r.status_code == 200:
        print('File uploaded successfully')
    else:
        print('Failed to upload file')

def main():
    while True:
        time_now = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        file_path = f'{time_now}.wav'
        print(f'Recording started at {time_now}')
        os.system(f'rec -c 1 -r 16000 {file_path} silence 1 0.1 1% 1 2.0 1%')
        print(f'Recording stopped at {datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}')
        audio_text = transcribe_audio(file_path)
        print(f'Transcribed text: {audio_text}')
        category = categorize_text(audio_text)
        print(f'Category: {category}')
        if category != 'casual talk':
            upload_file_to_drive(file_path)
        os.remove(file_path)

if __name__ == '__main__':
    main()
