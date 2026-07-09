'''
A social Media platform stores  friendships between users.
Requirements
Create a Graph where each user is connected to their friend.
Display all users and their friends in a formated way.
Store all usernames in a list.
Sort the usernames using Insertion Sort.
Ask the user to enter a name to see if they exists(binary search) and if they are connected.
If found, display all of the user's friends.

'''
graph = {
    "Puja": ["Rahul", "Aman"],
    "Rahul": ["Puja", "Neha"],
    "Aman": ["Puja", "Karan"],
    "Neha": ["Rahul"],
    "Karan": ["Aman"]
}

print("Users and their Friends:")
for user in graph:
    print(user, "->", graph[user])


users = list(graph.keys())


for i in range(1, len(users)):
    key = users[i]
    j = i - 1

    while j >= 0 and users[j] > key:
        users[j + 1] = users[j]
        j -= 1

    users[j + 1] = key


print("\nSorted Usernames:")
print(users)


search = input("\nEnter username to search: ")


low = 0
high = len(users) - 1
found = False


while low <= high:
    mid = (low + high) // 2

    if users[mid] == search:
        found = True
        break
    elif users[mid] < search:
        low = mid + 1
    else:
        high = mid - 1


if found:
    print("\nUser Found")
    print("Friends of", search, ":", graph[search])
else:
    print("User not found")