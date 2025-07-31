temperatures = [
  {'city': "Paris", 'continent': "Europe", "temperature": "12"},
  {'city': "Los Angeles", 'continent': "North America", "temperature": "22"},
  {'city': "Paris", 'continent': "Asia", "temperature": "18"},
  {'city': "New York", 'continent': "North America", "temperature": "14"},
  {'city': "Sao Paulo", 'continent': "South America", "temperature": "25"},
  {'city': "Toronto", 'continent': "North America", "temperature": "2"}
]

# Given the list of temperatures, calculate and print the average temperature of north American cities
Number_of_NA_cities = 0
total_temperature_NA = 0
for temp in temperatures:
    if temp['continent'] == 'North America':
        total_temperature_NA += int(temp['temperature'])
        Number_of_NA_cities += 1
average_temperature_NA = total_temperature_NA / Number_of_NA_cities
print(f"The average tempetarure of North America is, {average_temperature_NA}")