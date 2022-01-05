nums = input()
list = []
for i in range(len(nums)):
    list.append(nums[i] ** 2,)
    nums[i] = list[i]
nums.sort()
print(nums)
        
