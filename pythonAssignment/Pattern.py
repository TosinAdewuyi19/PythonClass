print("Pattern A")
for i in range(1, 6):
	print('*' * i)

print("Pattern B")
for i in range(6, 0, -1):
	print('*' * i)

print("Pattern C")
for i in range(1, 6):
	print(' ' * (5 - i) + '*' * i)

print("Pattern D")
for i in range(5, 0, -1):
	print(' ' * (i - 5) + '*' * i)