def odometer(oksana):
    sum = 0
    sum = oksana[0]*oksana[1]
    for i in range(2,len(oksana)-1,2):
        sum = sum + oksana[i]*(oksana[i+1]-oksana[i-1])
    return sum
