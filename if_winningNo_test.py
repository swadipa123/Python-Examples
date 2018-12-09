winning_no=130
guessed_no=input("Enter the no between 0 to 150 :")
guessed_no=int(guessed_no)
if winning_no==guessed_no:
    print("You win")
elif guessed_no< 130:
    print("TOO LOW")
else:
    print("Too high")       