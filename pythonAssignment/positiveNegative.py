negative_count = 0
positive_count = 0
zero_count = 0

for count in range(0,5):
    number = float(input(f"Please enter number {count+1}: "))

    if number < 0:
        negative_count += 1
    elif number > 0:
        positive_count += 1
    else:
        zero_count += 1

print("\nResults:")
print(f"Negative numbers: {negative_count}")
print(f"Positive numbers: {positive_count}")
print(f"Zeros: {zero_count}")
