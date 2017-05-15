# Programmer: Nate Sobol
# Title: Blackjack
# Last Modified: 5/12/17
# File: Blackjack.py

import sys
import re
import tkinter as tkint
import tkinter.messagebox as msgbox
from tkinter import *
from Card import Card
from random import shuffle

class Blackjack(Frame):

    # Declarations
    gameFlag = FALSE
    drawCount = 3
    cardSum = 0
    totalMoney = 1000;
    testList = []
    deckList = []
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    cardValue = ['Ace', '2', '3', '4', '5', '6', '7', '8', 
                  '9', '10', 'Jack', 'Queen', 'King']



    #Constructor
    def __init__(self):
        
        # Frame Initialization
        tkint.Frame.__init__(self)
        self.master.title("Blackjack")
        self.master.geometry("250x300")
        self.pack()
        self.master.configure(bg = "green")
        self.configure(bg = "green")
        
        # Creates Main Menu Bar
        mainMenu = Menu(self.master)
        self.master.config(menu=mainMenu)

        # Creates Submenu Game Action Menu
        actionMenu = Menu(mainMenu, bg = "#80f442")
        mainMenu.add_cascade(label=" Game Action Menu", menu=actionMenu)
        actionMenu.add_command(label="1. Play the Game", command=self.startGame)
        actionMenu.add_command(label="2. Display Available Funds", command=self.displayMoney)
        actionMenu.add_command(label="3. Reset Funds to Zero", command=self.resetMoney)

        # Creates Submenu Quit
        quitMenu = Menu(mainMenu, bg = "#f45f41")
        mainMenu.add_cascade(label="Quit", menu=quitMenu)
        quitMenu.add_command(label="1. Forfiet Current Game", command=self.forfiet)
        quitMenu.add_command(label="2. Quit", command=self.quit)

        # Game Label
        lable = Label(self, text='Your Hand:', bg = "yellow")
        lable.pack()
        
        # Listbox/ScrollBar
        self.deckDisplayListBox = Listbox(self)
        self.deckDisplayListBox.pack(side=RIGHT, fill=Y)
        scrollBar = Scrollbar(self)
        scrollBar.pack(side=RIGHT, fill=Y)
        scrollBar.config(borderwidth = 1, command=self.deckDisplayListBox.yview)
        self.deckDisplayListBox.config(yscrollcommand=scrollBar.set)

        # Button Hit Me
        self.hitMeButton = Button(text="Hit Me", command=self.HitMe, bg = "red")
        self.hitMeButton.config(height=5, width=50)
        self.hitMeButton.pack(side=BOTTOM )

        self.createList()
        


    # Event methods
    # Plays Game
    def startGame(self):
        self.deckDisplayListBox.delete(0, END)
        self.deckList = self.testList[:2]
        if self.gameFlag == FALSE:
            for item in self.deckList:
                self.deckDisplayListBox.insert(END, item)
            self.sumOfCards(self.cardSum)
            self.gameFlag = TRUE
        else:
                self.forfiet()
                self.startGame();

   # Displays Money
    def displayMoney(self):
        msgbox.showinfo("Money ", "You have: $" + str(self.totalMoney))

    # Quits Application
    def quit(self):
        if (msgbox.askyesno("Quit", "Are you sure?")):
            self.destroy()
            sys.exit()

    # Simulates New Card Deal
    def HitMe(self):
        if self.gameFlag == FALSE:
            if (msgbox.askyesno("Start a Game?", "No game Running. \nStart a new game? \nHint: You can start a new game using the menu as well.")):
                self.startGame()
        else:
            self.deckDisplayListBox.insert(END, self.testList[self.drawCount])
            self.cardSum = self.sumOfAllCards(self.cardSum, self.testList[self.drawCount])
            self.checkWin(self.cardSum)
            self.drawCount = self.drawCount + 1

    def forfiet(self):
        if self.gameFlag == FALSE:
            msgbox.showinfo("No game", "You aren't playing a game!")
            return 0
        if (msgbox.askyesno("Forfiet?", "Forfiet game or restart game if already playing?")):
            self.checkWin(0)
    
    # Card Creation Method
    # Creates and fills the Deck List
    def createList(self):
        for i in range(0, 4):
            for k in range(0, 13):
                self.cardList = Card(self.cardValue[k], self.suits[i])
                self.testList.append(self.cardList)
                shuffle(self.testList)
        self.deckList = self.testList[:2]


    # Logic Methods
    # Finds the sum of the first two cards dealt
    def sumOfCards(self, cardSum):
        for card in self.deckList:
            self.cardSum = self.cardSum + int(card.cardValue)   
        self.checkWin(self.cardSum)

    # Determines the sum of all cards on table
    def sumOfAllCards(self, cardTotal, curTotal):
            # first half
            string = str(curTotal).split()[0]

            # Remanipulates Cards
            if string.isdigit():
                    val = int(re.search(r'\d+', string).group())

            if string == 'Jack' or 'Queen' or 'King':
                    val = 10

            if cardTotal >= 22:
                if string == 'Ace':
                    val = 1
            elif cardTotal <= 21:
                if string == 'Ace':
                    val = 11

            totalCardSum = cardTotal + val
            return totalCardSum

    # Resets game to defualt values and shuffles the deck for new round
    def newRound(self):
        shuffle(self.testList)
        self.gameFlag = FALSE
        self.cardSum = 0

    # Resets Money
    def resetMoney():
        var = msgbox.askyesno("Reset Funds", "Are you sure(Y/N)?")
        if var == 1:
            msgbox.showinfo("Money Reset", "Your money has been reset")
            self.totalMoney = 1000
    
    # Validation Method
    # Checks if player has won or lost the game when needed
    def checkWin(self, cardSum):
        if cardSum == 21:
            msgbox.showinfo("You Won!", "You won: $100")
            self.totalMoney += 100
            self.newRound()

        if cardSum > 21:
            msgbox.showinfo("You Lost!", "You lost: $50")
            self.totalMoney -= 50
            self.newRound()

        if cardSum == 0:
            msgbox.showinfo("Forfieted", "You gave up and lost: $50")
            self.totalMoney -= 50
            self.newRound()

        if self.totalMoney <= 0:
            if (msgbox.askyesno("Quit", "You have no money. \nReset money and play again?")):
                self.newRound()
                self.resetMoney()
                

# Main Method
def main():
    Blackjack().mainloop()

if __name__ == '__main__':
    main()
