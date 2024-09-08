n=int(input())
for i in range(1,n+1):
    space = "  " * (n-i)
    num = (str(i)+" ") * ((2*i)-1)
    print(space + num)