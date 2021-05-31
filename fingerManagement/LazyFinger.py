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
            #print("setfirst_LazyFinger - lazy Finger was set to:", self.lazyFinger.data)
            return self.lazyFinger
    
    # update the finger after search
    def lazyFinger_search(self, tree, keyInInt):
        searchResult = None
        if type(tree)== RedBlackTree:    
            searchResult = (tree.twoDirectSearch_Node(self.lazyFinger, keyInInt)) 
            #print("search result:", (tree.twoDirectSearch_Node(self.lazyFinger, keyInInt)).data)
            
            if searchResult != self.lazyFinger:
                # only count if lazy finger was realy set new
                self.usedNodesInSearch += 1
                
            self.lazyFinger = searchResult
      
            #print("LazyFinger_search - lazyfinger was set to", self.lazyFinger.data)
        return searchResult
    
    def findMultipleElem_with_LazyFinger (self, tree, list):
        foundList = []
        while list != []:
            x = list.pop()
            self.lazyFinger_search(tree, x)   

if __name__ == '__main__':
    sys.setrecursionlimit(2000)
    
    bst = RedBlackTree()
    #skl = SkipList()
    inputList1 = [1,2,3,4,5,6,7,8]
    searchlist = [1,2,3,4,5,6,7,8]

    bst.insertMultipleElem(inputList1)
    
    # init
    lf = LazyFinger()
    lf.LazyFinger = lf.setfirst_LazyFinger(bst)
    # finger performance
    lf.findMultipleElem_with_LazyFinger(bst, searchlist)
    print ("so many LazyFinger.usedNodesInSearch:", lf.usedNodesInSearch)
    print ("so many BST.usedNodesInSearch:", bst.usedNodesInSearch)
    print ("so many BST+LAZYFinger usedNodesInSearch:", bst.usedNodesInSearch + lf.usedNodesInSearch)
    
    # finish finger 
    bst.deleteFullTree()
    
    # compare without
    print("--- without lazy finger ---")
    
    inputList1 = [1,2,3,4,5,6,7,8]
    searchlist = [1,1,1,1,1,1,1,1]
    
    bst.insertMultipleElem(inputList1)
    bst.findMultipleElem(searchlist)
    print ("so many BST.usedNodesInSearch:", bst.usedNodesInSearch)
    
    
    
    
    