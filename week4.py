populations = [
    {'country': 'france', 'population': 60000000},
    {'country': 'Spain', 'population': 12000000}, 
    {'country': 'USA', 'population': 8000000},
    {'country': 'Australia', 'population': 3000000},
    {'country': 'Canada', 'population': 15000000}
]
total_population = sum(country['population'] for country in populations)
print(f"The total population is:{total_population/1000000} million people")