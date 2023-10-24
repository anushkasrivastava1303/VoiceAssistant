import requests

api_address = "https://newsapi.org/v2/top-headlines?sources=google-news-in&apiKey=090b8b337f044721afa3595e050a5497"
json_data = requests.get(api_address).json()

ar=[]

def news():
    for i in range(5):
        ar.append("number " + str(i+1) + " , " + json_data["articles"][i]["title"]+".")
    return ar   




        