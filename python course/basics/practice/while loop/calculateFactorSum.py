# calculate the sum of all the factor of a number

def calculateFactorSum(n1, n2):
  i=1
  total =0
  while i <= n1:
    if i% n2 ==0:
      total = total + i
    i+=1
  return total
  
result = calculateFactorSum(30, 7)
print(result)