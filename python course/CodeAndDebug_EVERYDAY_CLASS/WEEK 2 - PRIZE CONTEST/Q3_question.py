'''
Q3. Make a function named printWords which accepts an integer n from
the user. Print the number as words.
Example:
printWords(91)
printWords(100001)
printWords(1254)

Nine One (OUTPUT)
one zero zero zero zero one (OUTPUT)
one two five four (OUTPUT)


'''
def reverse(num):
    rev=0
    while num!=0:
        r=num%10
        rev=rev*10+r
        num=num//10
    return rev

def printWords(n):
    reverse_number = reverse(n) 
    # rev=0
    while reverse_number!=0:
        r = reverse_number%10
        # rev = rev * 10 + r
        if r == 0:
            print("Zero",end=" ")
        elif r== 1:
            print("ONE",end=" ")
        elif r == 2:
            print("Two",end=" ")
        elif r== 3:
            print("Three",end=" ")
        elif r == 4:
            print("Four",end=" ")
        elif r == 5:
            print("Five",end=" ")
        elif r== 6:
            print("Six",end=" ")
        elif r == 7:
            print("Seven",end=" ")
        elif r== 8:
            print("Eight",end=" ")
        else:
            print("Nine",end=" ")
        reverse_number = reverse_number//10

num = int (input("Please enter the number : "))    
printWords(num)


