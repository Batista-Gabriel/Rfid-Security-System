import requests
import json
class Card:
    card_id=''
    baseUrl = ""

    def __init__(self):
        self.baseUrl = "http://localhost:3000/card/"

    def register(self,card_id):
        card_id.rstrip('\x00')
        self.card_id =card_id
        info={ "card_id": self.card_id}
        response = requests.post(self.baseUrl, data = info) 
        return response.text   
        
    def verify(self,card_id):
        self.card_id =card_id
        url = self.baseUrl + self.card_id
        response = requests.get(url)
        if response.json(): 
            return response.text

        return 0     

    def verifyUse(self,card_id):
        self.card_id =card_id
        url = self.baseUrl+ "thiscarduser/" + self.card_id
        response = requests.get(url)
        if response.json(): 
            return (json.loads(response.text))[0].get('user_nickname')#get first nickname inside of list of dict
 
        return 0     

