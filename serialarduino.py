import serial
import time
port="/dev/ttyUSB0"
#print('hello world')
bluetooth= serial.Serial(port,9600)
#print ('hello world 2')
bluetooth.flushInput()
#print ('hello world 3')
inputs=""
while True:
        #print("we are in the for loop")
        inputsp=bluetooth.readline().rstrip()
        
        #for letter in inputsp:
         #      inputs=inputs+ str(letter)
        print inputsp      
        if inputsp=="DOWN":
            print "APPLES"
        #else:
         #       print "oranges"
        if inputsp =="UP":
            print "Bannana"
exit()
