users = [
    {"name": "A", "age": 30},
    {"name": "B", "age": 22},
    {"name": "C", "age": 27}
]

sorted_users = sorted(users, key=lambda x: x["age"])
print(sorted_users)
