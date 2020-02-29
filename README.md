# XO
how to use terminal

from terminal import *
--------------------
terminal=Terminal()
terminal.open()
###your code###
terminal.close()
------------------------------------------
clear() this function clears the screen but terminal should be closed 
#terminal.close()
---------------------------------------------
terminal.move(y,x) # it goes to the y and x coordinates
terminal.get(y,x) # it gets the char in y and x coordinate
terminal.set(y,x,text) #it print a text in y and x coordinate
terminal.wait4key() # it returns press key on the keyboard
#enter right left up down
#you can use this to identify the movement and then use the terminal.move() or terminal.set() or terminal.get()
