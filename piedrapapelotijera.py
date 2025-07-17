play = "yes"
while play == "yes":

    print("Hello, my Skibbidi Sigma! You play my game.")
    answer = int(input("What will you choose? (1 🪨), (2 🧻), (3 ✂️)  "))

    import random

    computer_answer = random.randint(1, 3)

    rock = 1
    paper = 2
    scissors = 3

    if computer_answer == answer:
        print("It's a tie")

    elif computer_answer > answer:
        print("I won >:D")
        break

    elif answer > computer_answer:
        print("You won D:")
        break

    else:
        print("Please enter a valid response")

    play = input("Do you want to play again? ")
