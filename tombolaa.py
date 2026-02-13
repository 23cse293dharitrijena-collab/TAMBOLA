import random   


p1 = list(map(int, input("Player 1 choose 5 numbers: ").split()))
p2 = list(map(int, input("Player 2 choose 5 numbers: ").split()))

called_numbers = []
marked1 = []
marked2 = []

print("\nCaller starts calling numbers (enter 0 to stop)\n")

while True:
    call = int(input("Caller enter number: "))

    if call == 0:
        print("Game ended")
        break

    if call in called_numbers:
        print("Number already called!")
        continue

    called_numbers.append(call)

    
    if call in p1:
        marked1.append(call)
        print("Player 1 marked:", marked1)
    else:
        print("Not for Player 1")

    
    if call in p2:
        marked2.append(call)
        print("Player 2 marked:", marked2)
    else:
        print("Not for Player 2")

    print("Called so far:", called_numbers)

    
    if len(marked1) == 5:
        print("\nPlayer 1 WON")
        break

    if len(marked2) == 5:
        print("\nPlayer 2 WON")
        break
