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
    # print(bst.counterNodes, " so many Nodes were made in Tree")
    delta_time = (int(end-start)/(100000))
    #assert delta_time is delta_time > 0," \n delta_time: %r has probably an time overflow " % delta_time
    
    #print(int(delta_time), " total_seconds() needed for input in RedBlackTree")
    return (int(delta_time))

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
    #print(skl.counterNodes(), " so many Nodes were made in Skiplist")
    delta_time = (int(end-start)//(100000))
    # assert delta_time is delta_time > 0," \n delta_time: %r has probably an time overflow " % delta_time
    #print(int(delta_time), "total_seconds() needed for input in SkipList")
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
    #assert delta_time is delta_time > 0," \n delta_time: %r has probably an time overflow " % delta_time
    #print (bst.counterNodes, " so many new Nodes were made in Tree")
    #print (int(delta_time), " total_seconds() needed for searching all Nodes in RedBlackTree")
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
    #assert delta_time is delta_time > 0," \n delta_time: %r has probably an time overflow " % delta_time
    #print (bst.counterNodes, " so many new Nodes were made in Tree")
    #print (int(delta_time), " total_seconds() needed for searching all Nodes in RedBlackTree")
    return int(delta_time)

def messureTime_SEARCH_Skiplist(inputList):
    if type(inputList) != list:
        inputList = inputList.tolist()
    
    # init für Blackred tree
    delta_time = 0.0
    searchlist = inputList

    skl = SkipList()
    skl.insertMultipleElem(inputList)
    #start timer
    start = time.perf_counter_ns()
    
    skl.findMultipleElem(searchlist)
    
    end = time.perf_counter_ns()
    #print ("start and end time:", start, end)
    delta_time = (end-start)
    #assert delta_time is delta_time > 0," \n delta_time: %r has probably an time overflow " % delta_time
    #print (skl.counterNodes(), " so many new Nodes were made in Skiplist")
    #print (int(delta_time), " total_seconds() needed for searching all Nodes in Skiplist")
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


def subListLengh(listOfLists):
    lenSublist_Output = [] 
    for list in listOfLists:
        lenSublist_Output.append(len(list))
    #print ("the lenght of every SubList in ListOfLists is", lenSublist_Output)
    return lenSublist_Output 

if __name__ == "__main__":
    
    # Je nach dem wie stark die Rechenleistung ist, bitte begrenzen:
    sys.setrecursionlimit(20000)
    
    #DS Time performance mit der jewels der sublist anstellen: INSERT
    listOfLists = readMYfile('test1.csv')
    insert_TimeRBT = timePerformanceINSERTRedBlackTree(listOfLists)

    listOfLists = readMYfile('test1.csv')
    insert_TimeSKL = timePerformanceINSERTSkipList(listOfLists)
 
    
    listOfLists = readMYfile('test1.csv')
    search_TimeRBT = timePerformanceSEARCHRedBlackTree(listOfLists)
    
    listOfLists = readMYfile('test1.csv')
    search_TimeSKL = timePerformanceSEARCHSkipList(listOfLists)
    
    listOfLists = readMYfile('test1.csv')
    search_MinMaxFinger_TimeRBT = timePerformanceMinMaxFingerSEARCHRedBlackTree(listOfLists)
    
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
    plt1.set_xlabel('Number of Values from CSV')
    
    # Vermutung python cache alle input werte, sodass die suche 0 sec dauert...
    plt2.plot (numberOfInputValuesRBT, search_TimeRBT, 'bo', linestyle='--', label=r'Rootsearch time in RedBlackTree ') 
    plt2.plot (numberOfInputValuesSKL, search_MinMaxFinger_TimeRBT, 'go', linestyle='--', label=r'MinMax-Finger-Search time in RedBlackTree') 
    
    plt3.plot (numberOfInputValuesSKL, search_TimeSKL, 'ko', linestyle='--', label=r'Rootsearch time in SkipList ') 
    
    plt4.plot (numberOfInputValuesSKL, search_TimeSKL, 'ko', linestyle='--', label=r'Rootsearch time in SkipList ') 
    
    plt2.set_ylabel('Time in nano sec')
    plt2.set_xlabel('Number of Values from CSV')
    
    # Legende einblenden:
    plt1.legend(loc='upper left', frameon=True)
    plt2.legend(loc='upper right', frameon=True)
    plt3.legend(loc='upper right', frameon=True)
   
    print ("Plot is on Display")
    plt.show()
    

