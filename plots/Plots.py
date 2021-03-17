import numpy as np
import matplotlib.pyplot as plt
import csv
from numpy.core.arrayprint import IntegerFormat
from fileinput import filename
import time 
from datetime import timedelta
import datetime
from numpy.core.defchararray import isdigit, isdecimal
from decimal import Decimal  

# my files BAUSTELLE
import GenerateInputList
import sys 
import os
sys.path.append('.. /ba_schap/red_black_tree/RedBlackTree')
import RedBlackTree 


# dummy Array wir immer mit Zero gesteckt
dummyArray2 = np.array([])
dummyArray = np.array([])


# converting every element to Integer
def convertCharToInteger(lines):
    csvValues = []
    
    for line in lines:
        for ch in line:
            if isdigit(ch):
                csvValues.append(int(ch)) 
            elif isdecimal(ch):
                csvValues.append(float(format(Decimal(ch))))      
    # print("charToInteger hat konvertiert aus csv:", csvValues)     
    return csvValues 

# files öffnen:
def openFile(filename):
    infile = open(filename,'r')
    slines = infile.readlines() 
    csvValues = convertCharToInteger (slines)      
    return csvValues

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
    delta_time = datetime.timedelta(seconds=24*60*60).total_seconds()*1000
    #print(int(delta_time), " with formula: (seconds=24*60*60).total_seconds() needed for input in RedBlackTree")
    return (int(delta_time))

def messureTimeSkipList (inputList):
    if type(inputList) != list:
        inputList = inputList.tolist()
    #start timer
    delta_time = 0
    start_time = time.monotonic()
    
    # init für Blackred tree
    skl = SkipList()
    skl.insertMultipleElem(inputList)
    
    # End Timer
    end_time = time.monotonic() 
    print(skl.counterNodes, " so many Nodes were made in Tree")
    delta_time = datetime.timedelta(seconds=24*60*60).total_seconds()*1000
    #print(int(delta_time), " with formula: (seconds=24*60*60).total_seconds() needed for input in RedBlackTree")
    return (int(delta_time))
    
    
if __name__ == "__main__":
    #open csv file
    csvValues = openFile('1.csv') 
    # print ("das ist aktueller wert von csvValues in main:", csvValues)
    
    # behelfs variablen, copien für später, Schreibschutz durch Array 
    csvValues1 = csvValues
    csvValues1 = np.array(csvValues1)
    csvValues2 = csvValues
    csvValues2 = np.array(csvValues2)
    csvValues3 = csvValues
    csvValues3 = np.array(csvValues3)

    # Red Black tree Performace time:
    timeRBT = messureTimeRedBlackTree(csvValues1)
    print("timeRBT =", timeRBT)
    
    timeSKL = messureTimeSkipList(csvValues1)
    print("timeSKL =", timeSKL)

    # preparation for plot: 
    zeroArray = fillUpwithZero(dummyArray, csvValues2)
    # print("zero Array:", zeroArray)
  
    # needed right numbers of elements
    timeRBTArray= fillOneValue(dummyArray, csvValues3, timeRBT)
    # print ("timeRBTArray:", timeRBTArray)
    
    #actual plot
    fig, (plt1, plt2) = plt.subplots(2, 1)
    fig.suptitle(' Inputwerte von 1. Rot Schwarzbaum laufzeiten, 2. Skiplisten')
    
    plt1.plot (csvValues, zeroArray)
    plt1.set_xlabel('x3: random  Integer in CSV ausgelesen')
    plt1.set_ylabel('kombiniert mit Zeros')
    
    plt2.plot (csvValues, timeRBTArray)
    plt2.set_xlabel('x3: random  Integer in CSV ausgelesen')
    plt2.set_ylabel('kombiniert mit benötigter Zeit für csv array')
    # Beschriftungen in graph
    
    # print für plots
    plt.show()

