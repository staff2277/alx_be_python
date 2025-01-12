FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5



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
    results = (temperature -32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    print(f"{temperature}°{unit} is {results}°C")
    return results

def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    results = (temperature * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    print(f"{temperature}°{unit} is {results}°F")
    return results
    
    
   
if unit == 'f' or unit == "F":
      convert_to_celsius(unit)
elif unit == 'c' or unit == "C":
      convert_to_fahrenheit(unit)



""" temperature conversion programme """