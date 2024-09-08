n=int(input())
for i in range(1,n+1):
    if i < n:
        space = " " * (n-i)
        star="*" * i
        print(space + star)
    else:
        print("#" * n)
