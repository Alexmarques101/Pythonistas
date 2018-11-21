# 2018-2019 Fundamentos de Programação (LTI)
# Grupo 24 - Pythonistas
# 39071 Alexandre Santos
# 53828 Vasco Oliveira

fileName = '2019y01m12clients09h00.txt'
def readFile(fileName):
    """
    Converts a given file listing experts, clients or scheduling into a collection
    Requires: fileName is str, the name of a .txt file listing experts, clients or scheduling
    following the format specified in the project.
    Ensures: list whose first element is a tuple and the second is a list of lists
    """
    outputList = []
    
    outputList.append(readHeader(fileName))
    
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
    file = fileIn.readlines()
    file = [x.strip().replace("\n", "").replace(" ", "") for x in file]
    file = [x.split(",") for x in file]
    #experts = [line for line in experts]
    outputList.append(file)
    return outputList



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


