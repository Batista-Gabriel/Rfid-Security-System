import requests
class User:
  user_id =''
  user_name = ''
  user_nickname= ''
  user_gender= ''
  card_id_fk = ''
  baseUrl ="http://localhost:3000/user/"

  def alterUser(self):
  
    self.user_name = input("Digite o nome do usuario: ")
    self.user_nickname = input("Digite o apelido: ")
    self.user_gender = input("Digite o genero: ")
    self.card_id_fk = input("Digite o id do cartao: ")
    
    info={"user_name":self.user_name, "user_nickname": self.user_nickname,
      "user_gender":self.user_gender, "card_id_fk": self.card_id_fk}
    print(info)

    requests.patch(self.baseUrl, data = info)

  def register(self,dict):
      info={"user_name":dict["user_name"], "user_nickname":dict["user_nickname"],
      "user_gender":dict["user_gender"], "card_id_fk": dict["card_id_fk"]}   
      response = requests.post(self.baseUrl, data = info) 
      return response.text    

  def verifyUser(self,info): #pode usar como parametro o nome ou id
    
    if type(info) is str:
      url = self.baseUrl + 'byname/' + info
    elif type(info) is int:
      url = self.baseUrl + str(info)
    else:
      return 0
     
    response = requests.get(url)
    if response.json(): 
            return response.text

    return 0

