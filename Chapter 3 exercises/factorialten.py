e = 1.0  # Initialize e to 1

for i in range(1, 11): 
    factorial = 1
    for j in range(1, i + 1):
        factorial *= j
    e += 1 / factorial

print("Estimated value of e:", e)