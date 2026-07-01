# Dictionary with key-value pairs

student = {
    "name": "Rahul",
    "age": 20,
    "course": "BCA"
}

# Calling keys and values

print("Keys:")
for key in student:
    print(key)

print("\nValues:")
for value in student.values():
    print(value)

print("\nKey-Value Pairs:")
for key, value in student.items():
    print(key, ":", value)