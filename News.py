import requests
from ss import *
key="2b8f0e5b70ad419c9d09b9ade42f9e9b"
api_address = 'https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey='+key
json_data=requests.get(api_address).json()
ar=[]
def news():
    for i in range(6):
        ar.append("Number "+str(i+1)+", "+json_data["articles"][i]["title"]+".")

    return ar

