import numpy as np
import matplotlib.pyplot as plt
import csv
from numpy.core.arrayprint import IntegerFormat
from fileinput import filename
import time 
from datetime import timedelta
import datetime
from numpy.core.defchararray import isdigit, isdecimal, isnumeric
from decimal import Decimal  
import csv
import os
import numpy as np
import matplotlib.pyplot as plt
from _socket import close
from _operator import concat

# my files BAUSTELLE
import GenerateInputList
import sys 
import os
# try to find Modules RedBlackTree and Skiplist 
from red_black_tree.RedBlackTree import * 
from skiplist.SkipList import * 
from matplotlib.pyplot import title
from unicodedata import numeric
    
# dummy Array wir immer mit Zero gesteckt
dummyArray2 = np.array([])
dummyArray1 = np.array([])


# converting every element to Integer
def convertCharToInteger(lines):
    csvValues = []
    for line in lines:
        for ch in line:
            # isdigit runs only from 0-9, but i need loger numbers
            if isnumeric(ch) == True:
                csvValues.append(int(ch))                 
            elif isdecimal(ch):
                csvValues.append(float(format(Decimal(ch))))      
    # print("charToInteger hat konvertiert aus csv:", csvValues)     
    return csvValues 
    
def saveReadingInNewFile(numbers):
    with open('2.csv', 'w', newline='') as file:
        writer = csv.writer(file, lineterminator = "")
        file.write(str(numbers))
        print ("Done with generated List in 2.csv")
    file.close()
           
# files öffnen:
def openFile(filename):
    infile = open(filename,'r')
    slines = infile.readlines() 
    csvValues = convertCharToInteger (slines)
    # für Später um nachzuvollziehen welche daten genau beim Convertieren geschädigt wurden:
    saveReadingInNewFile(csvValues)
    return csvValues 

# Ziel der funktion, file öffnen, alle Listen auslesen, alle stringsauslesen und in INT convertieren, 
# Liste von Listen zurückgeben
def readMYfile(filename):
    with open( filename) as csv_file:
        reader=csv.reader (csv_file, delimiter=',', skipinitialspace=True)
        
        output_list =[]
        line_count = 0
        
        for line in reader:
            new_list = []
            new_list.append(line)
            # entfernen von extra klammern
            simple_list = new_list.pop()
            # Alle string in liste zu INTEGER
            for i in range(0, len(simple_list)):
                simple_list[i]= int(simple_list[i])
            output_list.append(simple_list)
            
            line_count +=1
        print ("output_list after reading file (integer)", output_list)
        return output_list

   
# format problems
def fillUpwithZero(y_array, csvValues2):
    # print ("fill up with Zero, used scvValue list:", csvValues2)
    # make list to append Zero
    if type(y_array) != list:
        y_array = y_array.tolist()
    while len(csvValues2) > len(y_array):
        y_array.append(0)
   
    # print ("fill up with Zero, used other list:", y_array)
    y_array = np.array(y_array)
    return y_array

def fillOneValue(y_array, csvValues3, x):
    # type check
    if type(y_array) != list:
        y_array = y_array.tolist()
    
    while len(csvValues3) > len(y_array):
        y_array.append(x)
   
    y_array = np.array(y_array)
    return y_array

# perfirmance messurement
def messureTimeRedBlackTree (inputList):
    if type(inputList) != list:
        inputList = inputList.tolist()
    #start timer
    delta_time = 0
    start_time = time.monotonic()
    
    # init für Blackred tree
    bst = RedBlackTree()
    bst.insertMultipleElem(inputList)
    
    # End Timer
    end_time = time.monotonic() 
    print(bst.counterNodes, " so many Nodes were made in Tree")
    delta_time = datetime.timedelta(seconds=60).total_seconds()/60
    print(int(delta_time), " total_seconds() needed for input in RedBlackTree")
    numberOfNodesBST = bst.counterNodes
    return (int(delta_time))

def messureTimeSkipList(inputList):
    if type(inputList) != list:
        inputList = inputList.tolist()
    #start timer
    delta_time = 0
    start_time = time.monotonic()
    
    # init für Skiplist tree
    skl = SkipList()
    skl.insertMultipleElem(inputList)
    
    # End Timer
    end_time = time.monotonic() 
    
    print(skl.counterNodes(), " so many Nodes were made in Skiplist")
    delta_time = datetime.timedelta(seconds=60).total_seconds()/60
    print(int(delta_time), "total_seconds() needed for input in SkipLsit")
   
    numberOfNodesSKL = skl.counterNodes()
    return (int(delta_time))
    
    
if __name__ == "__main__":
    
    listOfLists = readMYfile('test1.csv')
    #open csv file
    csvValues = openFile('1.csv') 
    # Schreibschutz
    csvValues1 = csvValues
    csvValues1 = np.array(csvValues1)
    csvValues2 = csvValues
    csvValues2 = np.array(csvValues2)
    csvValues3 = csvValues
    csvValues3 = np.array(csvValues3)
    csvValues4 = csvValues
    csvValues4 = np.array(csvValues4)

    # Performace time:
    timeRBT = messureTimeRedBlackTree(csvValues1)
    # print("timeRBT =", timeRBT)
    timeSKL = messureTimeSkipList(csvValues2)
    # print("timeSKL =", timeSKL)

    # preparation for plot: 
    # zeroArray = fillUpwithZero(dummyArray, csvValues2)
  
    # Formating: needed right numbers of elements
    timeRBTArray = fillOneValue(dummyArray1, csvValues3, timeRBT)   
    timeSKLArray = fillOneValue(dummyArray2, csvValues4, timeSKL)
    
    # Actual plot
    # fig, (plt1, plt2) = plt.subplots(2, 1)
    # fig.suptitle('OBEN RotSchwarzBaum -- UNTEN SkipListe')
    fig, (plt1) = plt.subplots(1, 1)
    fig.suptitle('OBEN RotSchwarzBaum ROT -- UNTEN SkipListe BLAU')
    
    plt1.plot (csvValues3, timeRBTArray, 'r+')
    plt1.plot (csvValues4, timeSKLArray, 'bx')
    print ("this is csvValues4, with timeRBTArray:", csvValues3, timeSKLArray)
    print ("this is csvValues3, with timeRBTArray:", csvValues3, timeRBTArray)

    # plt1.plot (csvValues4, csvValues4)
    plt1.set_ylabel('time in Sec')
    plt1.set_xlabel('Wertebereich der Imputwerte')
    
    # plt2.plot (csvValues4, timeSKLArray)
    # plt1.plot (csvValues4, csvValues4)
    # plt2.set_ylabel('SKL time')
    # plt2.set_xlabel('Wertebereich der Imputwerte')
    # Beschriftungen in graph
    
    # print für plots
    plt.show()

