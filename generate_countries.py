import random

def generate_country_city(num_samples=1):
    countries = random.choices(population=["South Africa", "England", "Hong Kong SAR", "Malaysia", "Singapore"], weights = [0.2, 0.2, 0.2, 0.2, 0.2], k=num_samples)

    cities = []
    for city in countries:
        if city == "South Africa":
            south_africa_cities = random.choices(population=["Cape Town", "Johannesburg", "Pretoria"], weights = [0.33, 0.33, 0.33])
            cities.append(south_africa_cities[0])
        elif city == "England":
            england_cities = random.choices(population=["Essex", "London", "Manchester"], weights =[0.33, 0.33, 0.33])
            cities.append(england_cities[0])
        elif city == "Malaysia":
            malaysia_cities = random.choices(population=["Kuala Lumpur", "George Town"], weights =[0.5, 0.5])
            cities.append(malaysia_cities[0])
        elif city == "Singapore":
            singapore_cities = "Singapore"
            cities.append(singapore_cities)
        elif city == "Hong Kong SAR":
            hk_cities = "Hong Kong"
            cities.append(hk_cities)
    
    return countries, cities 
