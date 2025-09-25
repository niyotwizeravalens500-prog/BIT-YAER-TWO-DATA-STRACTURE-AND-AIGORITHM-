# Air Quality Readings Project

import array

# Integers: Generate air quality readings (e.g., PM2.5 values)
readings = [45, 52, 38, 60, 49, 55, 41]
total = sum(readings)
average = total / len(readings)
minimum = min(readings)
maximum = max(readings)

# Strings: Formatted report with f-strings
report = (
    f"Air Quality Report\n"
    f"------------------\n"
    f"Total Readings Value: {total}\n"
    f"Average Reading: {average:.2f}\n"
    
)
print(report)

# Booleans: Apply threshold with compound condition
THRESHOLD = 50
if average > THRESHOLD and maximum > THRESHOLD:
    print("Status: Above Standard\n")
else:
    print("Status: Below Standard\n")

# Lists: Add, remove, sort, and display
print("Original readings:", readings)
readings.append(53)  # Add new reading
readings = [r for r in readings if r != min(readings)]  # Remove the minimum
readings.sort()
print("Modified readings:", readings)

# Arrays: Use array module for a fixed-size subset
subset = array.array('i', readings[:5])
array_sum = sum(subset)
print(f"\nSum of array subset: {array_sum}")
print(f"Sum of list: {sum(readings)}")

# Dictionaries: List of reading records
records = [
    {'id': 1, 'name': 'Station A', 'value': 45},
    {'id': 2, 'name': 'Station B', 'value': 52},
    {'id': 3, 'name': 'Station C', 'value': 38},
    {'id': 4, 'name': 'Station D', 'value': 60},
]
# Update one record
records[1]['value'] = 58  # Update Station B
# Delete another
records = [rec for rec in records if rec['id'] != 3]  # Remove Station C
# Compute total of 'value'
total_value = sum(rec['value'] for rec in records)
print("\nUpdated Records:")
for rec in records:
    print(rec)
print(f"Total of 'value' field: {total_value}")