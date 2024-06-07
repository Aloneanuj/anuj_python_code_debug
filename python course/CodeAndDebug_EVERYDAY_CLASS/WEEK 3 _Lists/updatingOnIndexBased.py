# update the element of list with '0' which is at even index using function
# input = [54,43,19,85,11,94,32]
# output = [0, 43, 0, 85, 0, 94, 0]


def update_list_elemet_by_index(my_list):
    for i in range (0, len(my_list)):
        if i %2==0:
            my_list[i]=0
            
def update_list_elemet_by_value(my_list):
    for i in range (0, len(my_list)):
        if my_list[i] %2==0:
            my_list[i]=0


my_list = [54,43,19,85,11,94,32]

update_list_elemet_by_index(my_list)
print(my_list)

update_list_elemet_by_value(my_list)
print(my_list)