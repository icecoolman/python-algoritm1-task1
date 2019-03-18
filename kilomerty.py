def odometer(oksana):
    sum = 0 
    for i in range(0,len(oksana),2):
        sum = sum + oksana[i]
    return sum
print(odometer([10,1,20,2]))
