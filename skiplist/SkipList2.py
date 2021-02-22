# irgendwas ist schief gelaufen bei der original skiplist
from platform import node
from pip._vendor.requests.api import head
#from builtins import None

# das ist ein neuer versuch alle Methoden zu programierren

class SkipNode():
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
        self.top = None
        self.node_height = 0
    
class SkipList():
    def __init__(self):
        self.head = SkipNode(None)
        self.skipList_len = 0
        self.skip_height = 0 
    
    def len(self):
        return self.len
    
    def deleteFullSkiplist(self):  
        # full srtucture Nodes in SL
        self.head = SkipNode()
        self.len = 0
        self.skl_height = 0 
        # all Nodes in SL
        self.data = data
        self.prev = None
        self.next = None
        self.top = None
        self.node_height = 0
        
    def insertElem(self, elem):
        
        if self.skipList_len == 0:
            #head Management
            dummy = SkipNode(elem)
            self.head.prev = None
            self.head.next = dummy
            #Dummy Management
            dummy.prev = self.head
            dummy.next = None
            self.skipList_len += 1
            print ("first 2 elements in lsit:" + str( self.head.data) + ", " + str(self.head.next.data))

        # Pointer Management überlegen!
        
        if self.skipList_len > 0:
            dummy = SkipNode(elem)
            dummy.next = None
            dummy.prev = self.head
            dummy.data = elem
            
            self.head.next = dummy
            
            print("done:", dummy.data)
    
    def lastNodeOnLevel(self):
        node = self.head
        while node.next != None:
            node.next = node.next.next
        return node.data
    
    def printLevel (self, nrLevel):
        tempNode= SkipNode(None)
        tempNode = self.head
        print ("printLevel ", tempNode.data)
        
        while tempNode.next != None:
            print ("printLevel - multiElement: ", node.data)
            tempNode.next = tempNode.next.next
        return print("ready")
    
    
    
    
if __name__ == "__main__":
    skl = SkipList()
    input = 1
    skl.insertElem(1)
    skl.insertElem(2)
    skl.insertElem(3)
    print(skl.lastNodeOnLevel())
    # skl.printLevel(0)
            
    