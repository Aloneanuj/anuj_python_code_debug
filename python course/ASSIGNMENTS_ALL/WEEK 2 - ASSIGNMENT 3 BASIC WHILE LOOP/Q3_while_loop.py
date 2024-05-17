'''Q3. Create a function named multiplicationTable that takes an integer num as an argument. 
Print the multiplication table of that number up to 10 numbers. '''
# def multiplicationTable(num):
#     i=num
#     j=1
#     multiply=1
#     while(j<=10):
#         multiply=i*j
#         print(multiply)
#         j+=1

# multiplicationTable(2)

# ----------------------
def multiplicationTable(num):
    i=1
    while i<=10:
        print(f"{num} * {i} = {num*i}")
        i+=1

multiplicationTable(2)