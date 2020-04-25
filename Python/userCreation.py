from utils.classes.user import User
from utils.classes.card import Card

if __name__ == '__main__':
    try:
        while 1:
       
            user =User()  
            card = Card()
            userInfo={}
            userInfo["user_name"] = input("Write o user full name: ")
            userInfo["user_nickname"] = input("Write nickname: ")
            userInfo["user_gender"] = input("Write gender: ")
            
            while 1:
                try:
                    #se nao for inteiro, vai gerar erro
                    userInfo['card_id_fk'] = int( input("Write id card : "))
                    
                    #transforma em string para ser analisado
                    userInfo['card_id_fk']= str(userInfo['card_id_fk'])    

                    if not card.verify(userInfo['card_id_fk']):
                        print("\nCard not registered\n")
                    
                    else:

                        if not card.verify(userInfo['card_id_fk']):
                            print("\nCard not registered\n")

                        else: 
                            cardUser =(card.verifyUse(userInfo['card_id_fk']))

                            if cardUser:
                                print("\nthis card is owned by ",cardUser,". Please, write another\n")

                            else:

                                break
                except ValueError:
                    print("\n\nplease, put a integer number")

                        
            if not userInfo["user_nickname"]:
                userInfo["user_nickname"] = None
            if not userInfo["user_gender"]:
                userInfo["user_gender"] = None
            if not userInfo["card_id_fk"]:
                userInfo["card_id_fk"] = None  

            user.register(userInfo)
            print("User registered successfully")
            input("press \'enter\' to register a new user")

    except KeyboardInterrupt:
        print("\n\nExecution ended by user")

