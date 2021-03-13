import pyttsx3  # for Text-to-Speech (tts)
import datetime
import speech_recognition as sr  # Library for performing speech recognition
import wikipedia
import webbrowser
import os
import random
import smtplib


# Dictionary for Gmail Contacts
gmail = {'sherry': 'sheheryark168@gmail.com', 'father': 'saboor.khi@gmail.com',
         'zulqarnain': 'haiderzulfiqarnain@gmail.com'}

# Family Dictionary
family = {'shayan': "Shayan is the Second Brother of Sheheryar's Family.",
          'sheheryar': "Sheheryar is the First child in his Family who is trying to be good son of his Family.",
          'ariyan': 'Ariyan is the second last brother of his family who is some time behaving like fool',
          'umair': "Umair is the cutest child in the world, but some time he behaving like a rude person."}


# Setting code for voice
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    """ Function for speaking """
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    """ Function for greeting my self at particular time """
    hour = int(datetime.datetime.now().hour)

    if 0 <= hour < 12:
        print("Good Morning!")
    elif 12 <= hour < 18:
        print("Good Afternoon!")
    else:
        print("Good Evening!")

    speak("Hi Sherry, I am Jarvis , Please tell me how may i help you.")


def takeCommand():
    """It take microphone user input and returns string output"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening.....')
        r.pause_threshold = 1  # seconds of non-speaking audio before a phrase is considered complete
        audio = r.listen(source)

    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)
        print("Please Say that Again !")
        return "None"

    return query


# For writing commands because i don't have any input for microphone
def writeCommand():
    print('\nListening...')
    user = input("Enter what do you want to do :    ").lower()
    print("Recognizing.....")

    return user


if __name__ == '__main__':
    # speak("I love you sherry")
    wishMe()
    while True:
        # query = takeCommand().lower()
        query = writeCommand().lower()

        # Logic for executing tasks based on query

        # For searching anything on wikipedia
        if 'wikipedia' in query:
            speak('Searching wikipedia....')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        # For opening Youtube
        elif 'open youtube' in query:
            webbrowser.open('youtube.com')

        # For opening Google
        elif 'open google' in query:
            webbrowser.open('google.com')

        # For opening StackoverFlow
        elif 'open stackoverflow' in query:
            webbrowser.open('stackoverflow.com')

        # For Playing Music
        elif 'play music' in query:
            music_dir = 'I:\\Video Songs'
            song = os.listdir(music_dir)
            print(song)
            num = random.randint(0, 26)
            os.startfile(os.path.join(music_dir, song[num]))

        # For getting Current Time
        elif 'current time' in query:
            strTime = datetime.datetime.now().strftime('%H:%M:%S')
            print(f"Sir the time is {strTime}")
            speak(f"Sir he time is {strTime}")

        # For Opening Vs Code
        elif 'open code' in query:
            codePath = "E:\\Software Files\\VS Code\\Microsoft VS Code\\Code.exe"
            print("Opening Vs Code Please wait...")
            speak("Opening Vs Code Please wait...")
            os.startfile(codePath)

        # To Send Email
        elif 'send email' in query:
            try:
                ask = input("Which person you want to send Email:   ").lower()
            except Exception as e:
                print(e)
            else:
                def sendEmail(person, content):
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login('alphasherry10@gmail.com', 'PASSword@786')  # Next time save your password in a
                    # separate  file for security
                    server.sendmail('alphasherry10@gmail.com', person, content)
                    server.close()

                if ask in gmail.keys():
                    speak(f"What Should i Say to {ask}?")
                    content = input("* ")
                    to = gmail[ask]
                    sendEmail(to, content)
                    print("Email has been sent.")
                    speak("Email has been sent .")
                else:
                    print(f"{ask} is not in your Contact List.")
                    speak(f"{ask} is not in your Contact List.")

        # For Opening Telegram
        elif 'open telegram' in query:
            telegramPath = 'E:\\Software Files\\Telegram\\Telegram Desktop\\Telegram.exe'
            print("Opening Telegram Please wait...")
            speak("Opening Telegram Please wait...")
            os.startfile(telegramPath)

        # For Opening Espn Cricket Info
        elif 'open cricket' in query:
            speak("Opening Cricket WebSite.")
            webbrowser.open('espncricinfo.com')

        # For opening Weekly Schedule File
        elif 'weekly schedule' in query:
            speak("Opening Your Weekly Schedule Excel File.")
            filepath = 'H:\\Personal\\Weekly Schedule\\Week 4 (15-2021).xlsx'
            os.startfile(filepath)

        # For opening Chrome
        elif 'open chrome' in query:
            speak("Opening Chrome for You.")
            filepath = '"C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"'
            os.startfile(filepath)

        # For Family Details
        elif 'family' in query:
            ask = input("Enter the name of the Person:  ")
            if ask in family.keys():
                speak(family[ask])
            else:
                speak("Not in List!")

        # For Quitting Jarvis
        elif 'quit' in query:
            print("Quiting Done!")
            speak("By Jani, I am sleeping now...")
            exit()
