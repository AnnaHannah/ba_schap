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
from matplotlib.pyplot import title
from unicodedata import numeric
from numpy import double

# my files BAUSTELLE
import GenerateInputList
import sys 

# try to find Modules RedBlackTree and Skiplist 
from red_black_tree.RedBlackTree import * 
from skiplist.SkipList import * 
from fingerManagement.MinMaxFinger import *
from fingerManagement.LazyFinger import *

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
        #print("\n -> Done reading File: ", filename)
        return output_list

def messureTime_INSERT_RedBlackTree (inputList):
    if type(inputList) != list:
        inputList = inputList.tolist()
    #start timer
    # start_time = time.monotonic()
    bst = RedBlackTree()
    start = time.perf_counter_ns()
    # init für Blackred tree
    
    bst.insertMultipleElem(inputList)
    
    # End Timer 
    end  = time.perf_counter_ns()
    delta_time = 0
    delta_time = (int(end-start)/(100000))
    return int(delta_time)

def messureTime_INSERT_SkipList(inputList):
    if type(inputList) != list:
        inputList = inputList.tolist()
    #start timer
    delta_time = 0
    skl = SkipList()
    #start_time = time.monotonic()
    start = time.perf_counter_ns()
    # init für Skiplist tree
   
    skl.insertMultipleElem(inputList)
    
    # End Timer
    end = time.perf_counter_ns()
    delta_time = (int(end-start)//(100000))
    return (int(delta_time))

def messureTime_SEARCH_RedBlackTree(inputList):
    if type(inputList) != list:
        inputList = inputList.tolist()
    
    # init für Blackred tree
    delta_time = 0.0
    searchlist = inputList
    
    bst = RedBlackTree()
    bst.insertMultipleElem(inputList)
    
    #start timer
    start = time.perf_counter_ns()
    
    bst.findMultipleElem(searchlist)

    end = time.perf_counter_ns()
    delta_time = (end-start)
    return int(delta_time)

def messureTime_MinMaxFingerSEARCH_RedBlackTree(inputList):
    if type(inputList) != list:
        inputList = inputList.tolist()
    
    # init für Blackred tree
    delta_time = 0.0
    searchlist = inputList
    
    bst = RedBlackTree()
    bst.insertMultipleElem(inputList)
    # set up Finger with given tree
    mmf = MinMaxFinger()
    mmf.maxiFinger = mmf.setMaxiFingerFrom(bst)
    mmf.miniFinger = mmf.setMiniFingerFrom(bst)
    
    #start timer
    start = time.perf_counter_ns()

    mmf.findMultipleElem_with_MinMaxFinger(bst, searchlist)
    
    end = time.perf_counter_ns()
    delta_time = (end-start)
    return int(delta_time)

def messureTime_LAZYFingerSEARCH_RedBlackTree(inputList):
    if type(inputList) != list:
        inputList = inputList.tolist()
    
    # init für Blackred tree
    delta_time = 0.0
    searchlist = inputList
    # set up tree
    bst = RedBlackTree()
    bst.insertMultipleElem(inputList)
    # set up Finger with given tree
    lf = LazyFinger()
    lf.LazyFinger = lf.setfirst_LazyFinger(bst)
    
    #start timer
    start = time.perf_counter_ns()

    lf.findMultipleElem_with_LazyFinger(bst, searchlist)
    
    end = time.perf_counter_ns()
    delta_time = (end-start)
    return int(delta_time)

def messureTime_SEARCH_Skiplist(inputList):
    if type(inputList) != list:
        inputList = inputList.tolist()
    
    # init für Skiplist
    delta_time = 0.0
    searchlist = inputList

    skl = SkipList()
    skl.insertMultipleElem(inputList)
    #start timer
    start = time.perf_counter_ns()
    
    skl.findMultipleElem(searchlist)
    
    end = time.perf_counter_ns()
    delta_time = (end-start)
    return int(delta_time)

def timePerformanceINSERTRedBlackTree(listOfLists):
    perf_OutputList = []   
    for list in listOfLists:
        timeRBT = messureTime_INSERT_RedBlackTree(list)
        perf_OutputList.append(timeRBT)
    print ("timePerformanceINSERTRedBlackTree has messured time pro list iteration, and will return:", perf_OutputList)
    return perf_OutputList

def timePerformanceINSERTSkipList(listOfLists):
    perf_OutputList = []   
    for list in listOfLists:
        timeSKL = messureTime_INSERT_SkipList(list)
        perf_OutputList.append(timeSKL)
    print ("timePerformanceINSERTSkipList has messured time pro list iteration, and will return:", perf_OutputList)
    return perf_OutputList

def timePerformanceSEARCHRedBlackTree(listOfLists):
    perf_OutputList = []   
    for list in listOfLists:
        timeRBT = messureTime_SEARCH_RedBlackTree(list)
        perf_OutputList.append(timeRBT)
    print ("timePerformanceSEARCHRedBlackTree has messured time pro list iteration, and will return:", perf_OutputList)
    return perf_OutputList

def timePerformanceSEARCHSkipList(listOfLists):
    perf_OutputList = []   
    for list in listOfLists:
        timeSKL = messureTime_SEARCH_Skiplist(list)
        perf_OutputList.append(timeSKL)
    print ("timePerformanceSEARCHSkipList has messured time pro list iteration, and will return:", perf_OutputList)
    return perf_OutputList
def timePerformanceMinMaxFingerSEARCHRedBlackTree (listOfLists):
    perf_OutputList = []   
    for list in listOfLists:
        timeSKL = messureTime_MinMaxFingerSEARCH_RedBlackTree(list)
        perf_OutputList.append(timeSKL)
    print ("timePerformanceMinMaxFingerSEARCHSkipList has messured time pro list iteration, and will return:", perf_OutputList)
    return perf_OutputList

def timePerformanceLAZYFingerSEARCHRedBlackTree(listOfLists):
    perf_OutputList = []   
    for list in listOfLists:
        timeSKL = messureTime_LAZYFingerSEARCH_RedBlackTree(list)
        perf_OutputList.append(timeSKL)
    print ("timePerformanceLAZYFingerSEARCHRedBlackTree has messured time pro list iteration, and will return:", perf_OutputList)
    return perf_OutputList


def subListLengh(listOfLists):
    lenSublist_Output = [] 
    for list in listOfLists:
        lenSublist_Output.append(len(list))
    #print ("the lenght of every SubList in ListOfLists is", lenSublist_Output)
    return lenSublist_Output 

if __name__ == "__main__":
    
    # Je nach dem wie stark die Rechenleistung ist, bitte begrenzen:
    sys.setrecursionlimit(20000)
    
    #Performance INSERT
    listOfLists = readMYfile('test1.csv')
    insert_TimeRBT = timePerformanceINSERTRedBlackTree(listOfLists)

    listOfLists = readMYfile('test1.csv')
    insert_TimeSKL = timePerformanceINSERTSkipList(listOfLists)
 
    #Performance ROOTSEARCH
    listOfLists = readMYfile('test1.csv')
    search_TimeRBT = timePerformanceSEARCHRedBlackTree(listOfLists)
    
    listOfLists = readMYfile('test1.csv')
    search_TimeSKL = timePerformanceSEARCHSkipList(listOfLists)
    
    #Performance FINGER SEARCH
    listOfLists = readMYfile('test1.csv')
    search_MinMaxFinger_TimeRBT = timePerformanceMinMaxFingerSEARCHRedBlackTree(listOfLists)
    
    listOfLists = readMYfile('test1.csv')
    search_LazyFinger_TimeRBT = timePerformanceLAZYFingerSEARCHRedBlackTree(listOfLists)
    
    # logischer weise hat diese Kennzahl das gleiche format wie List_performanceTime, gut für plot...
    # Anzahl der Input werte auslesen pro Liste
    listOfLists = readMYfile('test1.csv')
    numberOfInputValuesRBT = subListLengh(listOfLists)
    
    listOfLists = readMYfile('test1.csv')
    numberOfInputValuesSKL = subListLengh(listOfLists)

    
# ------------------------------
# Plot Idea: list lenght and time in Datastructure, global Time
    
    # Actual plot
    # https://www.grund-wissen.de/informatik/python/scipy/matplotlib.html
   
    
    fig, ((plt1, plt2), (plt3, plt4)) = plt.subplots(2, 2)
    fig.suptitle('Laufzeiten Rotschwarz Baum und Skiplist')
    
    plt1.plot (numberOfInputValuesRBT, insert_TimeRBT, 'ro', linestyle='--', label=r'insert time in RedBlackTree')
    plt1.plot (numberOfInputValuesSKL, insert_TimeSKL, 'mo', linestyle='--', label=r'insert time in SkipList')
    
    plt1.set_ylabel('Time in nano sec 10^(-6)')
    plt1.set_xlabel('Number of values per list from CSV')
    
    # Vermutung python cache alle input werte, sodass die suche 0 sec dauert...
    plt2.plot (numberOfInputValuesRBT, search_TimeRBT, 'bo', linestyle='--', label=r'Rootsearch time in RedBlackTree ') 
    plt2.plot (numberOfInputValuesSKL, search_MinMaxFinger_TimeRBT, 'go', linestyle='--', label=r'MinMax-Finger-Search time in RedBlackTree') 
    plt2.plot (numberOfInputValuesSKL, search_LazyFinger_TimeRBT, 'ko', linestyle='--', label=r'Lazy-Finger-Search time in RedBlackTree') 
    
    plt3.plot (numberOfInputValuesSKL, search_TimeSKL, 'ko', linestyle='--', label=r'Rootsearch time in SkipList ') 
    
    plt4.plot (numberOfInputValuesSKL, search_TimeSKL, 'ko', linestyle='--', label=r'Rootsearch time in SkipList ') 
    
    plt2.set_ylabel('Time in nano sec')
    plt2.set_xlabel('Number of Values from CSV')
    
    # Legende einblenden:
    plt1.legend(loc='upper left', frameon=True)
    plt2.legend(loc='upper right', frameon=True)
    plt3.legend(loc='upper right', frameon=True)
    plt4.legend(loc='upper right', frameon=True)
   
    print ("Plot is on Display")
    plt.show()
    

