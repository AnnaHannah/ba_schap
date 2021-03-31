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
        self.maxiFinger = Finger(0)
        self.miniFinger = Finger(0)
    
    def getMaximumOf(self, tree):      
        newMaxFinger = Node(0)
        newMaxFinger = tree.maximumInTree()
        self.maxiFinger = newMaxFinger
        print("MaxiFinger in MinMaxFinger was set", newMaxFinger.data)
        return newMaxFinger
    
    def getMinimumOf(self, tree):      
        newMinFinger = Node(0)
        newMinFinger = tree.minimumInTree()
        self.miniFinger = newMinFinger
        print("MiniFinger in MinMaxFinger was set: ", newMinFinger.data)
        return newMinFinger
    
    def fingerSearch(self, tree, keyInInt):
        searchResult = None
        if self.maxiFinger.data - keyInInt < keyInInt - self.miniFinger.data:
            searchResult = (tree.twoDirectSearch(self.maxiFinger, keyInInt)) 
            # print ("- fingerSearch used maxiFinger for:", searchResult)
        
        if self.maxiFinger.data - keyInInt > keyInInt - self.miniFinger.data:
            searchResult = (tree.twoDirectSearch(self.miniFinger, keyInInt))
            # print ("- fingerSearch used miniFinger for:", searchResult)
        #print ("\nfingerSearch has found:", searchResult)
        return searchResult
                  
            
if __name__ == "__main__":
    sys.setrecursionlimit(2000)
    bst = RedBlackTree()
    inputList1 = [1,2,3,4]
    bst.insertMultipleElem(inputList1)
    
    mmf=MinMaxFinger()
    mmf.maxiFinger = mmf.getMaximumOf(bst)
    mmf.miniFinger = mmf.getMinimumOf(bst)
       
    mmf.fingerSearch(bst, 1)
    bst.printTree()
    
    