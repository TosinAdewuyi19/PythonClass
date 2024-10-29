import random
random_number = random.randint(1, 50)
guess = None
while guess != random_number:
	guess = int(input("Guess a number between 1 and 50: "))
if guess < random_number:
	print("Too low, try another number. ")
elif  guess > random_number:
	print("Too high, try another number.")
	print ("Correct! The number is", random_number)
