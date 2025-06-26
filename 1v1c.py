import socket
import json

def choosecards(hand):#choose cards in hand, makes it so that you can select and deselect the card by clicking the number
    chosen=[]
    for i in range(len(hand)):
        print(str(i+1)+":"+hand[i])
    print("\nChoose a card by pressing its number then pressing enter")
    while True:
        try:
            choice=int(input("Enter a choice:"))
        except:
            print("Wrong input, try again\n")
            continue
        if choice==0:
            break
        elif choice<0 or choice>len(hand):
            print("Wrong input, try again\n")
            continue
        else:
            if hand[choice-1] not in chosen:
                chosen.append(hand[choice-1])
                print("You chose:",hand[choice-1])
            else:
                chosen.remove(hand[choice-1])
                print("You deselected:",hand[choice-1])
            print("\n")
        print("Your choices so far:",end="")
        for i in range(len(chosen)):
            if i!=len(chosen)-1:
                print(chosen[i],end=",")
            else:
                print(chosen[i])
        print("\n")
    return chosen


def displaycards(cards):
    for i in range(len(cards)):
        print(str(i+1),end=":")
        print(cards[i])
         


def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 5000))

    # Game loop to interact with the server
    while True:
        data = client_socket.recv(1024)
        shandlist = json.loads(data.decode())
        #displaycards(shandlist)
        #print(len(shandlist))
        chosen=choosecards(shandlist)    
        # for i in range(len(chosen)):
        #     print(chosen[i])
        dchosen=json.dumps(chosen)
        client_socket.sendall(dchosen.encode())
        input()
    client_socket.close()
main()
