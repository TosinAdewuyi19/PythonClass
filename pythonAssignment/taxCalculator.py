def calculate_tax(earnings):
	if earnings <= 30000:
		tax = earnings * 0.15
	else:
		tax = earnings * 0.20
for i in range(3):
	name = input("enter citizen's name: ")
	earnings = float(input("Enter citizen's earning: "))
tax = calculate_tax(earnings)
print(f"{name} owes ${tax:  } in taxes.")