number = int(input("Enter a number: "))
terms = int(input("Enter the number of terms"))

i = 0
while i <= terms:	
	result = number * i
	print(f"{number} X {terms} = {result}")
	i += 1