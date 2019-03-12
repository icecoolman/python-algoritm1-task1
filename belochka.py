def squirrel (N):
    N = N + 1
    sum = 1
    for i in range(1, N):
        sum = sum*i
    while(sum > 1):
        sum = sum/10
    sum = sum*10
    sum = int(sum)
    return sum
chislo = int(input())
print(squirrel(chislo))
