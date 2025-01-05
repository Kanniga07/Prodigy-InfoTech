def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def convert_temperature(value, unit):
    unit = unit.upper()
    if unit == 'C':
        fahrenheit = celsius_to_fahrenheit(value)
        kelvin = celsius_to_kelvin(value)
        return f"{value} °C = {fahrenheit:.2f} °F\n{value} °C = {kelvin:.2f} K"
    elif unit == 'F':
        celsius = fahrenheit_to_celsius(value)
        kelvin = fahrenheit_to_kelvin(value)
        return f"{value} °F = {celsius:.2f} °C\n{value} °F = {kelvin:.2f} K"
    elif unit == 'K':
        celsius = kelvin_to_celsius(value)
        fahrenheit = kelvin_to_fahrenheit(value)
        return f"{value} K = {celsius:.2f} °C\n{value} K = {fahrenheit:.2f} °F"
    else:
        return "The unit is invalid. Kindly type C, F, or K."

def main():
    print("Converter of Temperature")
    try:
        value = float(input("Put the temperature value here: "))
        unit = input("Put in the measurement unit (C for Celsius, F for Fahrenheit, and K for Kelvin): ").strip().upper()
        print(convert_temperature(value, unit))
    except ValueError:
        print("The input is invalid. Kindly input a number for the temperature.")

if __name__ == "__main__":
    main()
