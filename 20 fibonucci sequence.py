x = int(input().strip())

n1, n2 = 0, 1
for i in range(0, x):
    print(n1, end=' ')
    nth = n1 + n2
    n1 = n2
    n2 = nth
