# Temperature Converter in Python

temp = float(input("Enter the temperature value: "))
unit = input("Enter the unit (C for Celsius, F for Fahrenheit, K for Kelvin): ")

if unit.lower() == 'c':
    celsius = temp
    fahrenheit = (celsius * 9/5) + 32
    kelvin = celsius + 273.15
    print(f"\n{celsius:.2f} Celsius = {fahrenheit:.2f} Fahrenheit and {kelvin:.2f} Kelvin")

elif unit.lower() == 'f':
    fahrenheit = temp
    celsius = (fahrenheit - 32) * 5/9
    kelvin = celsius + 273.15
    print(f"\n{fahrenheit:.2f} Fahrenheit = {celsius:.2f} Celsius and {kelvin:.2f} Kelvin")

elif unit.lower() == 'k':
    kelvin = temp
    celsius = kelvin - 273.15
    fahrenheit = (celsius * 9/5) + 32
    print(f"\n{kelvin:.2f} Kelvin = {celsius:.2f} Celsius and {fahrenheit:.2f} Fahrenheit")

else:
    print("\nInvalid unit entered. Please use C, F, or K.")
