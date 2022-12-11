# Imports TKinter library
from tkinter import*            
import tkinter.font       

# Imports GPIO library     
from gpiozero import LED                    
import RPi.GPIO                  
RPi.GPIO.setmode(RPi.GPIO.BCM)  

# Gets current time
import time                     

Led = LED (14)                   

# An interface to the GUI is created
win = Tk()                      
win.title("5.3D Task - Morse Code")  
myFont = tkinter.font. Font(family = 'Helvetica', size = 12, weight = "bold") 

# Morse code for every alphabet
dictionary = { 'A':'.-', 
                   'B':'-...',
                    'C':'-.-.', 
                    'D':'-..', 
                    'E':'.',
                    'F':'..-.', 
                    'G':'--.', 
                    'H':'....',
                    'I':'..', 
                    'J':'.---',
                     'K':'-.-',
                    'L':'.-..',
                     'M':'--', 
                     'N':'-.',
                    'O':'---',
                     'P':'.--.', 
                     'Q':'--.-',
                    'R':'.-.',
                     'S':'...', 
                     'T':'-',
                    'U':'..-', 
                    'V':'...-',
                     'W':'.--',
                    'X':'-..-', 
                    'Y':'-.--', 
                    'Z':'--..',
                    '1':'.----', 
                    '2':'..---', 
                    '3':'...--',
                    '4':'....-', 
                    '5':'.....', 
                    '6':'-....',
                    '7':'--...', 
                    '8':'---..', 
                    '9':'----.',
                    '0':'-----', 
                    ', ':'--..--', 
                    '.':'.-.-.-',
                    '?':'..--..', 
                    '/':'-..-.', 
                    '-':'-....-',
                    '(':'-.--.',
                     ')':'-.--.-'}
ledinput = str()

# Dash function 
def dash():
    Led.on()
    time.sleep(2.0)
    Led.off()
    time.sleep(1)

# Dot function 
def dot():
    Led.on()
    time.sleep(2.5)
    Led.off()
    time.sleep(1)
 
def InputAnalysis(ledinput):
    ledinput = code.get()           

    ledinput = " ".join(dictionary[char] for char in ledinput.upper())
    print(ledinput)     

    for char in ledinput:      
        if char == ".":         
            dot()               

        elif char == "-":       
            dash()             

        elif char == "/" or char == " ":   
            time.sleep(1)

        else:
            print("ERROR! Enter a valid Character.")      

def close():                  
    RPi.GPIO.cleanup()
    win.destroy()

ledButton = Button (win, text = 'Blink name', font = myFont, command = lambda: InputAnalysis(ledinput), bg = 'red', height = 1)     
ledButton.grid (row=1, column=1)                        

code = Entry(win, font=myFont, width=10)                
code.grid(row=0, column=1)                              

exitButton = Button (win, text = 'Exit', font = myFont, command = close, bg = 'aqua', height = 1, width = 6)        
exitButton.grid (row=2, column=1)                       

win.protocol("WM_DELETE_WINDOW", close)        
win.mainloop()                                
