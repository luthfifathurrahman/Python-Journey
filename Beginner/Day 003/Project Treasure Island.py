print("welcome to treasure island.")
print("your mission is to find treasure.")
left_or_right = input("do you want to go right or left? type right or left: ").lower()
if left_or_right == "left":
    print("congrats, you go to the next phase")
    swim_or_wait = input("do you want to swim or wait? type swim or wait: ").lower()
    if swim_or_wait == "wait":
        print("congrats again!!")
        door = input("which door do you want to enter? blue, red, or yellow? type blue, red, yellow: ").lower()
        if door == "yellow":
            print("you win!")
        elif door == "red":
            print("burned by fire")
        elif door == "blue":
            print("eaten by beasts")
        else:
            print("game over")
    else:
        print("game over")
else:
    print("game over")
