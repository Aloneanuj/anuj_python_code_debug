lst = [4,5,3,6,9,7,4,5,55,45,2,1,222]
for i in lst:
    if i%2==0:
        print(i, end=" ")

# enumerate
print(list(enumerate(lst)))

for i,j in enumerate(lst):
    # print(i, end=" ")    #print all the index
    # print(j, end=" ")   #print all the values 
    
    print(f"index {i} value {j}")
    