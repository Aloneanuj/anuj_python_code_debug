"""Create a function that takes three numbers as parameters and returns
the largest among them. Also if no arguments are passed, make sure the
parameters take default value as None and return answer as -1"""

def largest(num1= None, num2= None, num3= None):

    if num1!= None and num2!= None and num3 != None:
        largest_number =  max(num1, num2, num3)
        print("greatest number : ",largest_number)
    
    else:
       print(-1)

largest(56,96)