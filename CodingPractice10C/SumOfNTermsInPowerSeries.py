m=int(input())
n=int(input())
sum_of = 0
power = 1
for i in range(1,n+1):
    sum_of = sum_of + (m ** power)
    power = power + 2
print(sum_of)