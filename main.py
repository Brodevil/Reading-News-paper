"""
Akhbar padh kr sunno, From the newapi.org We are getting the frest top news and then using the pywin32 are makint the python to speack it
"""
def speak(str):

    from win32com.client import Dispatch
    speak = Dispatch("SAPI.Spvoice")
    speak.speak(str)


def news_api(apikey):
    import json
    import requests
    response = requests.get("https://newsapi.org/v2/top-headlines?"
                            "country=in&"   # As per your country you can just change the contry short name, For Example > India >in. Write it this way "country={your_country_short_name}&"
                            f"apiKey={apikey}")

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
        
