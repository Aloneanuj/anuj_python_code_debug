# Q3. Create a function findLargest that accepts an List of Integers and returns 
# the largest number from the list. 
def findLargest (num_list):
    max_num= max(num_list)
    print("using the max function ",max_num)
    temp=num_list[0]
    for i in range(0, len(num_list)):
        if num_list[i]> temp:
            temp= num_list[i]
    print(temp)

num_list = [4,500,8,9,6,99,3]     
findLargest(num_list)   