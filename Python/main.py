import requests
from utils.classes.card import Card
from utils.classes.arduino import Arduino


if __name__ == '__main__':
  arduino = Arduino()
  try:
    while 1:
      

      card = Card()

      choice =int(input("\n \nType:\n1  to register a new card \n2 to verify if it's registered \n3 to seek its owner info: "))
      print("Awaiting card to be read \n")
      
      while 1:
        arduino.write("verify")
        cardId =arduino.read()

        if cardId != 'no' and cardId !="OK":
          break

      cardExists= card.verify(cardId)

      if choice == 1: 
        if cardExists: 
          print("card already registered")
        else:
          card.register(cardId)
          print("card registered successfully")

      elif choice == 2:
        
        if cardExists:
          print("card already registered")
        else:
          print("card not registered")
      
      elif choice ==3:
        cardUser=card.verifyUse(cardId)
        if cardUser:
           print("This card is owned by ",cardUser)

        else:
          print("This card doesn't have an owner")
        
      

      input("Press ENTER to prossid")
  except KeyboardInterrupt:
        print("\n\nExecution ended by user") 
        del arduino
      
