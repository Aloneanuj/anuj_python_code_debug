'''
        1
      2 1
    3 2 1
  4 3 2 1
5 4 3 2 1
'''


def pattern(n: int) -> None:
    for i in range(1, n + 1):
        for j in range(n - i):
            print(" ", end=" ")
        for k in range(i, 0, -1):
            print(k, end=" ")
        print()

pattern(5)