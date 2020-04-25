
#include "SerialTransfer.h" //serial communication
#include <MFRC522.h> //rfid

#define SS_PIN 10
#define RST_PIN 9
#define opendoor 3
#define incomingmessage 5 //led that will blink if our arduino is receiving any message

#define enoughtime 5000 //the same card won't get a response unless this amount of time has been passed


SerialTransfer message;
MFRC522 rfid(SS_PIN, RST_PIN);

byte nuidPICC[4];


unsigned long lastTime = 0;
unsigned long now;

void setup()
{
  Serial.begin(115200);
  message.begin(Serial);
  SPI.begin();
  rfid.PCD_Init();

  pinMode(opendoor, OUTPUT);
  digitalWrite(opendoor, LOW);

  pinMode(incomingmessage, OUTPUT);
  digitalWrite(incomingmessage, LOW);
}

void loop()
{
  String str = "";
String conteudo = "";
  if (message.available())
  {
    digitalWrite(incomingmessage, HIGH);
    for (uint16_t i = 0; i < message.bytesRead; i++)
      str.concat( String (char( message.rxBuff[i])));// setting the message into a string

  }

  digitalWrite(incomingmessage, LOW);

  if (str == "verify") {

    do {
      // seek new cards
      if ( ! rfid.PICC_IsNewCardPresent()) { //if none found

        now = millis();
        if (now - lastTime >= enoughtime) { //reset last card nuid
          for (int i = 0; i < 4; i++)
            nuidPICC[i] = 0;
 
        }
        message.txBuff[0] = 'n';
        message.txBuff[1] = 'o';
        message.sendData(2);
        delay(200);
        return;
      }
      // select a card
      if ( ! rfid.PICC_ReadCardSerial()) {
        return;
      }
      //check if last card is different than the newest
      if (rfid.uid.uidByte[0] != nuidPICC[0] ||
          rfid.uid.uidByte[1] != nuidPICC[1] ||
          rfid.uid.uidByte[2] != nuidPICC[2] ||
          rfid.uid.uidByte[3] != nuidPICC[3] ) {
        for (byte i = 0; i < 4; i++) {
          nuidPICC[i] = rfid.uid.uidByte[i];
        }
        //get this card data into a string
        for (byte i = 0; i < rfid.uid.size; i++) {
          conteudo.concat(String(rfid.uid.uidByte[i] < 0x10 ? "0" : ""));
          conteudo.concat(String(rfid.uid.uidByte[i], DEC));
        }

        if (conteudo.length() < 11)
          conteudo.concat(String("0"));

        conteudo.toCharArray(message.txBuff, conteudo.length());
        message.sendData(conteudo.length()); //send data thru serial comuinication
        lastTime = now;
        break;

      }

    } while (1);

  } if (str == "confirmed") {
    digitalWrite(opendoor, HIGH);

    message.txBuff[0] = 'o';
    message.txBuff[1] = 'k';
    message.sendData(2);
    delay(1000);
    digitalWrite(opendoor, LOW);

    delay(200);
  }
}