import os
import platform
import curses
def clear():
    if platform.system()=='Windows':
        os.system('cls')
        return
    os.system('clear')
class Terminal:
    def __init__(self,open=True):
        if open:
            self.open()
    def __del__(self):
        self.close()
    def open(self):
        self.screen=curses.initscr()
        curses.noecho()
        curses.cbreak()
        self.screen.keypad(True)
    def close(self):
        curses.nocbreak()
        self.screen.keypad(0)
        curses.echo()
        curses.endwin()
    def move(self,y,x):
        self.screen.move(y,x)
    def get(self,y,x):
        return chr(self.screen.inch(y,x))
    def set(self,y,x,text):
        self.screen.addstr(y,x,text)
    def wait4key(self):
        char=self.screen.getch()
        if char == curses.KEY_ENTER or char == 10 or char == 13:
            return 'enter'
        elif char == curses.KEY_RIGHT:
            return 'right'
        elif char == curses.KEY_LEFT:
            return 'left'
        elif char == curses.KEY_UP:
            return 'up'
        elif char == curses.KEY_DOWN:
            return 'down'
