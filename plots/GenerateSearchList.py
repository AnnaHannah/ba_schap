import sys
import csv
import os
import numpy as np
import matplotlib.pyplot as plt
import random
from _socket import close
from _operator import concat

# Beispiel test fälle mit Listen

data_list = []
a  = list(range(0,1200))
b  = list(range(0,1400))
c  = list(range(0,1600))
d  = list(range(0,1800))
e  = list(range(0,2000))
f  = list(range(0,2200))
g  = list(range(0,2400))
h  = list(range(0,2600))


# verteilungen:
def make_zickzack(list):
    max = list [-1]
    for i in list:
        if (i % 2 == 0):
           list[i] = 0
        else:
            list[i] = max 
            
    return list

def make_oneNumber(list, number):
    for i in list:
           list[i] = number
    return list

def make_oneCluster_left(list, x_spread):
    for i in list:
        y = random.randrange(0, x_spread)
        list[i] = y
    return list
         
def make_oneCluster_right(list, x_spread):
    max = list[-1]
    cluster_middle = (max - x_spread)
    for i in list:
        y = random.randrange(cluster_middle, max)
        list[i] = y
    return list

def make_oneCluster_middle(list, x_spread):
    max = list[-1]
    list_middle = int(max//2 - x_spread)
    list_middle_limit = list_middle + 2*x_spread
    for i in list:
        y = random.randrange(list_middle, list_middle_limit)
        list[i] = y
    return list
    
def make_total_random(list):
    # Achtung, es macht nur Sinn nach Elementen zusuchen die auch da sind! => maximum der gegeben Listen ist größtest Elemeent
    max = list [-1]
    for i in list:
        y = random.randrange(0, max)
        list[i] = y
    return list

def makeBigLists(listOfList):
    print("\n1. Generating with makeBigLists - method is starting")
    ouput_list=[]
    print("2. ... ")
    # verarbeitung der Listen mit verteilungen 
    
    make_oneCluster_middle(a,600)
    make_oneCluster_middle(b,700)
    make_oneCluster_middle(c,800)
    make_oneCluster_middle(d,900)
    make_oneCluster_middle(e,1000)
    make_oneCluster_middle(f,1100)
    make_oneCluster_middle(g,1200)
    make_oneCluster_middle(h,1300)
    
    # Beispiel um alle Listen anzuhängen  
    ouput_list.append(a) 
    ouput_list.append(b) 
    ouput_list.append(c) 
    ouput_list.append(d)   
    ouput_list.append(e) 
    ouput_list.append(f) 
    ouput_list.append(g)
    ouput_list.append(h)
    print ("3. Generated number of sublists/Testcase is: ", len(ouput_list))     
    return ouput_list


# erstelle test csv file mit mini data listen:
def writeMYfile(filename, data):
    with open (filename, 'w', newline='') as file:
        writer = csv.writer(file, delimiter =',')
        writer.writerows(data)      
    print ("\n-> Done with writing data in", filename)
    

if __name__ == "__main__":
    sys.setrecursionlimit(3000)
    print("\n !!! Recursion allowed in this program:", sys.getrecursionlimit())
    #print(make_zickzack(a))
    #print(make_oneCluster_middle(b, 2))
    #print(make_total_random(a))
  
    
    # schreibe test1 csv mit datalisten:
    dataForCSV = makeBigLists(data_list)
    writeMYfile("searchLists.csv", dataForCSV) 
