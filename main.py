# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 22:20:54 2019

@author: Visal Rajeev
"""

from tkinter import *
import tkinter.messagebox
import random


root = Tk()

root.geometry('300x300')
root.title("Stone-Paper-Scissor Game")

msg = Message(root, width='500',text = 'Welcome to the stone-paper-scissor game')
msg.place(x=3, y=3)

def play():
    window = Toplevel(root)
    window.geometry('300x300')
    window.title("Play")
    
    def compute(move):
        action = ['stone','paper','scissor']
        n = random.randrange(0,3)
        
        user = move
        
        if user == 'stone':
            if action[n] == 'stone':
                msg ="It's a draw"
            elif action[n] == 'paper':
                msg ="Computer has won"
            elif action[n] == 'scissor':
                msg ="You have won"
        
        elif user == 'paper':
            if action[n] == 'paper':
                msg ="It's a draw"
            elif action[n] == 'scissor':
                msg ="Computer has won"
            elif action[n] == 'stone':
                msg ="You have won"
        
        elif user == 'scissor':
            if action[n] == 'scissor':
                msg ="It's a draw"
            elif action[n] == 'stone':
                msg ="Computer has won"
            elif action[n] == 'paper':
                msg ="You have won"
        
            else:
                msg = "You have entered wrong move"
        
        tkinter.messagebox.showinfo("Result", msg)     
        
        
    stone = Button(window, height=3, width=10, text='Stone', command=lambda:compute('stone'), bg='brown')
    stone.place(x=10, y=50)
    
    scissor = Button(window, height=3, width=10, text='Scissor', command=lambda:compute('scissor'), bg='cyan')
    scissor.place(x=100, y=50)
    
    paper = Button(window, height=3, width=10, text='Paper', command=lambda:compute('paper'), bg='white')
    paper.place(x=200, y=50)
    
    close = Button(window, height=3, width=10, text='Close', command=window.destroy,bg='red')
    close.place(x=110, y=120)
    
        
    
def instruction():
    
    window = Toplevel(root)
    window.geometry('500x300')
    window.title("Instruction")
    
    msg = Message(window, width='500',text = 'Instruction to play the game')
    msg.place(x=3, y=3)
    
    a = "1.The game is played between a bot and user(ie. you)"
    b = "2.There are total 3 moves that are Stone, Paper and Scissor"
    c = "3.During each match both the player will one move"
    d = "4.In oreder to win a match player should make moves on the left side of the list"
    e = ".4.1.Stone > Scissor \n Scissor > Paper \n Paper > Stone "
    f = "5.If both player make same move then it's a draw"
    
    msg1 = Message(window, width='1000',text = a)
    msg1.place(x=3, y=30)
    msg2 = Message(window, width='1000',text = b)
    msg2.place(x=3, y=60)
    msg3 = Message(window, width='1000',text = c)
    msg3.place(x=3, y=90)
    msg4 = Message(window, width='1000',text = d)
    msg4.place(x=3, y=120)
    msg5 = Message(window, width='1000',text = e)
    msg5.place(x=3, y=150)
    msg6 = Message(window, width='1000',text = f)
    msg6.place(x=3, y=220)
    
    close= Button(window, height=2, width=20, text='Close', command=window.destroy,bg='red')
    close.place(x=80, y=250)

b0 = Button(root, height=2, width=20, text='Play', command=lambda:play(), bg='yellow')
b0.place(x=50, y=50)

b1 = Button(root, height=2, width=20, text='Instructions', command=lambda:instruction(),bg='yellow')
b1.place(x=50, y=100)

close = Button(root, height=2, width=20, text='Close', command=root.destroy,bg='red')
close.place(x=50, y=150)

root.mainloop()
