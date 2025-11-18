nums = []

# Append 1–20
for i in range(1, 21):
    nums.append(i)

# Remove odd numbers
nums = [n for n in nums if n % 2 == 0]

# Sort descending
nums = sorted(nums, reverse=True)

# Slice top 3 numbers
top3 = nums[:3]

print(top3)
