from plyer import notification  # To make a Notification function
import requests  # For collecting data
from bs4 import BeautifulSoup
from time import sleep


def notify_me(title, message):
    notification.notify(
        title=title, message=message,
        app_icon='J:\\Code With Harry\\Python using Pycharm\\Python Projects'
                 '\\Real-Time Corona virus Notification System\\virus.ico',
        timeout=10,
    )


def get_data(url):
    data = requests.get(url)
    return data.text


if __name__ == '__main__':
    my_html_data = get_data('https://www.worldometers.info/coronavirus/country/pakistan/')

    soup = BeautifulSoup(my_html_data, 'html.parser')
    # print(soup.prettify())
    covid = ''
    for text in soup.find_all('title'):
        covid = text.get_text()
    # print(ds)
    notify_me('Covid-19', f"{covid[:-12]}")
    sleep(5)
