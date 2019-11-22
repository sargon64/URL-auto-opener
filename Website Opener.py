import webbrowser as webb
import os
import sys
import time

running = bool(True)
URL = input('Enter Starting URL:')
URLstring = str(" ")
URLstring = [str(URLstring) for URLstring in input("Enter multiple value: ").split()]
ValNum = int(input('Input the numper of values: '))
Valstr = str(ValNum)
print("Number of list is: ", URLstring)
Type = int(-1)
URLdecomp = str('')
FullURL = ''
Safety = False
Pos = str('Y')

webb.open('https://google.com/', new=1)

while Safety == False:
    Safeteytoken = input('You are about to open' + Valstr + 'tabs are you sure you want to do so? (Y/N): ')
            
    if Safeteytoken == Pos:
        Safety = True

if Safety:

    while running:
        time.sleep(1)
    
        Type += 1

        if Type < ValNum:
            URLdecomp = URLstring[Type]
    
        if Type == ValNum:
            running = bool(False)

        URLdecomp = str(URLdecomp)
        FullURL = URL + URLdecomp
    
        print(URLdecomp)

        webb.open_new(FullURL)





