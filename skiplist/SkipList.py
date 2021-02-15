import sys
from _overlapped import NULL
from LinkedList import LinkedList
# Implementing Skiplist in Python
from random import randint, seed
from tkinter.tix import INTEGER


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

    def find(self, elem, update = None):
        if update == None:
            update = self.updateList(elem)
        if len(update) > 0:
            candidate = update[0].next[0]
            if candidate != None and candidate.elem == elem:
                return candidate
        return None
    
    def contains(self, elem, update = None):
        return self.find(elem, update) != None

    def randomHeight(self):
        height = 1
        while randint(1, 2) != 1:
            height += 1
        return height

    def updateList(self, elem):
        update = [None]*self.maxHeight
        x = self.head
        for i in reversed(range(self.maxHeight)):
            while x.next[i] != None and x.next[i].elem < elem:
                x = x.next[i]
            update[i] = x
        return update
        
    def insertElem(self, elem):

        node = SkipNode(self.randomHeight(), elem)

        self.maxHeight = max(self.maxHeight, len(node.next))
        while len(self.head.next) < len(node.next):
            self.head.next.append(None)

        update = self.updateList(elem)            
        if self.find(elem, update) == None:
            for i in range(len(node.next)):
                node.next[i] = update[i].next[i]
                update[i].next[i] = node
            self.len += 1
    
    def insertMultipleElem(self, list):
        # Listeneinträge Pop-> einzeln einfügen in Skipliste    
        while list != []:
            x = list.pop()
            self.insertElem(x)
        

    def delete(self, elem):
        update = self.updateList(elem)
        x = self.find(elem, update)
        if x != None:
            for i in reversed(range(len(x.next))):
                update[i].next[i] = x.next[i]
                if self.head.next[i] == None:
                    self.maxHeight -= 1
            self.len -= 1            
                
    def printList(self):
        # Alle schichten der Skiplist durchgehen und immer 1 abziehen        
        for i in range(len(self.head.next)-1, -1, -1):
            print (i)
            x = self.head
            while x.next[i] != None:
                print (x.next[i].elem)
                x = x.next[i]
            print (" ")
        # ohne das return erscheint ein None
        return ''
            
if __name__ == "__main__":
    skl = SkipList()
    list = [1,2,3]
    skl.insertMultipleElem(list)
    

    
     
        