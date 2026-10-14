d = 32
j = 32

print(d is j) # True, because both d and j point to the same integer object in memory.

list1 = [3,343,"jls"]

list2 = [3,343,"jls"]
print(list1 is list2)# Different objects in memory, so it will return False