'''def solution(A)
that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.
For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.
Given A = [1, 2, 3], the function should return 4.
Given A = [-1, -3], the function should return 1.
Write an efficient algorithm for the following assumptions:
• N is an integer within the range [1..100,000];
• each element of array A is an integer within the range [-1,000,000..1,000,000].'''


def solution(A):
    smallest = min(A)
    greater = max(A)
    if greater<=0:
        print(1)
    else:
        for i in range(smallest, greater+1):
            if i not in A:
                return i
        return i+1
# A=[1, 3, 6, 4, 1, 2]


# Get the number of elements from the user
num_elements = int(input("Enter the number of elements: "))
# Create an empty list
A = []
# Loop to get user input for each element
for i in range(num_elements):
  element = int(input(f"Enter element {i+1}: "))
  A.append(element)

print("Your list:", A)

result=solution(A)
print(result)