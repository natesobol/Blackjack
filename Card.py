# Programmer: Nate Sobol
# Title: Blackjack
# Last Modified: 5/12/17
# File: Card.py
# Simple Class that initially manipulates the values of the deck upon creation of the list

class Card():

    # Constructor
    def __init__(self, cardIndex, suitIndex):
        
        # Declaration
        self.cardIndex = cardIndex
        self.suitIndex = suitIndex

        # Initial Manipulation
        if cardIndex.isdigit():
            self.cardValue = cardIndex
        if cardIndex == 'Ace':
            self.cardValue = '11'
        else:
            self.cardValue = '10'
    
    # String Formatting Method
    def __str__(self):
        return "%s of %s " % (self.cardIndex, self.suitIndex)