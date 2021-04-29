# this class is the MinMax Finger tree
# this version of finger trees accepts input datastructure, then sets ist minimal and maximal pointers(Fingers) and then starts 
# a search from the given Pointer, 

# Finktioniert nur für rot schwarz bäume

from red_black_tree.RedBlackTree import * 
from skiplist.SkipList import * 


class Finger():
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None
        self.color = None
        
class MinMaxFinger():
    def __init__ (self):
        self.maxiFinger = Finger(None)
        self.miniFinger = Finger(None)
    
    def setMaxiFingerFrom(self, tree):  
        if type(tree)== RedBlackTree:    
            newMaxFinger = tree.maximumInTree()
            self.maxiFinger = newMaxFinger
            #print("MaxiFinger was set from " + str(type(tree)) + " to", newMaxFinger.data)
            return newMaxFinger
        if type(tree) == SkipList:
            newMaxFinger = tree.maximumInSkiplist()
            self.maxiFinger = newMaxFinger
            #print("MaxiFinger was set from " + str(type(tree)) + " to", newMaxFinger.data)
            return newMaxFinger
    
    def setMiniFingerFrom(self, tree):  
        if type(tree)== RedBlackTree:        
            newMinFinger = tree.minimumInTree()
            self.miniFinger = newMinFinger
            #print("MiniFinger was set from " + str(type(tree)) + " to", newMinFinger.data)
            return newMinFinger
        if type(tree)== SkipList: 
            newMinFinger = tree.minimumInSkiplist()
            self.miniFinger = newMinFinger
            #print("MiniFinger was set from " + str(type(tree)) + " to", newMinFinger.data)
            return newMinFinger
    
    def fingerSearch(self, tree, keyInInt):
        searchResult = None
        if type(tree)== RedBlackTree:    
            if self.maxiFinger.data - keyInInt < keyInInt - self.miniFinger.data:
                searchResult = (tree.twoDirectSearch(self.maxiFinger, keyInInt)) 
                #print ("fingerSearch used maxiFinger for:", searchResult)      
            if self.maxiFinger.data - keyInInt > keyInInt - self.miniFinger.data:
                searchResult = (tree.twoDirectSearch(self.miniFinger, keyInInt))
                #print ("fingerSearch used miniFinger for:", searchResult)
                #print ("\nfingerSearch has found:", searchResult)
            return searchResult
        
        # #if type(tree)== SkipList: 
            # if self.maxiFinger.data - keyInInt < keyInInt - self.miniFinger.data:
                # searchResult = (tree.twoDirectSearch(self.maxiFinger, keyInInt)) 
                # # print ("- fingerSearch used maxiFinger for:", searchResult)      
            # if self.maxiFinger.data - keyInInt > keyInInt - self.miniFinger.data:
                # searchResult = (tree.twoDirectSearch(self.miniFinger, keyInInt))
                # #print ("- fingerSearch used miniFinger for:", searchResult)
                # #print ("\nfingerSearch has found:", searchResult)
            
    def findMultipleElem_with_MinMaxFinger (self, tree, list):
        foundList = []
        while list != []:
            x = list.pop()
            self.fingerSearch(tree, x)   
        
if __name__ == "__main__":
    sys.setrecursionlimit(2000)
    bst = RedBlackTree()
    #skl = SkipList()
    inputList1 = [1,2,3,4,2,2,2,5,6,7,0]
    searchlist = [1,2,3,4,2,2,2,5,6,7,0]

    bst.insertMultipleElem(inputList1)
    #skl.insertMultipleElem(inputList1)
    
    mmf = MinMaxFinger()
    mmf.maxiFinger = mmf.setMaxiFingerFrom(bst)
    mmf.miniFinger = mmf.setMiniFingerFrom(bst)
    #mmf.maxiFinger = mmf.setMaxiFingerFrom(skl)
    #mmf.miniFinger = mmf.setMiniFingerFrom(skl)
       
    #print("\nErgebniss von Fingersearch ist, fingersearch entscheidet selbst ob es von minimum oder Maximum sucht:", mmf.fingerSearch(bst, 3))
    #print("\nErgebniss von Fingersearch ist, fingersearch entscheidet selbst ob es von minimum oder Maximum sucht:", mmf.findMultipleElem_with_MinMaxFinger(bst, searchlist))

    #bst.printTree()
    #skl.printSkipList()
    
    