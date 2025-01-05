import random

class Cards:
    def __init__(self, name, value, suit):
        self.name=name
        self.value=value
        self.suit=suit
    def display(self):
        print(self.name,"of",self.suit+",",self.value)

#def shuffle(deck):
    #for i in 


def main():
    deck=[]
    names=["Jack","Queen","King"]
    suit=["Spade","Club","Diamond","Hearts"]
    for i in range(13):
        for j in range(4):
            if (i<9):
                name=str(i+2)
                value=i+2
            elif (i>8 and i<12):
                name=names[i-9]
                value=10
            else:
                name="Ace"
                value=11
            card=Cards(name,value,suit[j])
            deck.append(card)
    for i in range(52):
        deck[i].display()
    
    

main()
