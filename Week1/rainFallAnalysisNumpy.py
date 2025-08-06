"""
week1- activity 4: Rainfall Analysis with NumPy
Sample rainfall = [0.0, 5.2, 3.1, 0.0, 12.4, 0.0, 7.5]

Tasks: 
Convert the list to a NumPy array and print it.
Print the total rainfall for the week.
Print the average rainfall for the week.
Count how many days had no rain (0 mm).
Print the days (by index) where the rainfall was more than 5 mm.
"""

import numpy as np
# Sample rainfall data for a week
rainfall = [0.0, 5.2, 3.1, 0.0, 12.4, 0.0, 7.5]
# Convert the list to a NumPy array
rainfall_array = np.array(rainfall)

def total_rainfall(rainfall_array):
    """Calculate the total rainfall for the week."""
    return np.sum(rainfall_array)

def average_rainfall(rainfall_array):
    """Calculate the average rainfall for the week."""
    return np.mean(rainfall_array)  

def no_rain_days(rainfall_array):
    """Count how many days had no rain (0 mm)."""
    return np.count_nonzero(rainfall_array == 0)

def days_with_rain(rainfall_array):
    """Count the days with rainfall more than the threshold."""
    return np.nonzero(rainfall_array > 0)  #display number of days with rain

def heavy_rain_indexes(rainfall_array, threshold=5):
    """Find the days with rainfall more than the threshold."""
    return np.where(rainfall_array > threshold)[0]  #returns indices of days with rainfall > threshold

"""
def days_with_heavy_rain(rainfall_array, threshold=5):
    #Find the days with rainfall more than the threshold.
    return np.where(rainfall_array > threshold)[0]  #returns indices of days with rainfall > threshold

days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'] #List of days in a week
days_with_heavy_rain = [day for day, rain_count in zip(days, rainfall_array) if rain_count > 5] #days with rainfall more than 5 mm     
"""
if __name__ == "__main__":
    try:
        # Display the results
        print("Rainfall data for the week:", rainfall_array)
        print(f"Total rainfall for the week: {total_rainfall(rainfall_array):.4f} mm")  # Display the total rainfall
        print(f"Average rainfall for the week: {average_rainfall(rainfall_array):.2f} mm")  # Display the average rainfall
        print(f"Number of days with no rain: {no_rain_days(rainfall_array)}")   # Count days with no rain
        print(f"Number of days with rain: {np.count_nonzero(rainfall_array > 0)}")  # Count days with rain 
        print(f"Days with rainfall more than 5 mm (by index): {heavy_rain_indexes(rainfall_array)}")  # Display days with heavy rain
        #print("Days with rainfall more than 5 mm:", days_with_heavy_rain)  # Display days with heavy rain
        
            
    except Exception as e:
        print("An error occurred:", e)

"""
# Calculate and print the total rainfall for the week
total_rainfall= np.sum(rainfall_array)
print(f"Total rainfall for the week: {total_rainfall:.4f} mm") #display 4 decimals
total_rainfall = np.mean(rainfall_array)
# Calculate and print the average rainfall for the week
print(f"Average rainfall for the week: {total_rainfall:.2f} mm") #display 2 decimals
# Count how many days had no rain (0 mm)
no_rain_days = np.count_nonzero(rainfall_array == 0)
print(f"Number of days with no rain: {no_rain_days}") #display number of days with no rain
#Count the days with raindfall
days_with_rain = np.count_nonzero(rainfall_array > 0)
print(f"Number of days with rain: {days_with_rain}") #display number of days with rain
"""