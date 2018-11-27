# 2018-2019 Fundamentos de Programação (LTI)
# Grupo 24 - Pythonistas
# 39071 Alexandre Santos
# 53828 Vasco Oliveira

from datetime import datetime


def date (date):
    """
    Write contract
    """
    date = datetime.strptime(date, '%Y-%m-%d') 
    
    
    return date

def hours (hours):
    """
    Write contract
    """
    hours = datetime.strptime(hours, '%H:%M').time()
       
    return hours

def strToDate (date, hours):
    
    date = datetime.strptime(date, '%Y-%m-%d') 
    hours = datetime.strptime(hours, '%H:%M').time()
    return date, hours