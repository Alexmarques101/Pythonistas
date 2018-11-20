# 2018-2019 Fundamentos de Programação (LTI)
# Grupo 24 - Pythonistas
# 39071 Alexandre Santos
# 53828 Vasco Oliveira

fileName = '2019y01m12clients09h00.txt'
def readExpertsFile(fileName):
    """
    Converts a given file listing experts into a collection
    Requires: fileName is str, the name of a .txt file listing experts,
    following the format specified in the project.
    Ensures: list whose first element is ... <to complete>
    """
    outputList = []
    
    #outputList.append(readHeader(fileName))
    
    fileIn = open(fileName, 'r')

    # ... <to complete>
    #Salta o cabeçalho
    fileIn.readline()
    fileIn.readline()
    fileIn.readline()
    fileIn.readline()
    fileIn.readline()
    fileIn.readline()
    fileIn.readline()
    experts = fileIn.readlines()
    experts = [x.strip().replace("\n", "") for x in experts]
    experts = [x.split(",") for x in experts]
    #experts = [line for line in experts]
    #outputList.append(experts)
    return experts



def readHeader(fileName):
    """
    Converts a given file listing experts into a tupple 
    Requires: fileName is str, the name of a .txt file listing experts,
    following the format specified in the project.
    Ensures: list whose first element is ... <to complete>
    """
    # ... <to complete>
    fileIn = open(fileName, 'r') #Inclui fileIn aqui para conseguir abrir o txt
    fileIn.readline()
    day = fileIn.readline().strip().replace("\n", "")
    fileIn.readline()
    time = fileIn.readline().strip().replace("\n", "")
    fileIn.readline()
    company = fileIn.readline().strip().replace("\n", "")
    #fileIn.readline()
    scope = fileIn.readline().strip().replace("\n", "")
    
    return (day, time, company, scope)


