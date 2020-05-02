clear()
clears the screen its cross-platform

-----------------------------------------------
for using it first initialize the object : 

terminal = Terminal()

------------------------------------------------
moving cursor : 

terminal.move(y,x) #dont use this and then use print use terminal.set

------------------------------------------------
getting a character of terminal : 
!! returns the character that is in y x coordinate

terminal.get(y,x)

------------------------------------------------
setting a string in terminal : 
!! it moves the curser to the y x coordinate and then pritns str

terminal.set(y,x,str)

------------------------------------------------
keyPressed : 
how to detect if a key is pressed

terminal.keyPressed([optional=False])

it returns this : 
enter
right
left
up down

if the optional arguments is set to True it returns the decimal of the pressed key

exapmle:

while True:
    keyPressed=terminal.keyPressed() #getting the pressed key
    clear() # clearing the screen
    terminal.set(0,0,keyPressed) # shows which key is pressed
    if(keyPressed=='enter'):
        break
