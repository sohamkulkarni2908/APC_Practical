cities = {"Pune": 7000000, "Kolhapur": 20000000,"Mumbai": 80000000,"Nagpur": 3000000}

city = input("Enter city to remove: ")

if city in cities:
    del cities[city]
    print(cities)
else:
    print("City not found")