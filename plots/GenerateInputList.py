import csv
import os
import numpy as np
import matplotlib.pyplot as plt
from _socket import close

# zum vielen Testen: 
# os.remove('1.csv')

a = list(range(1,100))
b = []
# c = list(reversed(range(10)))
# d = []

# Reihenfolge der zahlen in der csv Datei bestimmen  
def put_in_RevOrder_data():
    for i in range(len(a)):
        b.append(a.pop())
    return b
#
# def put_in_Ordered_data():
    # for i in range(len(c)):
        # d.append(c.pop())
    # return d

# Reihenfolgen ausführen
#put_in_Ordered_data()
put_in_RevOrder_data()



# Zahlenreihen speichern in externem File:
# optional verscheidene Zahlenfolgen in einzelnen reihen speichern
with open('1.csv', 'w', newline='') as file:
    writer = csv.writer(file, lineterminator = "")
    #writer = csv.writer(file, lineterminator = "")
    file.write(str(b))
    #file.write(str(d))
    print ("Done with generated List in csv")
    file.close()