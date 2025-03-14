import random
import socket
import threading
import json





class Cards:

    
    def __init__(self,name,value,addvalue,suit):
        self.__name=name
        self.__value=value
        self.__suit=suit
        self.__addvalue=addvalue

    
    def getvalue(self):
        return self.__value

    def getsuit(self):
        return self.__suit

    def getname(self):
        return self.__name

    def getaddvalue(self):
        return self.__addvalue

    def display(self):
        print(self.__name,"of",self.__suit+",",self.__value)

        
    def sname(self):
        return self.__name+" of "+self.__suit

    
    def gettotvalue(self):
        return self.__value+self.__addvalue





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
            if (small.gettotvalue()>cards[j].gettotvalue()):
                small=cards[j]
                index=j
        temp=cards[i]
        cards[i]=cards[index]
        cards[index]=temp
    return cards

            
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


def randomamount(hand,num):
    amount=[]
    for i in range(num):
        while True:
            rand=random.randint(0,len(hand)-1)
            if hand[rand] not in amount:
                break
        amount.append(hand[rand])
    return amount


def isfourofakind(played):
    if not len(played)>=4:
        #print(1)
        return False
    else:
        #print(2)
        for i in range(len(played)):
            if (i+3)>=(len(played)):
                break
            else:
                #print(3)
                if played[i].gettotvalue()==played[i+3].gettotvalue():
                    return True
    return False


def isstraightflush(played):
    if len(played)<5:
        return False
    else:
        for i in range(0,len(played)):
            possible=[]
            card=played[i]
            #print("Initial card:",played[i].sname())
            for j in range(4):
                #print("The current card is",card.sname())
                card=getnextcard(card)
                #print("The next card is",card.sname())
                #print()
                if card.getvalue()==11:
                    break
                possible.append(card)
            '''
            displaycards(possible)
            print("One card is",possible[0].getvalue()," and the other is",played[1].getvalue())
            if samecard(possible[0],played[1]):
                print("Matches")
            else:
                print("Doesn't match")
            '''
            if card.getvalue()==11:
                continue
            if ifin(possible,played):
                print("The straight flush:",end="")
                print(played[i].sname(),end=",")
                displaycards(possible)
                return True
        return False


def getnextcard(card):
    '''
    print(card.sname())c
    print("Value:",card.getvalue())
    print("Add Value:",card.getaddvalue())
    '''
    face=["Jack","Queen","King"]
    if card.getvalue()>0 and card.getvalue()<10:
        '''
        print(card.sname())
        print("Next Value:",card.getvalue()+1)
        '''
        return Cards(str(card.getvalue()+1),card.getvalue()+1,0,card.getsuit())
    elif card.getvalue()==10:
        if card.getname()=="King":
            return Cards("Ace",11,0,card.getsuit())
        else:
            '''
            print(card.sname())
            print("Value:",card.getvalue())
            print("Add Value:",card.getaddvalue())
            print("Tot Value:",card.gettotvalue())
            print("Minused:",round(card.gettotvalue()-10,2))
            print("Face num:",int(round((round(card.gettotvalue()-10,2)*10))))
            '''
            return Cards(face[int(round((round(card.gettotvalue()-10,2)*10)))],10,card.getaddvalue()+.1,card.getsuit())
    else:
        return Cards("2",2,0,card.getsuit())


def samecard(card1,card2):
    if card1.sname()==card2.sname():
        return True
    return False


def ifin(hand1,hand2):
    count=0
    #print(len(hand1))
    for i in range(len(hand1)):
        for j in range(len(hand2)):
            if samecard(hand1[i],hand2[j]):
                count+=1
                break
        if count==len(hand1):
            return True
    return False

        
def main():
    p1=Person("P1")
    p2=Person("P2")
    deck=[]
    names=["Jack","Queen","King"]
    suit=["Spade","Club","Diamond","Hearts"]
    for i in range(13):
        for j in range(4):
            addvalue=0
            if (i<9):
                name=str(i+2)
                value=i+2
                #print("value:",value)
            elif (i>8 and i<12):
                name=names[i-9]
                value=10
                addvalue+=(round((i-8)*.1,2))
                #print(addvalue)
            else:
                name="Ace"
                value=11
            card=Cards(name,value,addvalue,suit[j])
            deck.append(card)
    #display(deck)
    #shuffle(deck)
    #print("Shuffled deck\n")
    #display(deck)
    #print("------------------------------------")
    #deal(deck,p1,p2)
    #print("Player 1's hand\n")
    #display(p1)
    #print("------------------------------------")
    #print("Player 2's hand\n")
    #display(p2)
    #print("------------------------------------")
    #print("Remaining Deck\n")
    '''
    displaydeck(deck[0:30])
    if (isstraightflush(deck[0:20:4])):
        print("True")
    else:
        print("False")  
    #print("------------------------------------")
    '''
    '''
    count=1
    for i in range(len(deck)):
        print("Current card:",deck[i].sname())
        print("Next card:",getnextcard(deck[i]).sname())
        print(count)
        print()
        count+=1
    displaycards(deck[0:5])
    if (isfourofakind(deck[0:4])):
        print("True")
    else:
        print("False")
    print("Player 1's cards",end=":")
    displaycards(p1.gethand())
    '''
    
    count=0
    amount=15
    while True:
        while True:
            randoms=randomamount(deck,amount)
            print(amount,"randoms are:",end="")
            displaycards(randoms)
            played=sortcards(randoms)
            print(amount,"randoms sorted are:",end="")
            displaycards(played)
            if isstraightflush(played):
                break
            print("\n")
            count+=1
        input()
    #print("Count:"+str(count))
    '''
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
    '''
    
main()

#rule of thumb just go with the trajectory of the game, keep it simple for now
#now maybe integrate what type of combo your cards that you selected are
#move on to other combos like (three of a kind, fullhouse), sorted function is not correct(doesn't sort face cards and 10's correctly)
