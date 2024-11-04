total_miles = 0
total_gallons = 0

while True:
    miles = float(input("Enter miles driven or 0 to quit: "))
    if miles ==0:
       break

    gallons = float(input("Enter gallons used: "))

    mpg = miles / gallons
    print(f"Miles per gallon for this trip is: {mpg:.2f}")
    total_miles += miles
    total_gallons += gallons

    combined_mpg = total_miles / total_gallons
    print(f"Combined miles per gallons: {combined_mpg:.2f}")

    print("End of program!")
