import curses
from curses import wrapper
import time

def start(stdscr):
    stdscr.clear()
    stdscr.addstr("This is a typing speed test!\n")
    stdscr.addstr("\npress any key to start...")
    stdscr.refresh()
    stdscr.getkey()

def display_text(stdscr,target,current,wpm=0):
    stdscr.addstr(target)
    stdscr.addstr(1,0,f"WPM-{wpm}")
    for i,char in enumerate(current):
        correct = target[i]
        color = curses.color_pair(1)
        if char != correct:
            color = curses.color_pair(2)
        stdscr.addstr(0,i,char,color)


def avg_len(text):
    text = text.split()
    count =0
    for words in text:
        count += len(words)
    return round(count/len(text))

def wpm(stdscr):
    text = "if you like this terminal app then share this project with your friends also"
    avg_len_words = avg_len(text)
    writen_text = []
    wpm=0
    s_time=time.time()
    stdscr.nodelay(True)
    while True:
        time_taken = max(time.time() - s_time,1)
        wpm = round(((len(writen_text)/time_taken)*60)/avg_len_words)
        stdscr.clear()
        display_text(stdscr,text,writen_text,wpm)
        stdscr.refresh()
        if len(text) == len(writen_text):
            stdscr.nodelay(False)
            break
        try:
            key = stdscr.getkey()
        except:
            continue
        if ord(key) == 27:
            break
        if key in ("KEY_BACKSPACE" , '\b' ,'\x7f'):
            if len(writen_text) >0:
                writen_text.pop()
        elif len(writen_text) < len(text):
            writen_text.append(key)
        
def main(stdscr):
    curses.init_pair(1,curses.COLOR_GREEN , curses.COLOR_BLACK)
    curses.init_pair(2,curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3,curses.COLOR_WHITE , curses.COLOR_BLACK)
    start(stdscr)
    while True:
        wpm(stdscr)
        stdscr.addstr(3,0,"Test complete ! if want to continue press any key!")
        key = stdscr.getkey()
        if ord(key) == 27:
            break



wrapper(main)



