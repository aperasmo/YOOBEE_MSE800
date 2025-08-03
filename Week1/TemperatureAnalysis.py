import numpy as np

#  Define the temperature data
temps_celsius = np.array([18.5, 19, 20, 25.0, 2, 30, 13.9])

# calculate average temperature
def get_average(temp_list):
    return np.mean(temp_list)

# find highest and lowest temperatures
def get_extremes(temp_list):
    highest = np.max(temp_list)
    lowest = np.min(temp_list)
    return highest, lowest

#  (Use the formula: F = C × 9/5 + 32) calculate average temperature
def convert_to_fahrenheit(temp_list):
    return temp_list * 9/5 + 32

#  find days with temperature > 20°C
def find_hot_days(temp_list, threshold=20):
    return np.where(temp_list > threshold)[0]

     
    
average = get_average(temps_celsius)
high, low = get_extremes(temps_celsius)
temps_fahrenheit = convert_to_fahrenheit(temps_celsius)
hot_days = find_hot_days(temps_celsius)

days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
hot_days = [day for day, temp in zip(days, temps_celsius) if temp > 20]     
        
if __name__ == "__main__":
    try:
        #  Display the results
        print("Temperature list in Celsius", temps_celsius)
        print(f"Average temperature: {average:.2f}°C")
        print(f"Highest temperature: {high}°C")
        print(f"Lowest temperature: {low}°C")
        print("Temperatures in Fahrenheit:",(temps_fahrenheit))
        print("Days with temperature > 20°C):", hot_days)
        
    except ValueError as e:
        print("Error:", e)
