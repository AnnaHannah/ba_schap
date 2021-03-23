import sys
from _overlapped import NULL
from skiplist.LinkedList import LinkedList
# Implementing Skiplist in Python
from random import randint, seed
from time import sleep
from tkinter.tix import INTEGER
from operator import contains
from numpy.core.defchararray import isdigit, isdecimal


class SkipNode():
 
    def __init__(self, height = 0, elem = None):
        self.height = 0
        self.elem = elem
        self.next = [None]*height

class SkipList():

    def __init__(self):
        self.head = SkipNode()
        self.len = 0
        # max hight of a specitifc Node - it is always smaller then Skiplist hight
        self.maxHeight = 0 

    def __len__(self):
        return self.len

    def findElem(self, elem):
        # update = self.updateList(elem)
        if elem == None:
            return (print( "Error you need to put an Element in FindElem()"))
        if elem != None:
            for i in (range(0, len(self.head.next), 1)):
                x = self.head
                while x.next[i] != None: 
                    x = x.next[i] 
                    if x.elem == elem: 
                        return x.elem
            return None    
    
    def findNodeByElem(self, elem, node):
        update = self.updateList(elem, node)
        if elem == None:
            #print("\n C2) findfindNodeByElemElem was given None", elem)
            return None
        else:
            if len(update) > len(self) and elem != None:
                candidate = update[0].next[0]
                if candidate != None and candidate.elem == elem:
                    #print("C2) findNodeByElem found this candidate:", candidate.elem)
                    return candidate

    def contains(self, elem):
        return (self.findElem(elem) != None)

    def randomHeight(self):
        height = 1
        while randint(1, 2) != 1:
            height += 1
        return height

    def updateList(self, elem, node):
        #print("B) in function updateList() - jumpNextLine - this is number of clean lines:", [None]*self.maxHeight)
        update = [None]*self.maxHeight
        x = self.head
        for i in reversed(range(self.maxHeight)):
            # Jede Ebene durchgehen
            while x.next[i] != None and x.next[i].elem < elem:
                # alle elemente in der ebene durch gehen und beim richtigen Stoppen:
                x = x.next[i]
            update[i] = x
            #print("B) in function updateList() - jumpNextLine - this was updated:", elem)
        return update
        
    def insertElem(self, elem):
        #if self.findElem(elem) != None:
            #print("A) NO insert Elem() for element in Skiplist, it seems to be there:", elem) 
        
        if self.findElem(elem) == None:
            #print("\nA) function insertElem() start Skipnode:", elem)
            # make new Node with element
            node = SkipNode(self.randomHeight(), elem)
            self.maxHeight = max(self.maxHeight, len(node.next))
            
            while len(self.head.next) < len(node.next):
                self.head.next.append(None)
                #print("A) insertElem is doing: append", node.elem)
    
            update = self.updateList(elem, node)            
            if self.findNodeByElem(elem, update) == None:
                #print("A) in function insertElem() this will update:", elem)
                for i in range(0, len(node.next)):
                    node.next[i] = update[i].next[i]
                    update[i].next[i] = node
                    #print("A) in function insertElem() this is updated:", node.elem)
                self.len += 1
            else: return ''  
   
    def insertMultipleElem(self, list):
        # Listeneinträge Pop-> einzeln einfügen in Skipliste    
        while list.__len__() > 0:
            x = list.pop()
            self.insertElem(x)  
            
    def findMultipleElem(self, list):   
        foundList = []
        while list.__len__() > 0:
            x = list.pop()
            if self.findElem(x) != None:
                foundList.append(self.findElem(x))
        return foundList

    def delete(self, elem):
        x = self.findElfindNodeByElem
        if x != None:
            for i in reversed(range(len(x.next))):
                #print("\n delete was operating on:", x.elem)
                update[i].next[i] = x.next[i]
                if self.head.next[i] == None:
                    self.maxHeight -= 1
            self.len -= 1            
        
    def counterNodes(self):
        counter = 0
        for i in reversed(range(0, len(self.head.next), 1)):
            # Jede Ebene hat einen Kopf, der alleine ist schon 1 Wert
            x = self.head
            counter = counter + 1 
            while x.next[i] != None:  
                # jedes Element wird gezählt
                if x.elem != None:
                    counter = counter + 1
                x = x.next[i] 
        return counter            
                
    def printList(self):
        # indent = ""
        # Alle schichten der Skiplist durchgehen und immer 1 abziehen       
        for i in reversed(range(0, len(self.head.next), 1)):
            print ("\n------------------------------- Ebene Nummer", i)
            x = self.head
            while x.next[i] != None:  
                if x.elem != None:
                    sys.stdout.write(str(x.elem) + " ")
                x = x.next[i]
            if x.next[i] == None:
                    sys.stdout.write(str(x.elem) + " ")

        # ohne das return erscheint ein None
        return ''
            
if __name__ == "__main__":
    skl = SkipList()
    inputList = list(range(1,1000))
    skl.insertMultipleElem(inputList)
    print(skl.counterNodes())
    # print("__len__ funktion says:", skl.__len__())
    # searchlist = [1,2,3,99,'aaa']
    # skl.printList()
    # print ("\n")
    # print ("Ergebnis von Suche skl.findMultipleElem (" +str(searchlist) +") ist:", skl.findMultipleElem(searchlist) )     