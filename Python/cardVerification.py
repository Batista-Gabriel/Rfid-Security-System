from utils.classes.arduino import Arduino
from utils.classes.card import Card

if __name__ == '__main__':
    try:
        arduino = Arduino()
        card=Card()
        while 1:
            arduino.write("verify")
            cardId= arduino.read()
            #print(cardId)
            if cardId != 'no' and cardId != 'ok':  
                cardUser =(card.verifyUse(cardId))
                if cardUser:
                    print("Welcome, "+ cardUser)
                    arduino.write("confirmed")
                    arduino.read()
                else:
                    print("User/card not registered") 

    except KeyboardInterrupt:
        print("\n\nEnded by user")





        
 