def temperature(temp_fahrenheit):
    temp_centigrade = (5 / 9) * (temp_fahrenheit - 32)
    return temp_centigrade

temp_fahrenheit = float(input("Enter temperature in Fahrenheit: "))
temp_centigrade = temperature(temp_fahrenheit)

print(f"{temp_fahrenheit}°F is equivalent to {temp_centigrade}°C")