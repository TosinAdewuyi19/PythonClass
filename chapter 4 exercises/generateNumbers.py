import random

def generate_numbers():
    number1 = random.randint(1, 9)
    number2 = random.randint(1, 9)
    return (number1, number2)

def multiplication_quiz():
    while True:
        number1, number2 = generate_numbers()
        while True:
            print(f"How much is {number1} times {number2}?")
            answer = int(input("Your answer: "))
    
            if answer == number1 * number2:
                print("Very good! Well done!")
                break
            else:
                print("No. Please try again.")
        another = input("Do you want to solve another problem? (yes/no): ")
        if another != 'yes':
            print("Thank you for participating! Goodbye!")
            break

multiplication_quiz()
