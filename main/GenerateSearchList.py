import sys
import csv
import os
import numpy as np
import matplotlib.pyplot as plt
import random
from _socket import close
from _operator import concat

# my files BAUSTELLE
import sys 

# try to find Modules RedBlackTree and Skiplist 
from red_black_tree.RedBlackTree import * 
from skiplist.SkipList import * 
from fingerManagement.MinMaxFinger import *
from fingerManagement.LazyFinger import *
import logging

# Beispiel test fälle mit Listen

data_list = []
x = [1]
a = list(range(1,25))
b = list(range(1,50))
c = list(range(1,75))
d = list(range(1,100))
e = list(range(1,125))
f = list(range(1,150))
g = list(range(1,175))
h = list(range(1,200))

# verteilungen:

def make_oneNumber(list, number):
    for i in list:
           list[i] = number
    return list

def make_zickzack(list):
    max = int(list[-1])
    res = []
    for i in list:
        if (i % 2 != 0):
           res.append(1) 
        else:
           res.append(max)  
    #print ("make_zickzack %r list lenght with list:" % str(len(res)+1),  res )
    print (res)
    return res

def make_oneCluster_left(list, x_spread):
    res = []
    for i in list:
        y = random.randrange(0, x_spread)
        res.append(y)
    return res
         
def make_oneCluster_right(list, x_spread):
    max = int(list[-1])
    res = []
    cluster_middle = (max - x_spread)
    for i in list:
        y = random.randrange(cluster_middle, max)
        res.append(y)
    return res

def make_oneCluster_middle(list, x_spread):
    res = []
    max = int(list[-1])
    list_middle = int(max//2 - x_spread)
    list_middle_limit = list_middle + 2*x_spread
    for i in list:
        y = random.randrange(list_middle, list_middle_limit)
        res.append(y)
    return res
    
def make_total_random(list):
    # Achtung, es macht nur Sinn nach Elementen zusuchen die auch da sind! => maximum der gegeben Listen ist größtest Elemeent
    res=[]
    max = int(list [-1])
    for i in list:
        y = random.randrange(0, max)
        res.append(y)
    return res

# --------------------------------------------------------------------------------

def makeBigLists(listOfList):
    print("\n1. Generating with makeBigLists - method is starting")
    ouput_list=[]
    print("2. ... ")
    # verarbeitung der Listen mit verteilungen 
    a_new = []
    b_new = []
    c_new = []
    d_new = []
    e_new = []
    f_new = []
    g_new = []
    h_new = []

    a_new = make_zickzack(a)
    b_new = make_zickzack(b)
    c_new = make_zickzack(c)
    d_new = make_zickzack(d)
    e_new = make_zickzack(e)
    f_new = make_zickzack(f)
    g_new = make_zickzack(g)
    h_new = make_zickzack(h)

    # Logging for easy study
    logging.info("\n first list is logged here:")
    logging.info ("\n a_new = % r" % a_new)
    
    # Beispiel um alle Listen anzuhängen 
    ouput_list.append(x) 
    ouput_list.append(a_new)
    ouput_list.append(b_new)
    ouput_list.append(c_new)
    ouput_list.append(d_new)
    ouput_list.append(e_new)
    ouput_list.append(f_new)
    ouput_list.append(g_new)
    ouput_list.append(h_new)
    print ("3. Generated number of sublists/Testcase is: ", len(ouput_list))     
    return ouput_list


# erstelle test csv file mit mini data listen:
def writeMYfile(filename, data):
    with open (filename, 'w', newline='') as file:
        writer = csv.writer(file, delimiter =',')
        writer.writerows(data)      
    print ("\n-> Done with writing data in", filename)
    

if __name__ == "__main__":
    logging.basicConfig(filename='logFILE-GenerateInputLists.log', encoding='utf-8', level=logging.DEBUG)
    logging.info("\n -> Recursion allowed in this program: %r" % sys.getrecursionlimit())


    sys.setrecursionlimit(3000)
    print("\n -> Recursion allowed in this program:", sys.getrecursionlimit())
    #print(make_zickzack(a))
    #print(make_oneCluster_middle(b, 2))
    #print(make_total_random(a))
  
    
    # schreibe test1 csv mit datalisten:
    dataForCSV = makeBigLists(data_list)
    writeMYfile("searchLists.csv", dataForCSV) 
