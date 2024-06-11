my_list = [5,4,5,8,6,3,1,44,8715,1,512,2,145]
# # append()-----------------
# my_list.append(100)  #insert value 100 at the last
# print(my_list)
# my_list.append(200)  #insert value 200 at the last after 100
# print(my_list)

# # insert()-----------------------
# print("-------------insert------------")
# my_list.insert(4, 50)  #insert value 50 at index 4 after 100
# my_list.insert(400, 10)  #insert value 10 at the last if that index is not present 
# my_list.insert(50, 700)  #insert value 700 at the last if that index is not present 
# print(my_list)

my_list.pop() # remove the value from last
removed_element= my_list.pop()
print("removed element = :", removed_element)
my_list.pop(5) # remove the data from index 5
my_list.pop()
print(my_list)
