import random
print("START THE PREDICT GAME:-\n")

def winnner(player1 , player2):
    if player1 > player2:
        print(f"opps! {A}")
        print(f"Match Won {B}")
    elif player1 < player2:
        print(f"opps! {B}")
        print(f"Match Won {A}")
    else:
        print("Match Draw")

def players():
    print("TERM PLAYER-1:")

    computer = random.randint(1,30)
    count1 = 1
    global A

    A = input('PLAYER-1 ENTER YOUR NAME: ')
    while True:
        try:
            player1 = int(input(f"{A} enter the number in range of 1 to 30:- "))
            if player1 > 30 or player1 == 0 or player1<0:
                print(f"{A} enter the number in given range:")
            elif computer > player1:
                print(f"{A} enter the bigger number of",player1)
            elif computer < player1:
                print(f"{A} enter the smaller number of",player1)
            elif computer == player1:
                print("match the number")
                print(f"{A} you get the matching in " + str(count1) + " attempt:")
                break
            count1 = count1+1
        except Exception as E:
            print(str(E))
            print(f"{A} Enter Only Integer Not Alpha, Decimal & Special Character")



    print(f"\nNOW the, TERM PLAYER-2:")
    computer = random.randint(1,30)
    count2 = 1
    global B

    B = input('PLAYER-2 ENTER YOUR NAME: ')

    while True:
        try:
            player2 = int(input(f"{B} enter the number in range of 1 to 30:- "))
            if player2 > 30 or player2 == 0 or player2<0:
                print(f"{B} enter the number in given range:")
            elif computer > player2:
                print(f"{B} enter the bigger number of",player2)
            elif computer < player2:
                print(f"{B} enter the smaller number of",player2)
            elif computer == player2:
                print("match the number")
                print(f"{B} you get the matching in " + str(count2) + " attempt:\n")
                break
            count2 = count2+1

        except Exception as E:
            print(str(E))
            print(f"{B} Enter Only Integer Not Alpha, Decimal & Special Character")

    winnner(count1, count2)
def again_play():
    players()

    try:
        while True:

            a = input("\nWant To Play Again: (Y OR N) - ")
            if a == "Y" or a == "y":
                players()
            elif a == 'N' or a == 'n':
                print('Thanks For Playing ')
                break
            elif a != "Y" or a != "y":
                print('please enter given construction:')
                print("Press only Y or N  \nY for 'CONTINUE' & N for 'QUIT' ")
    except Exception as E:
        print(str(E))
            
again_play()
print("\nGAME END")  