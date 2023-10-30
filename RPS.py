import random 

choices = ("Rock", "Paper", "Scissors")
user = input("Please select one: Rock, Paper, Scissors.")

while user not in choices:
    user = input("Your input was not valid. Please select one: Rock, Paper, Scissors. PS it is case sensetive!")

computer = random.choice(choices) 

print(f"User: {user}")
print(f"Computer: {computer}")

if computer == user: 
    print(f"It's a tie!")
elif((user == "Rock" and computer == "Scissors") or (user == "Scissors" and computer == "Paper") or (user == "Paper" and computer == "Rock")):
    print(f"You win!")
else: 
    print(f"You lose :(")

