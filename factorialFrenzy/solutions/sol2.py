n = int(input())

if n == 0:
    print(1)
    exit()

fac = 1
for i in range(1, n + 1):
    fac *= i


print(fac)
