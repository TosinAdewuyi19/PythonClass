letter = input("Enter a single letter: ")
if len(letter) != 1 or not letter.isalpha():
	print("Not a single letter")


if letter in 'AEIOUaeiou':
		print("Vowel")
else: 
	print("Consonant")


