import math

# Data organisation.
radiation_data = {
    "City Centre": [22, 19, 20, 31, 28],
    "Industrial Zone": [35, 32, 30, 37, 40],
    "Residential District": [15, 12, 18, 20, 14],
    "Rural Outskirts": [9, 13, 16, 14, 7],
    "Downtown": [25, 18, 22, 21, 26]
}

# Average Calculation.
def calculate_average(data):
    return sum(data) /len(data)

# Standard Deviation Calculation.
def calculation_def_deviation(data):
    avg = calculate_average(data)
    variance = sum((x - avg) ** 2 for x in data) /len(data)
    std_dev = math.sqrt(variance)
    return std_dev

# Calculate and print averageand standard deviation for each location
for location, radiation in radiation_data.items():
    avg = calculate_average(radiation)
    std_dev = calculation_def_deviation(radiation)
    print(f"Location: {location}")
    print(f"average Radiation: {avg: .2f}")
    print(f"Standard Deviation: {std_dev: .2f}")
    print()


