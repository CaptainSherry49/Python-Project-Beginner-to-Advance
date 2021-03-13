import os
import pandas as pd
from pydub import AudioSegment
from gtts import gTTS


def text_to_speech(text, filename):
    my_text = str(text)
    language = 'hi'
    my_obj = gTTS(text=my_text, lang=language, slow=False)
    my_obj.save(filename)


def merge_audios(audios):
    """ This function returns pydub audio segment """
    combined = AudioSegment.empty()
    for audio in audios:
        combined += AudioSegment.from_mp3(audio)
    return combined


def generate_skeleton():
    """ This function will generate audio from given mp3 """
    audio = AudioSegment.from_mp3("railway.mp3")

    # 1 - Generate Kripiya dehan dejiya
    start = 20000  # in milliseconds
    finish = 21300  # in milliseconds
    audio_process = audio[start: finish]
    audio_process.export('1_Hindi.mp3', format='mp3')

    # 2 train no. train name & is form-city

    # 3 - Generate k rasta
    start = 27400  # in milliseconds
    finish = 28000  # in milliseconds
    audio_process = audio[start: finish]
    audio_process.export('3_Hindi.mp3', format='mp3')

    # 4 - to-City

    # 5 - Generate ko jana wali apna nirdharit sama
    start = 28800  # in milliseconds
    finish = 31800  # in milliseconds
    audio_process = audio[start: finish]
    audio_process.export('5_Hindi.mp3', format='mp3')

    # 6 - Time

    # 7 - Generate Par platform number
    start = 34200  # in milliseconds
    finish = 36000  # in milliseconds
    audio_process = audio[start: finish]
    audio_process.export('7_Hindi.mp3', format='mp3')

    # 8 - Platform number

    # 9 - Generate sa jay gi
    start = 36600  # in milliseconds
    finish = 37600  # in milliseconds
    audio_process = audio[start: finish]
    audio_process.export('9_Hindi.mp3', format='mp3')


def generate_announcement(filename):
    df = pd.read_excel(filename)
    print(df)
    for index, item in df.iterrows():

        # 2 Generate train no. train name & is form-city
        text_to_speech(str(item['train_no']) + ' ' + item['train_name'] + ' ' + item['from'], '2_hindi.mp3')

        # 4 - Generate to-City
        text_to_speech(item['to'], '4_hindi.mp3')

        # 6 - Generate Time
        text_to_speech(item['time'], '6_hindi.mp3')

        # 8 - Generate Platform number
        text_to_speech(item['platform'], '8_hindi.mp3')

        audios = [f"{i}_hindi.mp3" for i in range(1, 10)]
        announcement = merge_audios(audios)
        announcement.export(f"announcement_{index +  1}.mp3", format='mp3')


if __name__ == '__main__':
    print("Generating Skeleton...")
    generate_skeleton()
    print("Now generating Announcement...")
    generate_announcement("railway_announcement.xlsx")
