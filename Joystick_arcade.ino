const byte PIN_BUTTON_SELECT = 2; 
const byte PIN_BUTTON_RIGHT = 3;
const byte PIN_BUTTON_UP = 4;
const byte PIN_BUTTON_DOWN = 5;
const byte PIN_BUTTON_LEFT = 6;


void setup()
{
  Serial.begin(9600);// Begin the serial monitor at 9600bps
 pinMode(PIN_BUTTON_UP, INPUT);  
  digitalWrite(PIN_BUTTON_UP, HIGH);
  
  pinMode(PIN_BUTTON_DOWN, INPUT);  
  digitalWrite(PIN_BUTTON_DOWN, HIGH);
}


void loop()
{
  if (digitalRead(PIN_BUTTON_DOWN)==LOW)
  {
   Serial.println("DOWN"); 
    
  }
  if (digitalRead(PIN_BUTTON_UP)==LOW)
  {
   Serial.println("UP"); 
  }
  delay(100);
}
