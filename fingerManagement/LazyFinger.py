# Lazy finger merkt sich immer das zuletzt gesuchte element und verwendet dieses Element als Startnode in der suchfunktion

# meine Datenstruckturen
from red_black_tree.RedBlackTree import * 
from skiplist.SkipList import * 
import csv


class Finger():
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None
        self.color = None
        
class LazyFinger():
    def __init__ (self):
        self.lazyFinger = Finger(None)
        
        # param to messure performance
        self.usedNodesInSearch = 0
        
        
    # set the first finger to the root (why not)      
    def setfirst_LazyFinger(self, tree):
        if type(tree)== RedBlackTree:    
            newLazyFinger = tree.getRoot()
            self.lazyFinger = newLazyFinger
           
            assert type(self.lazyFinger.data) or self.lazyFinger is not None, " \n %r is not a Finger, something went wrhong while setting up fisrt Lazy Finger:" % (self.lazyFinger.data)
            #print(" Error, something went wrong, while setting the first finger")
            return self.lazyFinger
    
    # update the finger after search
    def lazyFinger_search(self, tree, keyInInt):
        assert (type(self.lazyFinger) or self.lazyFinger.data) is not None, " \n %r is not a Finger, in this Tree only Lazy Finger as Finger accepted. \n Please modify your Lazyfinger" % (self.lazyFinger)
        
        if type(tree)== RedBlackTree:
            self.usedNodesInSearch += 1
            
            #print("-- lazyFinger_search searches for:", keyInInt)
            
            if keyInInt == self.lazyFinger.data:
                searchResult = self.lazyFinger
                #print ("1a) lazy finger %r was used for search result:" % self.lazyFinger.data, searchResult.data)
                #print ("1b) lazyFinger_search - self.usedNodesInSearch:", self.usedNodesInSearch)
                #print ("1c) lazyFinger_search - bst.usedNodesInSearch:", bst.usedNodesInSearch)
            else:
                searchResult = None
                print(searchResult)
                searchResult = tree.twoDirectSearch_Node(self.lazyFinger, keyInInt)
                
                #print ("2a) lazy finger %r was used for search result:" % self.lazyFinger.data, searchResult.data)
                #print ("2b) lazyFinger_search - self.usedNodesInSearch:", self.usedNodesInSearch)
                #print ("2c) lazyFinger_search - bst.usedNodesInSearch:", bst.usedNodesInSearch)
                print(searchResult)
                self.lazyFinger = searchResult
            #print ("Lazy Finger now set to:", self.lazyFinger.data)
            #print (searchResult.data == self.lazyFinger.data)
            
            return searchResult     
    
    def findMultipleElem_with_LazyFinger (self, tree, list):
        foundList = []
        while list != []:
            x = list.pop()
            self.lazyFinger_search(tree, x)   

if __name__ == '__main__':
    sys.setrecursionlimit(2000)
    
    
    #skl = SkipList()
    inputList1 = [1,2,3,4,5,6,7,8]
    searchlist = [1,1]
    print ("insert list in bst:", inputList1)
    print ("search list for Lazy finger:", searchlist)
       
    len_s = len(searchlist)
    len_i = len(inputList1) 
    
    bst = RedBlackTree()
    bst.insertMultipleElem(inputList1)
    
    
    lf = LazyFinger()
    lf.LazyFinger = lf.setfirst_LazyFinger(bst)
    print("\n setfirst_LazyFinger - lazyFinger was set to:", lf.lazyFinger.data)
    
    print ("so many LazyFinger.usedNodesInSearch in BST:", lf.usedNodesInSearch)
    print ("so many BST.usedNodesInSearch:", bst.usedNodesInSearch)
    print ("TOTAL Used Nodes in search:", bst.usedNodesInSearch + lf.usedNodesInSearch)
    
    # Aktion  
    lf.findMultipleElem_with_LazyFinger(bst, searchlist)
    
    print ("so many LazyFinger.usedNodesInSearch in BST:", lf.usedNodesInSearch)
    print ("so many BST.usedNodesInSearch:", bst.usedNodesInSearch)
    print ("TOTAL Used Nodes in search:", bst.usedNodesInSearch + lf.usedNodesInSearch)
   
    
    # compare without
    print("--- without lazy finger ---")

    print ("len_s", len_s)
    print("mathematical search would be", (math.log2(len_i))*(len_s))
    
    #bst.printTree()
    #bst.printTree()
    #skl.printSkipList()
    
    
    
    
    
    