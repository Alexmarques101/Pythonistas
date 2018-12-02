# 2018-2019 Fundamentos de Programação (LTI)
# Grupo 24 - Pythonistas
# 39071 Alexandre Santos
# 53828 Vasco Oliveira

from copy import deepcopy
file1= '2019y02m15clients10h30.txt'
file2 = '2019y02m15experts10h30.txt'
from filesReading import readFile
from dateTime import strToDate

def scheduling (file1, file2):
    """
    Contrato escrever...
    """
    final = []
    clients = readFile(file1)
    experts = readFile(file2)
    client=0
    expert=0
    for client in range(len(clients[1])): #itera sobre a lista dos clientes um a um
        for expert in range(len(experts[1])): #itera sobre a lista dos experts um a um
            
            #O especialista a quem é atribuído o atendimento tem de ser um profissional no domínio do pedido,
            #com um nível de reputação igual ou superior ao pretendido pelo cliente, a cobrar à hora, no máximo, aquilo que o cliente aceita pagar, 
            #e a trabalhar na zona/cidade para que é feito o pedido.
            if (clients[1][client][1]== experts[1][expert][1]) and (clients[1][client][6] in experts [1][expert][2]) \
                and (clients[1][client][5] <= experts [1][expert][3]) and (clients[1][client][5] <= experts [1][expert][3]) \
                and (int(clients[1][client][4]) >= int(experts[1][expert][4])): #caso a cidade do cliente 1 coincida com a do expert 1 então devolve os dois, etc
                    
                    result= max(strToDate(clients[1][client][2],clients[1][client][3]),
                              strToDate(experts[1][expert][5],experts[1][expert][6])),\
                            clients[1][client][0],experts[1][expert][0]
                            
                    
                    final.append([result[0][0].strftime("%Y-%m-%d"), result[0][1].strftime("%H:%M"), result[1], result[2]])
                    
    #Auxiliar list to facilitate
    auxiliar = []
    i=0
    for i in range(len(final)):
        auxiliar.append(final[i][2])
    
   #Including clients with no match.
   #Created a deep copy of clients and then for each one that is not in Auxiliar list, remove it and
   #include it in final
    schedule = deepcopy(clients)
    j=0
    for j in range(len(clients[1])):
        if clients[1][j][0] not in auxiliar:
            final.append([schedule[1][j].pop(2), schedule[1][j].pop(2), schedule[1][j].pop(0), "declined"])
            
    return final       

    #Fiz uns testes mas parece que as datas não estão a sair bem...
    
       
           
           
           
                