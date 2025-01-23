import socket
import json

def choosecards(hand):
    chosen=[]
    for i in range(len(hand)):
        print(i+1,":",hand[i])
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
        
def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 5000))

    # Game loop to interact with the server
    
    data = client_socket.recv(1024)
    shandlist = json.loads(data.decode())
    #print(len(shandlist))
    chosen=choosecards(shandlist)    
    dchosen=json.dumps(chosen)
    client_socket.sendall(dchosen.encode())
    client_socket.close()

main()
