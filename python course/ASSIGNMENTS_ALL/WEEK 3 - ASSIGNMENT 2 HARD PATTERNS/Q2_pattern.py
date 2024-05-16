'''
        1
      2 1
    3 2 1
  4 3 2 1
5 4 3 2 1
'''
def pattern(n):
    for i in range (1, n + 1):
        for j in range(n, i,-1):
            print(" ",end=" ")
        for l in range (i, 0,-1):
            print(l, end=" ")
        print()
pattern(5)