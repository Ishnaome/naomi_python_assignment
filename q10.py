values = []

for i in range(5):
    values.append(input(f"Enter value {i+1}: "))

print("First:", values[0])
print("Last:", values[-1])
print("Full list:", values)
