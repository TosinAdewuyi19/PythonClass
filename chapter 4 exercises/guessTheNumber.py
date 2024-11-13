import random
def guess_the_number():
    print("Guess my number between 1 and 1000 with the fewest guesses")
    target_number = random.randint(1, 1000)
    guess = None 
    attempt = 0

    while guess != target_number:
        guess = int(input("Enter your guess: "))
        attempt +=1 

        if guess < target_number:
            print("Too low try again.")
        elif guess > target_number:
            print("Too high try again.")
    
    print(f"Congratulations. You gueesed the number in {attempts} attempts!")

    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again == 'yes':
        guess_the_number()
    else:
        print("Thank you for playing")
guess_the_number()