numbers = []
for i in range (3):
   number = float(input("Enter the numbers: "))
   numbers.append(number)
   firstNumber, secondNumber, thirdNumber = numbers
if (firstNumber < secondNumber < thirdNumber):
	print("Increasing")

elif (firstNumber > secondNumber > thirdNumber):
	print("Decreasing")
