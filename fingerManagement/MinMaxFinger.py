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
            print("MaxiFinger was set from " + str(type(tree)) + " to", newMaxFinger.data)
            return newMaxFinger
        if type(tree) == SkipList:
            newMaxFinger = tree.maximumInSkiplist()
            self.maxiFinger = newMaxFinger
            print("MaxiFinger was set from " + str(type(tree)) + " to", newMaxFinger.data)
            return newMaxFinger
    
    def setMiniFingerFrom(self, tree):  
        if type(tree)== RedBlackTree:        
            newMinFinger = tree.minimumInTree()
            self.miniFinger = newMinFinger
            print("MiniFinger was set from " + str(type(tree)) + " to", newMinFinger.data)
            return newMinFinger
        if type(tree)== SkipList: 
            newMinFinger = tree.minimumInSkiplist()
            self.miniFinger = newMinFinger
            print("MiniFinger was set from " + str(type(tree)) + " to", newMinFinger.data)
            return newMinFinger
    
    def fingerSearch(self, tree, keyInInt):
        searchResult = None
        if type(tree)== RedBlackTree:    
            if self.maxiFinger.data - keyInInt < keyInInt - self.miniFinger.data:
                searchResult = (tree.twoDirectSearch(self.maxiFinger, keyInInt)) 
                # print ("- fingerSearch used maxiFinger for:", searchResult)      
            if self.maxiFinger.data - keyInInt > keyInInt - self.miniFinger.data:
                searchResult = (tree.twoDirectSearch(self.miniFinger, keyInInt))
                # print ("- fingerSearch used miniFinger for:", searchResult)
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
            
            
        
if __name__ == "__main__":
    sys.setrecursionlimit(2000)
    bst = RedBlackTree()
    skl = SkipList()
    inputList1 = [1,2,3,4,2,2,2,5,6,7,999]
    bst.insertMultipleElem(inputList1)
    
    mmf=MinMaxFinger()
    mmf.maxiFinger = mmf.setMaxiFingerFrom(bst)
    mmf.miniFinger = mmf.setMiniFingerFrom(bst)
    mmf.maxiFinger = mmf.setMaxiFingerFrom(skl)
    mmf.miniFinger = mmf.setMiniFingerFrom(skl)
       
    mmf.fingerSearch(skl, 2)
    # bst.printTree()
    skl.printSkipList()
    
    