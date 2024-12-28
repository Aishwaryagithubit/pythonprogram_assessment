#ask user to enter the temperature in celsius
temperature = float(input("enter a temperature in celsius: "))
#convert celsius into Fahrenheit
result = (temperature *9/5) + 32
print(f"{temperature} is equivalent to {result}F.")