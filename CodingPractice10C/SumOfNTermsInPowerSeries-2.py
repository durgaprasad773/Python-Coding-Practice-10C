x=int(input())
n=int(input())
power = 2
sum_of = 0
for i in range(1,n+1):
    sum_of = sum_of + (x ** power)
    power = power + 2
print(sum_of)