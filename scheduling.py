#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 16:01:31 2018

@author: alexandremarquesdossantos
"""
file1= '2019y01m12clients09h00.txt'
file2 = '2019y01m12experts09h30.txt'
from filesReading import readFile
def scheduling (file1, file2):
    """
    Contrato escrever...
    """
    clients = readFile(file1)
    experts = readFile(file2)
    client=0
    expert=0
    for client in range(len(clients[1])): #itera sobre a lista dos clientes um a um
        for expert in range(len(experts[1])): #itera sobre a lista dos experts um a um
            if (clients[1][client][1]== experts[1][expert][1]) and (clients[1][client][6] in experts [1][expert][2]): #caso a cidade do cliente 1 coincida com a do expert 1 então devolve os dois, etc
                print(clients[1][client][0:],experts[1][expert][0:])
                
                