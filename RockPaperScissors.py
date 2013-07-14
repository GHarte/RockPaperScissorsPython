#author: Gareth Harte

import sys
from tkinter import *
import tkinter.messagebox

from random import randrange
root = Tk()
root.geometry('300x150+0+0')
playerChoice = StringVar(None)
result = StringVar(None)
win = 'You win'
tie = 'Its a tie!'
lose = 'You lose'

scissorsgif = PhotoImage(file="scissors.gif")
papergif = PhotoImage(file="paper.gif")
stonegif = PhotoImage(file="stone.gif")

def Rock():
    CPUChoice = randrange(3)
    playerChoice = '1'
    if playerChoice == '1' and CPUChoice == 0:
        result = tie
        resultText.set('You and the CPU both picked rock. ' + result)
        
    if playerChoice == '1' and CPUChoice == 1:
        result = lose
        resultText.set('Paper beats rock. ' + result)
        
    if playerChoice == '1' and CPUChoice == 2:
        result = win
        resultText.set('Rock smashes scissors. ' + result)

def Paper():
    CPUChoice = randrange(3)
    playerChoice = '2'
    if playerChoice == '2' and CPUChoice == 0:
        result = win
        resultText.set('Paper beats rock. ' + result)
        
    if playerChoice == '2' and CPUChoice == 1:
        result = tie
        resultText.set('You and the CPU both picked paper ' + result)
        
    if playerChoice == '2' and CPUChoice == 2:
        result = lose
        resultText.set('Scissors cuts up paper. ' + result)

def Scissors():
    CPUChoice = randrange(3)
    playerChoice = '3'
    if playerChoice == '3' and CPUChoice == 0:
        result = lose
        resultText.set('Rock smashes scissors. ' + result)
        
    if playerChoice == '3' and CPUChoice == 1:
        result = win
        resultText.set('Scissors cuts up paper. ' + result)
        
    if playerChoice == '3' and CPUChoice == 2:
        result = tie
        resultText.set('You and the CPU both picked scissors. ' + result)


    

widgetRock = Button(root, command=Rock, width=40, height=35, image=stonegif)
widgetRock.place(x=25,y=10)

widgetPaper = Button(root, command=Paper, width=40, height=35, image=papergif)
widgetPaper.place(x=125,y=10)

widgetS = Button(root, command=Scissors, width=40, height=35, image=scissorsgif)
widgetS.place(x=225,y=10)

resultText = StringVar()
resultText.set("Go!")
widgetResult = Label(root, textvariable=resultText, width = 42)
widgetResult.place(x=0, y=70)

widgetE = Button(root, text='End Game', command=quit, width=20)
widgetE.place(x=75, y=110)

root.title('Rock, Paper, Scissors!')
root.mainloop()

"""
Copyright 2013 Gareth Harte
 
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
 
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
 
See <http://www.gnu.org/licenses/> for a copy of the GNU General Public License.
"""
