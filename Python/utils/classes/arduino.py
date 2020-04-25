from time import sleep
from pySerialTransfer import pySerialTransfer as serial
import string

def split(word): 
    return [char for char in word]  
 
class Arduino:
    door= "COM13" 
    link = ''   

    def __init__(self):
        self.door= "COM13"
        self.link = serial.SerialTransfer(self.door)
        self.link.open()
        print("Initializing...")
        sleep(3)
        print("Ready")

    def __del__(self): 
        self.link.close()

    def read(self):
        
        while 1:
            
            while True:
                while not self.link.available():
                    if self.link.status < 0:
                        print('ERROR: {}'.format(self.link.status))                                            
                
                #print('Response received:')
            
                response = ''
                for index in range(self.link.bytesRead):                   
                    response += chr(self.link.rxBuff[index])
                    
                response=response.replace("\x00", "")
                return(response)

        

    def write(self,string):
        self.link.txBuff=split(string)
        self.link.send(len(string))
        