lst = [8, 96, 85, 25, 45,412,65,2589,12,1,89]

print("print value at 3 index : ",lst[3])   
print("print value at first index (0) : ",lst[0])   
print("print value at last index : ",lst[-1])
print("print value at last second index : ",lst[-2])
print("print value at last fifth index : ",lst[-5])
print("print value at 5 index : ",lst[5])

print("-----------Iterates and print all the values--------")
for i in range(0, 10):
    print(lst[i], end=" ")

print("\n -----------Iterates and print all the values in reverse order--------")

for i in range (10 ,-1,-1):
    print(lst[i], end=" ")

print("\n-----------Iterates and print all the values using len function--------")
for i in range(0, len(lst)):
    print(lst[i], end=" ")

print("\n-----------Iterates and print all the values in reverse using len function--------")
for i in range (len(lst)-1 ,-1,-1):
    print(lst[i], end=" ")
