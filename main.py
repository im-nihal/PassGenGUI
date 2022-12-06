from tkinter import *
import pyperclip
import random

win = Tk() #tkinter object
win.geometry("600x500") #Width and Height of window
win.title("PASSWORD GENERATOR") #Title of Window
win.configure(background='blue')

psk = StringVar() #stores the generated password
psklen = IntVar() #stores length of password
psklen.set(0) #intial length is 6


def gen():
    #storing all the caracters needed
    chars = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
             'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5',
             '6', '7', '8', '9', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_',
             '-', '+', '=', '|', '}', '{', ']', '[', ':', ';', '"', "'", '<', '>', ',', '.',
             '?', '/', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
             'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    password = "" #empty string
    for i in range(psklen.get()):
        password = password + random.choice(chars)
    psk.set(password)


def copy(): #copy mechanism
    ran_psk = psk.get()
    pyperclip.copy(ran_psk)


Label(win, text="Strong Password Generator", font="Jost 20 bold",bg='Blue',fg='white').pack(pady=3)
Label(win, text="Want A Str0ng PassW0rd? U came To Ri8 pLace!", font="Courier 14 italic",bg='Blue',fg='white').pack(pady=3)
Label(win, text="Enter Length of password").pack(pady=3)
Entry(win, textvariable=psklen).pack(pady=3)
Button(win, text="Generate", command=gen).pack(pady=7)
Entry(win, textvariable=psk).pack(pady=3)
Button(win, text="Copy To Clipboard", command=copy).pack()
win.mainloop() #application keeps running unless closed.