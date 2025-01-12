FAHRENHEIT_TO_CELSIUS_FACTOR = (5/9)
CELSIUS_TO_FAHRENHEIT_FACTOR = (9/5)



temperature = int(input("Enter the temperature to convert: "))
if not isinstance(temperature, int):
        print("Invalid temperature. Please enter a numeric value.")
        temperature = int(input("Enter the temperature to convert: "))

unit = str(input("Is this temperature in Celsius or Fahrenheit? (C/F): "))
if not isinstance(unit, str):
        print("Invalid unit. Please enter a either C or F.")
        unit = str(input("Is this temperature in Celsius or Fahrenheit? (C/F): "))

def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    FAHRENHEIT_TO_CELSIUS_FACTOR = (temperature -32) * (5/9)
    print(f"{temperature}°{unit} is {FAHRENHEIT_TO_CELSIUS_FACTOR}°C")
    return FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    CELSIUS_TO_FAHRENHEIT_FACTOR = (temperature * 1.8) + 32
    print(f"{temperature}°{unit} is {CELSIUS_TO_FAHRENHEIT_FACTOR}°F")
    return CELSIUS_TO_FAHRENHEIT_FACTOR
    
    
   
if unit == 'f' or unit == "F":
      convert_to_celsius(unit)
elif unit == 'c' or unit == "C":
      convert_to_fahrenheit(unit)



""" temperature conversion programme """