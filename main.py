"""
Akhbar padh kr sunno, From the newapi.org We are getting the frest top news and then using the pywin32 are makint the python to speack it
"""
import json
import requests
from win32com.client import Dispatch


def speak(str):
    speak = Dispatch("SAPI.Spvoice")
    speak.speak(str)


def news_api( apikey, url="https://newsapi.org/v2/top-headlines?sources=the-times-of-india&apikey=96926ea85ee242508e5527e0891be103"):
    
    if url == "https://newsapi.org/v2/top-headlines?sources=the-times-of-india&apikey=96926ea85ee242508e5527e0891be103":
        response = requests.get("https://newsapi.org/v2/top-headlines?"
                                "sources=the-times-of-india&"
                                f"apiKey={apikey}")
    else:
        response = requests.get(url)

    json_data = json.loads(response.text)
    return json_data


if __name__ == "__main__":
    top_ten = news_api()    # we have the acces to put the URL and our API key, Default link is also avalable 
    arts = top_ten['articles']
    for articles in arts:
        print(f"Title: {articles['title']}. \nDiscription: {articles['description']}. Actually: {articles['content']}\nFor more info... Go to ==>>> {articles['url']}\n")
        speak(f"Title; {articles['title']}. \nDiscription; {articles['description']}. Actually; {articles['content']}\n")
        speak("Moving On next news!")
    speak("Thank you for listening")
              
 # how does the program is if you think you can best feel free to pull requests
