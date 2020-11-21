def ConquestCampaign(N,M,L,battalion):
    mas = [[]] 
    dni = 1
    # формируем массив
    for i in range(N): 
        mas.append([])
        for j in range(M):
            mas[i].append(0)
    #метим места высадки
    for i in range(0,len(battalion),2):
        k = battalion[i] - 1
        l = battalion[i+1] - 1
        mas[k][l] += 1
    chit = 0
    #захватываем территорию
    while( L < M*N):
        for i in range(N):
            for j in range(M):
                if(mas[i][j] !=0 and j <= M-2 and i <= N-2 and i >= 1 and j >= 1):
                    mas[i-1][j] =+1
                    mas[i+1][j] =+1
                    mas[i][j+1] =+1
                    mas[i][j-1] =+1
                if(mas[i][j] != 0):
                    chit += 1
                L =+ chit
        dni += 1
    return dni
