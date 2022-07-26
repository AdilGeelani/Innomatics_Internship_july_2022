nums = [1, 2, 3, 4]
li = []
for i in range(0, len(nums)):
    if i == 0:
        li.append(nums[i])
    else:
        li.append(li[i - 1] + nums[i])
print(li)