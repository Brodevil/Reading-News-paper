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


def readable(news):
    for i in range(10):
        if i+1 == 1:
            result = f"{i+1}st News is. Title; {news['articles'][i]['title']}. \nDiscription; {news['articles'][i]['description']}.Actually; {news['articles'][i]['content']}.\nHere the {i+1}st news ended.\n\n"
            yield result
        elif i+1 == 2:
            result = f"{i+1}nd News is. Title; {news['articles'][i]['title']}. \nDiscription; {news['articles'][i]['description']}.Actually; {news['articles'][i]['content']}.\nHere the {i+1}nd news ended.\n\n"
            yield result
        elif i+1 == 3:
            result = f"{i+1}rd News is. Title; {news['articles'][i]['title']}. \nDiscription; {news['articles'][i]['description']}.Actually; {news['articles'][i]['content']}.\nHere the {i+1}rd news ended.\n\n"
            yield result
        else:
            result = f"{i+1}th News is. Title; {news['articles'][i]['title']}. \nDiscription; {news['articles'][i]['description']}.Actually; {news['articles'][i]['content']}.\nHere the {i+1}th news ended.\n\n"


if __name__ == "__main__":
    top_ten = news_api()    # Enter your API key as the argument
    news = readable(top_ten)
    for i in tuple(news):
        speak(i)
