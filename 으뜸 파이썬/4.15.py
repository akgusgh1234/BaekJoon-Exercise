def my_sort(*nums):
    a=[]
    for i in range(0,len(nums)):
        a.append(nums[i])
    a.sort()
    return a
print(my_sort(45,3,4,56,5))
