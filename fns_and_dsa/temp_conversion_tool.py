FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    print(f"{fahrenheit}°F is {celsius}°C")
    return celsius

def convert_to_fahrenheit(celsius):
    fahrenheit = (celsius * (9/5)) + 32 
    print(f"{celsius}°C is {fahrenheit}°F")
    return fahrenheit

try:
    temperature = float(input("Enter the temperature to convert: "))
    if not isinstance(temperature, (int, float)):
        raise ValueError("Invalid temperature. Please enter a numeric value.")
except ValueError:
    print("Invalid temperature. Please enter a numeric value.")
    exit()

unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().lower()

if unit == 'f':
    convert_to_celsius(temperature)
elif unit == 'c':
    convert_to_fahrenheit(temperature)
else:
    print("Invalid unit. Please enter either 'C' or 'F'.")