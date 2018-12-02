# 2018-2019 Fundamentos de Programação (LTI)
# Grupo 24 - Pythonistas
# 39071 Alexandre Santos
# 53828 Vasco Oliveira

import datetime as dt


def strToDate (date, hours):
    
    date = dt.datetime.strptime(date, '%Y-%m-%d') 
    hours = dt.datetime.strptime(hours, '%H:%M').time()
    return date, hours

#Function to add one hour to the finish time of expert task    
def add_one_hour(hours):

    t1 = dt.datetime.strptime(hours, '%H:%M')
    t2 = dt.datetime.strptime('01:00', '%H:%M')
    time_available = dt.datetime.strptime('00:00', '%H:%M')
    return (t1 - time_available + t2).time().strftime('%H:%M')
