from time import sleep
from pySerialTransfer import pySerialTransfer as serial
import string

import sys

def split(word): 
    return [char for char in word]  
 
class Arduino:

    def __init__(self,door):
        try:
            print("Initializing...")
            self.door= door
            self.link = serial.SerialTransfer(self.door)
            self.link.open()
            sleep(3)
            print("Ready")
            self.error = False
        except Exception as e:
            self.error = True

    def __del__(self): 
        if (not self.error):
            self.link.close()

    def read(self):
        
        while 1:
            
            while True:
                while not self.link.available():
                    if self.link.status < 0:
                        print('ERROR: {}'.format(self.link.status))                                            
                
            
                response = ''
                for index in range(self.link.bytesRead):                   
                    response += chr(self.link.rxBuff[index])
                    
                response=response.replace("\x00", "")
                return(response)

        

    def write(self,string):
        self.link.txBuff=split(string)
        self.link.send(len(string))
        