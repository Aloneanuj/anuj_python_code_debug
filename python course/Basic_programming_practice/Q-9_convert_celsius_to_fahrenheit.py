# Convert Celsius to Fahrenheit
# F=(C× 9/5 )+32

def celsius_to_fahrenheit(temperature):
    Fahrenheit = (temperature * 9/5) + 32
    print(Fahrenheit)

temperature = float(input("Enter the temperature in celsius: "))
celsius_to_fahrenheit(temperature)