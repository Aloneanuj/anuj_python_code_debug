# Q4. Create a function findSmallest that accepts an List of Integers and 
# returns the smallest number from the list.
def findSmallest(lst):
    smallest_num=min(lst)
    print(smallest_num)
    temp=lst[0]
    for i in range(len(lst)):
        if lst[i]<temp:
            temp=lst[i]
    print("Smallest Element: ",temp)
    
lst = [8,6,9,8,5,6,10,2,5,7,8,88]
findSmallest(lst)
