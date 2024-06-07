# Q5. Create a function updateOddEven that accepts an List of Integers and 
# update all the even numbers to 0 and update all the odd numbers to 1.
def updateOddEven (lst):
    for i in range(0, len(lst)):
        if lst[i]%2==0:
            lst[i]=0
        else: 
            lst[i]=1
    # print(lst)
        
    
    
lst = [4,7,9,6,3,5,4,89,4,11]
updateOddEven(lst)
print(lst)






