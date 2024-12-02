
"""Pseudocodes
1) create a counter for right answer
2) asign the minus sign to variable "sign" for easy use later in the program
3) create a counter for looping the questions
4) create pass and variables
5) generate random questions using random
6) collect the user answers
7) print the result
8) print the time taken to complete the task"""



import random

def get_results():
	
	right_answer = []
	sign = "-"
	counter = 0
	passed = 0
	failed = 0
	while counter <= 9:
		rand_number1 = random.randrange(1,100)
		rand_number2 = random.randrange(1,100)
		
		response = int(input(f"Calculate {rand_number1} {sign} {rand_number2}: "))
		if counter <= 9:

			answer = rand_number1 - rand_number2
		
		if answer == response:
			passed += 1

		else: 
			failed += 1
		right_answer.append(f"You missed question {counter 
+1}, The correct answer for {rand_number1} {sign} {rand_number2} is {answer}")

		counter +=1
	for result in right_answer:
		print (result)

	
	return (f"Your score is {passed} / {failed}")

print(get_results())
print("You spent 30 seconds on this task")


