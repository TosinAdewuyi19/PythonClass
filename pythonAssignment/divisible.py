x = 5 
y = 20
p = 3 
count_divisible = 0
for i in range(x, y, +1):
	if i % p == 0:
		count_divisible += 1
		print("The number of values divisible by", p, "between", x, "and", y, "is", count_divisible) 