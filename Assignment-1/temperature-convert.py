def convert_temperature(temperature, unit):
    if unit.lower() == 'c': # Check if the unit is Celsius
        # Convert Celsius to Fahrenheit
        converted = round((temperature * 9/5) + 32, 2) # Using round for better precision
        return f"{temperature}°C is {converted}°F" #returning formatted string
    
    elif unit.lower() == 'f': # Check if the unit is Fahrenheit
        # Convert Fahrenheit to Celsius
        converted = round((temperature - 32) * 5/9, 2) #using round for better precision
        return f"{temperature}°F is {converted}°C" #returning formatted string
    
    else:
        return "Invalid unit. Please use 'C' for Celsius or 'F' for Fahrenheit." #handling invalid input

# Looping for multiple inputs
while True:
    try:
        temp = float(input("Enter temperature value: "))
        unit = input("Enter unit ('C' for Celsius, 'F' for Fahrenheit): ")
        print(convert_temperature(temp, unit)) #calling the conversion function and printing the result
        again = input("Convert another? (y/n): ") #asking user if they want to convert another temperature
        if again.lower() != 'y': #if user does not want to continue, break the loop
            break
    except ValueError: #handling non-numeric input
        print("Invalid input, please enter a numeric value") #asking user to enter a valid numeric value
