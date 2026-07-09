'''
An airline wants to manage routes between cities.

Requirements
Create a graph where each city is connected to its direct flight destination.
Display all available routes.
Store all city names in a list.
Sort the city names alphabetically using Insersion Sort.
Ask the user to search for a city using Binary Search.
If found, display all cities directly connected to it.
Otherwise, display "City not found".
'''

graph = {
    "Delhi": ["Mumbai", "Kolkata"],
    "Mumbai": ["Delhi", "Chennai"],
    "Chennai": ["Mumbai", "Bangalore"],
    "Bangalore": ["Chennai"],
    "Kolkata": ["Delhi"]
}

print("Available Routes:")
for city in graph:
    print(city, "->", graph[city])

cities = list(graph.keys())

for i in range(1, len(cities)):
    key = cities[i]
    j = i - 1

    while j >= 0 and cities[j] > key:
        cities[j + 1] = cities[j]
        j -= 1

    cities[j + 1] = key

print("\nSorted Cities:")
print(cities)

search = input("\nEnter city to search: ")

low = 0
high = len(cities) - 1
found = False

while low <= high:
    mid = (low + high) // 2

    if cities[mid] == search:
        found = True
        break
    elif cities[mid] < search:
        low = mid + 1
    else:
        high = mid - 1

if found:
    print("City Found")
    print("Direct Flights:", graph[search])
else:
    print("City not found")