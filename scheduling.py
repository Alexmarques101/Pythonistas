
# 2018-2019 Fundamentos de Programação (LTI)
# Grupo 24 - Pythonistas
# 39071 Alexandre Santos
# 53828 Vasco Oliveira

from copy import deepcopy
file1= '2019y03m20clients12h30.txt'
file2 = '2019y03m20experts12h30.txt'
from filesReading import readFile
from dateTime import strToDate, add_one_hour, add_half_hour

def scheduling (file1, file2):
    """
    Contrato escrever...
    """
    final = []
    clients = readFile(file1)
    experts = readFile(file2)
    client=0
    expert=0
    
    #Defining the header with half hour more
    #Possibly need to change this to account for 8h to 20h schedule
    header = deepcopy(clients[0])
    header = list(header) # transform to list so that we can change values. Tuples don't let it
    header[1] = add_half_hour(header[1])
    header[3] = 'Schedule:'
    
    for client in range(len(clients[1])): #itera sobre a lista dos clientes um a um
        for expert in range(len(experts[1])): #itera sobre a lista dos experts um a um
            
            #if the local is the same, if the service asked is addressed by expert,  quality of service (e.g. 4*),price asked by client higher than expert charges
            if (clients[1][client][1]== experts[1][expert][1]) and (clients[1][client][6] in experts [1][expert][2]) \
                and (clients[1][client][5] <= experts [1][expert][3]) and (clients[1][client][5] <= experts [1][expert][3]) \
                and (int(clients[1][client][4]) >= int(experts[1][expert][4])): #caso a cidade do cliente 1 coincida com a do expert 1 então devolve os dois, etc
                    
                    #When Expert finishes task after current time then he is available 1h after finishing his task
                    if strToDate(experts[1][expert][5],experts[1][expert][6]) > strToDate(experts[0][0],experts[0][1]):
                        
                        #experts[1][expert][6] = add_one_hour(strToDate(experts[1][expert][5],experts[1][expert][6])[1].strftime("%H:%M"))  #adding 1h to the expert availability                          
                        result= max(strToDate(clients[1][client][2],clients[1][client][3]),
                              max(strToDate(experts[1][expert][5],add_one_hour(experts[1][expert][6])),strToDate(experts[0][0],experts[0][1]))),\
                            clients[1][client][0],experts[1][expert][0]

                        final.append([result[0][0].strftime("%Y-%m-%d"), result[0][1].strftime("%H:%M"), result[1], result[2]])
                    #On the contrary, when he is without a task for some time, he is available at the header time of the file
                    else:
                        result= max(strToDate(clients[1][client][2],clients[1][client][3]),
                              max(strToDate(experts[1][expert][5],experts[1][expert][6]),strToDate(experts[0][0],experts[0][1]))),\
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
             final.append([header[0], header[1], schedule[1][j].pop(0), "declined"])
             #return final   

    #Sort the final list by date and hour, with 'declined' clients first.
    declinedList = []
    serviceList= []

    for line in final:
        if 'declined' in line:
            declinedList.append(line)
        else:
            serviceList.append(line)
        
    finalList = header + sorted(declinedList) + sorted(serviceList)
    
    return finalList
    
       
           