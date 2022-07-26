
def shuffle(nums, n): # nums is a list containing 2n number of elements
    li = []
    for i in range(0, len(nums)):
        if i % 2 == 0:
            li.append(nums[int(i / 2)])
        else:
            li.append(nums[int(n + (i / 2))])
    return li
print(shuffle(nums = [1, 2, 3, 4, 5, 6], n = 3))