print(f"{'n':>2} {'n!':>5}")  

for n in range(1, 6):
    factorial = 1
for i in range(1, n + 1):
        factorial *= i
print(f"{n:>2} {factorial:>5}")