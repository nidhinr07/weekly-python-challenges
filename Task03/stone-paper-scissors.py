import random

options = ("stone", "paper", "scissors")
computer_score = 0
user_score = 0

print(">>>>>>>>>>>>>>>>>>     LETS START THE GAME     <<<<<<<<<<<<<<<<<<<<<<<<<<<")

while True:
    answer = random.choice(options)

    print("-----------------------")
    print(f"Your Score: {user_score}")
    print(f"Computer Score: {computer_score}")
    print("-----------------------")

    choice = input("(Stone, Paper, Scissors or Exit): ").strip().lower()

    if choice == "exit":
        break

    if choice not in options:
        print("Invalid choice! Please choose Stone, Paper or Scissors.")
        continue

    print("Computer Choice:", answer)

    if choice == answer:
        print("It's a Draw!")

    elif choice == "stone" and answer == "scissors":
        user_score += 1
        print("You Win!")

    elif choice == "paper" and answer == "stone":
        user_score += 1
        print("You Win!")

    elif choice == "scissors" and answer == "paper":
        user_score += 1
        print("You Win!")

    else:
        computer_score += 1
        print("Computer Wins!")


print("\nFINAL RESULTS")
print("-----------------------------")
print(f"Your Score: {user_score}")
print(f"Computer Score: {computer_score}")
print("-----------------------------")

if user_score > computer_score:
    print("\nYou Win!!!")

elif computer_score > user_score:
    print("\nComputer Wins!!!")

else:
    print("\nIt's a Draw!!!")
