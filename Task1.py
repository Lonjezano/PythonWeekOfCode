import random

number = random.randrange(1,9)
count = 0


guess = int(input("Guess a number between 1 and 9 : "))

while (number != guess):
    if guess > 9 or guess == 0:
        guess = int(input("Please enter a number beteen 1 and 9 : "))
        count +=1
    else:
        guess = int(input("Wrong guess, please try again : "))
        count +=1

print(f"You guessed correctly after {count} tries \nThank you for playing")
exit()
