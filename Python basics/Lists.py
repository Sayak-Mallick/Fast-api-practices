names = ["sayak", "ramesh", "mohan"]
nums = [139, 56, 32, 87, 45, 49]

print(nums[2:])

print(nums + names)
mix = [nums, names]
print(mix)
print(mix[0][3])
print(mix[1][1])

print(nums.count(56))
nums.append(78)
print(nums)
nums.remove(32)
print(nums)

nums.pop(4)
print(nums)
del nums[2:4]
print(nums)

nums.extend([32, 234, 34, 435])
print(nums)

nums[2:4] = [54, 76]
print(nums)