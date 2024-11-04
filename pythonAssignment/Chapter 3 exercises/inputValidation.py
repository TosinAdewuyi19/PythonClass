passes = 0
failures = 0

for student in range(10):
    result = int(input('Enter result (1=pass, 2=fail): '))

while result != 1 and result != 2:
    print('invalid input. Please enter 1 or 2. ') 
    result= int(input('Enter result (1= pass, 2=fail): '))
if result ==1:
    passes = passes + 1
else: 
    failures = failures + 1
print('Passes:', passes)
print('Failures:', passes)
if passes > 8: 
    print ('Bonus to instructor!')