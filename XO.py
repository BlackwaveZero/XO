import random
import time
from terminal import *
map='----- ----- -----'+'\n'+'' \
    '|   | |   | |   |'+'\n' \
    '----- ----- -----'+'\n'+'' \
    '|   | |   | |   |'+'\n' \
    '----- ----- -----'+'\n'+'' \
    '|   | |   | |   |'+'\n' \
    '----- ----- -----'+'\n'
while True:
    clear()
    print ('1.play')
    print ('2.exit')
    command=input(':>')
    if command=='play' or command=='1':
        clear()
        player1=input('Player 1 name :')
        player2=input('Player 2 name :')
        result=''
        clear()
        turn=0
        terminal=Terminal()
        x=2
        y=1
        terminal.set(0,0,map)
        while True:
            key=terminal.wait4key()
            if turn%2==1:
                terminal.set(10, 0, 'player '+player1+' (X) turn ')
            else:
                terminal.set(10, 0, 'player '+player2+' (O) turn ')
            if key=='enter':
                if terminal.get(y,x)==' ':
                    if turn%2==1:
                        terminal.set(y,x,'X')
                        terminal.move(y,x)
                    else:
                        terminal.set(y,x,'O')
                        terminal.move(y,x)
                    condition=(terminal.get(1,2)==terminal.get(1,8)   and terminal.get(1,8)==terminal.get(1,14) and terminal.get(1,14)!=' '  )    or \
                            (terminal.get(3,2)==terminal.get(3,8)   and terminal.get(3,8)==terminal.get(3,14)  and terminal.get(3,14)!=' ')    or \
                            (terminal.get(5,2)==terminal.get(5,8)   and terminal.get(5,8)==terminal.get(5,14)  and terminal.get(5,14)!=' ')    or \
                            (terminal.get(1,2)==terminal.get(3,2)   and terminal.get(3,2)==terminal.get(5,2)   and terminal.get(5,2)!=' ')    or \
                            (terminal.get(1,8)==terminal.get(3,8)   and terminal.get(3,8)==terminal.get(5,8)   and terminal.get(5,8)!=' ')    or \
                            (terminal.get(1,14)==terminal.get(3,14) and terminal.get(3,14)==terminal.get(5,14) and terminal.get(5,14)!=' ')    or \
                            (terminal.get(1,2)==terminal.get(3,8)   and terminal.get(3,8)==terminal.get(5,14)  and terminal.get(5,14)!=' ')    or \
                            (terminal.get(1,14)==terminal.get(3,8)  and terminal.get(3,8)==terminal.get(5,2)   and terminal.get(5,2)!=' ')
                    if condition:
                        if turn%2==1:
                            result='player '+player1+' (X) has won !!!! '
                        else:
                            result= 'player '+player2+' (O) has won !!!! '
                        break
                    elif turn==8:
                        result= 'Tie game !!!'
                        break
                    turn+=1
            elif key=='right':
                if x==14:
                    continue
                x+=6
                terminal.move(y,x)
            elif key=='left':
                if x==2:
                    continue
                x-=6
                terminal.move(y,x)
            elif key=='up':
                if y==1:
                    continue
                y-=2
                terminal.move(y,x)
            elif key=='down':
                if y==5:
                    continue
                y+=2
                terminal.move(y,x)
        terminal.close()
        clear()
        print (result)
        for i in range(1,6):
            print ( '.',flush=True,end='')
            time.sleep(1)
    elif command=='2' or command=='exit':
        break
    else:
        print ('invalid command')
        input('press enter to continue...')
