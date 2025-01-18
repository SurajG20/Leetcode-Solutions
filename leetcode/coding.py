def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []



# Reading input
import ast
nums = ast.literal_eval(input().strip())  # Safely evaluate the array string
target = int(input().strip())

# # Solve and output
result = two_sum(nums, target)
print(f"Input array: {nums}")
print(f"Target sum: {target}")
print(f"Output indices: {result}")