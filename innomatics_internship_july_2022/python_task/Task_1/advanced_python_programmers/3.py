# input the list
n = int(input("Enter number of kids : "))
candies = []
for i in range(0, n):
    print(f"Enter the candies with {i+1} kid:  ")
    ele = int(input())

    candies.append(ele) # adding the element
print(f"The candies list is : {candies}")
extraCandies = int(input("enter the extra amount of candies you have : "))
li = []
for i in range(0, len(candies)):
    if candies[i] + extraCandies >= max(candies):
        li.append("true")
    else:
        li.append("false")
print(li)