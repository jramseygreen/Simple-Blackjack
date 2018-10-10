def main():
    print("")
    n=int(input("How many decks do you wish to play with?"))
    deck=makedeck(n)
    deckQ(deck)
    deck=shuffleQ(deck)
    deckQ(deck)
    playGame(deck)
    
def deckQ(deck):
    print("")
    ins=input("would you like to see the cards? (y/n): ")
    if ins=="y":
        print(deck)
        
def shuffleQ(deck):
    print("")
    option=input("Do you wish to shuffle the deck? (y/n): ")
    if option.lower()=="y":
        deck=shuffle(deck)
    return deck;

def playGame(deck):
    print("")
    playerNum=int(input("How many players?: "))
    running=True
    while running:
        #ask to shuffle the deck
        deck=shuffleQ(deck)
        deckQ(deck) #ask to see the deck          
        hand=makeHands(playerNum, deck) #array of arrays, e.g. hand[0] displays 2 cards of the dealer
                                        #hand[0][0] and hand[0][1] gives the 2 cards held respectively
        
        for i in range(len(hand)):
            if i!=0:
                print("")
                print("     The dealer has: ")
                print("          ",hand[0])
                printPlayers(hand)
                game=True
                while game:
                    print("")
                    print("Player",i)
                    option=int(input("[1] Stick or [2] Twist: "))
                    if option==2:
                        hand[i].append(dealCard(deck))
                        if validate(hand[i]):
                            print("")
                            print("bust!")
                            hand[i].append("BUST")
                            game=False
                        else:
                            print("")
                            print("     Player",i,"has: ")
                            print("          ",hand[i])

                    elif option==1:
                        game=False
        playDealer(hand, deck)
        hand=gameOutcome(hand)
        printResult(hand)
        print("")
        print(hand)
        
        for i in hand:
            if "BUST" in i:
                i.remove("BUST")
            if "WIN" in i:
                i.remove("WIN")
            if "LOSE" in i:
                i.remove("LOSE")
            deck+=i
            print("")
        print(deck)

def printResult(hand):
    print("")
    n=0
    for i in hand:
        if "BUST" in i or "LOSE" in i:
            if n==0:
                print("Dealer Lost.")
                print("")
            else:
                print("player",n,"Lost.")
        elif "WIN" in i:
            print("player",n,"Won.")
        n+=1
    
def playDealer(hand, deck):
    running=True
    while running:
        besthand=bestHand(hand)
        if value(hand[0])<15 and value(hand[0])<value(besthand):
            hand[0].append(dealCard(deck))
            if validate(hand[0]):
                hand[0].append("BUST")
                running=False
        else:
            running=False  
    
def bestHand(hand):
    best=["c2","h2"]
    for i in hand:
        if value(i)>value(best):
            best=i
    return best;

def gameOutcome(hand):
    for i in hand:
        if value(i)>value(hand[0]) or "BUST" in hand[0]:
            i.append("WIN")
        else:
            i.append("LOSE")
    return hand;

def value(hand):
    total=0
    for i in hand:
        if i!="BUST":
            if i[1]=="A":
                total+=11
            elif i[1]=="J" or i[1]=="Q" or i[1]=="K":
                total+=10
            else:
                try:
                    total+=int(i[1])
                except:
                    total=total
    for n in hand: #ace is 11 or 1
        if "A" in n and total>21:
            total-=10
    return total;
    
def validate(hand):
    total=value(hand)
    if total>21:
        return True;
    else:
        return False;
            
def printPlayers(hand):
    for i in range(len(hand)-1):
        print("")
        print("     player",i+1,"has: ")
        print("          ",hand[i+1])
        
def makeHands(n, deck):
    hand=[]
    hand.append(dealHand(deck)) #hand 0 is always the dealer's hand

    #players' hands
    for i in range(n):
        hand.append(dealHand(deck))
                      
    return hand;
                      
def dealHand(deck):
    hand=[]
    for i in range(2):
        hand.append(dealCard(deck))
        
    
    return hand;

def dealCard(deck):
    return deck.pop(0);

    
def shuffle(deck):
    from random import randint
    #every card is moved to random place in the deck
    for i in range(len(deck)):
        num=randint(0,len(deck)-1)

        #swap to random place
        temp=deck[i]
        deck[i]=deck[num]
        deck[num]=temp
        
    return deck;

def makedeck(n):
    deck=[]
    for i in range(n):
        for n in range(13):
            #special cards
            if n==0:
                deck.append("cA")
                deck.append("hA")
                deck.append("sA")
                deck.append("dA")
            elif n==10:
                deck.append("cJ")
                deck.append("hJ")
                deck.append("sJ")
                deck.append("dJ")
            elif n==11:
                deck.append("cQ")
                deck.append("hQ")
                deck.append("sQ")
                deck.append("dQ")
            elif n==12:
                deck.append("cK")
                deck.append("hK")
                deck.append("sK")
                deck.append("dK")
            #regular cards
            else:
                deck.append("c"+str(n+1))
                deck.append("h"+str(n+1))
                deck.append("s"+str(n+1))
                deck.append("d"+str(n+1))
        
    return deck;

main()
