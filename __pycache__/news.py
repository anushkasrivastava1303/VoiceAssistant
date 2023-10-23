import requests

api_address = "https://newsapi.org/v2/top-headlines?country=us&apiKey=090b8b337f044721afa3595e050a5497"
json_data = requests.get(api_address).json()

ar=[]

def news():
    for i in range(3):
        ar.append("number" + str(i+1) + json_data["articles"][i]["title"]+".")
    return ar   

arr=news()

print(arr)
        
        
         
