# Exercise 9 tut 84 CWH Python

# akhbaar padhke sunao
# newsapi.org
# install pywin32 module

import requests
import json

def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)

if __name__ == "__main__":
    speak("Top news for today...")
    url = "https://newsapi.org/v2/top-headlines?country=us&apiKey=9bb76e125d034f3e8074ca55a5d4e623"
    news_dict = requests.get(url).text
    news_dict = json.loads(news_dict)
    arts = news_dict['articles']
    for article in arts:
        speak(article['title'])
        print(article['title'])
        print(article['url'])
        print("")
        speak("Moving on to the next news...")