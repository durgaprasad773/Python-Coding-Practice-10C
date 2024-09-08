n=int(input())
for i in range(n):
    space = " " * i
    star="*" * ((2*(n-i)) -1)
    print(space + star)