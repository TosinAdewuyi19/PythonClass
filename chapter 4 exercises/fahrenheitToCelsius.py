def Fahrenheit(celsius):
    return (9 / 5 ) * Celsius + 32
print(f"{'Celsius':>10} {'Fahrenheit':>12}")

for Celsius in range(101):
    fahrenheit_value = Fahrenheit(Celsius)
    print(f"{Celsius:>10} {fahrenheit_value:>12.1f}")