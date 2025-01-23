import random
import socket
import threading
import json





class Cards:
    
    def __init__(self, name, value, suit):
        self.__name=name
        self.__value=value
        self.__suit=suit
    
    def getvalue(self):
        return self.__value
        
    def display(self):
        print(self.__name,"of",self.__suit+",",self.__value)
        
    def sname(self):
        return self.__name+" of "+self.__suit





class Person:
    
    def __init__(self,name="",hp=1000,hand=[]):
        self.__name=name
        self.__hp=hp
        self.__hand=hand

    def getname(self):
        return self.__name
    
    def gethand(self):
        return self.__hand

    def sethand(self,hand):
        self.__hand=hand

    def stringhand(self):
        shand=""
        for i in range(len(self.__hand)):
            if i==len(self.__hand)-1:
                shand+=self.__hand[i].sname()
            else:
                shand+=self.__hand[i].sname()
                shand+=", "
        return shand

    def handaslist(self):
        cards=[]
        for i in range(len(self.__hand)):
            cards.append(self.__hand[i].sname())
        return cards

    def playedcards(self,slhand):
        played=[]
        if len(slhand)==0:
            return played
        else:
            for i in range(len(slhand)):
                for j in range(len(self.__hand)):
                    if slhand[i]==self.__hand[j].sname():
                        played.append(self.__hand.pop(j)) 
                        break
        return played




'''    
class Combo:
    
    def __init__(self,hand):
        self.__hand=hand
        
    def determinecombo(self):
''' 
        



def shuffle(deck):
    for i in range(52):
        rand=random.randint(0,51)
        deck[i], deck[rand] = deck[rand], deck[i]

def displaydeck(deck):
    for i in range(len(deck)):
        #print(i)
        deck[i].display()
        
def displaycards(cards):
    for i in range(len(cards)):
         if i!=len(cards)-1:
                print(cards[i].sname(),end=",")
         else:
             print(cards[i].sname())

def sortcards(cards):
    for i in range(len(cards)-1):
        small=cards[i]
        index=i
        for j in range(i+1,len(cards)):
            if (small.getvalue()>cards[j].getvalue()):
                small=cards[j]
                index=j
        temp=cards[i]
        cards[i]=cards[index]
        cards[index]=temp
            
def deal(deck,p1,p2):
    count=0
    hand1=[]
    hand2=[]
    for i in range(10):
        hand1.append(deck.pop(0))
        hand2.append(deck.pop(0))
    p1.sethand(hand1)
    p2.sethand(hand2)

def handle_p(player_socket,player):
    shand=player.handaslist()
    dshand=json.dumps(shand)
    #print(information[0])
    player_socket.sendall(dshand.encode())
    data=player_socket.recv(1024)
    played=json.loads(data.decode())
    played=player.playedcards(played)
    print(player.getname()+" played:",end="")
    displaycards(played)
    sortcards(played)
    print(player.getname()+" played sorted:",end="")
    displaycards(played)
    print(player.getname()+" got:",end="")
    print(player.stringhand())
    player_socket.close()
    




def main():
    p1=Person("P1")
    p2=Person("P2")
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

    #display(deck)
    shuffle(deck)
    #print("Shuffled deck\n")
    #display(deck)
    #print("------------------------------------")
    deal(deck,p1,p2)
    #print("Player 1's hand\n")
    #display(p1)
    #print("------------------------------------")
    #print("Player 2's hand\n")
    #display(p2)
    #print("------------------------------------")
    #print("Remaining Deck\n")
    #display(deck)
    #print("------------------------------------")
    server_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 5000))
    server_socket.listen(2)
    player1_socket, addr1 = server_socket.accept()  
    print("Player 1 connected:", addr1)
    player2_socket, addr2 = server_socket.accept()
    print("Player 2 connected:", addr2)
    #shand1="Your hand:"+p1.stringhand()+"\n"
    #shand2="Your hand:"+p2.stringhand()+"\n"
    threading.Thread(target=handle_p, args=(player1_socket, p1)).start()
    threading.Thread(target=handle_p, args=(player2_socket, p2)).start()
    
main()

#rule of thumb just go with the trajectory of the game, keep it simple for now
#now maybe integrate what type of combo your cards that you selected are

