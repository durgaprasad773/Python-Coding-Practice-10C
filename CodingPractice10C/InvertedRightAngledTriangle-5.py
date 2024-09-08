n=int(input())
for i in range(n):
    space = "  " * i
    num = (str(n-i)+" ") * (n-i)
    print(space + num)