# ------------------------- Exercise 9: News Reader  ------------------ #

import requests
import json

urls = 'http://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=dc3d113bd5fb4711bf1ebf5a875cd8b5'
x = requests.get(urls)

data = json.loads(x.text)
# print(data)


# ---------------- For Reading News Paper ------------------ #
def speak(string):
    from win32com.client import Dispatch

    speak = Dispatch("SAPI.SpVoice")

    speak.Speak(string)


if __name__ == '__main__':
    for i in range(10):
        news = data['articles'][i]['title']
        speak(f'News no {i+1} is : {news}')
