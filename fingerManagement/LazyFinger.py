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
        
    # set the first finger to the root (why not)      
    def setfirst_LazyFinger(self, tree):
        if type(tree)== RedBlackTree:    
            newLazyFinger = tree.getRoot()
            self.lazyFinger = newLazyFinger
            print("setfirst_LazyFinger - lazy Finger was set to:", self.lazyFinger.data)
            return self.lazyFinger
    
    # update the finger after search
    def lazyFinger_search(self, tree, keyInInt):
        searchResult = None
        if type(tree)== RedBlackTree:    
            searchResult = (tree.twoDirectSearch_Node(self.lazyFinger, keyInInt)) 
            print("search result:", (tree.twoDirectSearch_Node(self.lazyFinger, keyInInt)).data)
            self.lazyFinger = searchResult
            print("LazyFinger_search - lazyfinger was set to", self.lazyFinger.data)
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
    inputList1 = [1,2,3,4,2,2,2,5,6,7,0]
    searchlist = [1,2,3,4,2,2,2,5,6,7,0]

    bst.insertMultipleElem(inputList1)
    bst.printTree()
    # init
    lf = LazyFinger()
    lf.LazyFinger = lf.setfirst_LazyFinger(bst)
    lf.findMultipleElem_with_LazyFinger(bst, searchlist)
    
    