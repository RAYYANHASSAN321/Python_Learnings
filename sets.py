# ------------------------ Sets -----------------------------#
nums = set()
nums = {1 , 2 , 4 , 5 , 6 , 3 , 2}

print(nums)

nums.add(7) # to add a new value
print(nums)

nums.update([9 , 10 , 8]) # to add multiple values
print(nums)

nums.remove(10) # to remove any value / element but if value doesn't exist error will be shown
print(nums)

nums.discard(10) # to remove any value but if value doesn't exist error will be shown
print(nums)

nums.pop() # to remove random element
print(nums)

nums.clear() # to remove all elements from set
print(nums)

s1 = {1 , 5 , 3 , 5 , 2 , 4}
s2 = {7 , 4 , 8 , 9 , 2 , 8}

print(s1.union(s2)) # to show unique values from both sets and align in asscending order 

print(s1.intersection(s2)) # to show common value from both sets

print(s1.difference(s2)) # s1 - s2

print(s2.difference(s2)) # s2 - s1

