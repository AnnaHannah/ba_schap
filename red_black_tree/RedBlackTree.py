import sys
from _overlapped import NULL
from idlelib.idle_test.test_editor import insert
# Implementing Red-Black Tree in Python
# Importing the threading module
from time import sleep
from tkinter.tix import INTEGER
from idlelib.idle_test.test_configdialog import root

# global Variable
mRcounter = 0
mBcounter = 0


# Node creation
class Node():

    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None
        self.color = None


class RedBlackTree():

    def __init__(self):
        self.TNULL = Node(0)
        self.TNULL.color = 1
        self.TNULL.left = None
        self.TNULL.right = None
        self.root = self.TNULL
        self.counterNodes = 0
    
    def deleteFullTree (self):
        # all Nodes in tree
        self.TNULL = Node(0)
        self.TNULL.color = 0
        self.TNULL.left = None
        self.TNULL.right = None
        self.root = self.TNULL
        self.counterNodes = 0
        # tree Parameters
        self.data = None
        self.parent = None
        self.left = None
        self.right = None
        self.color = 1
        
    # Preorder
    def preOrderHelper(self, node):
        if node != self.TNULL:
            sys.stdout.write(str(node.data) + " ")
            self.preOrderHelper(node.left)
            self.preOrderHelper(node.right)

    # Inorder
    def inOrderHelper(self, node):
        if node != self.TNULL:
            self.inOrderHelper(node.left)
            sys.stdout.write(str(node.data) + " ")
            self.inOrderHelper(node.right)

    # Postorder
    def postOrderHelper(self, node):
        if node != self.TNULL:
            self.postOrderHelper(node.left)
            self.postOrderHelper(node.right)
            sys.stdout.write(str(node.data) + " ")

    # Search the tree
    def searchTreeHelper(self, node, key):
        if key == node.data:
            #print ("Gesucht nach %r und im Tree gefunden." % node.data)
            return node.data
        if node == self.TNULL:
            return None
        if key < node.data:
            return self.searchTreeHelper(node.left, key)
        return self.searchTreeHelper(node.right, key)

    # Balancing the tree after deletion
    def fixDelete(self, x):
        while x != self.root and x.color == 0:
            if x == x.parent.left:
                s = x.parent.right
                if s.color == 1:
                    s.color = 0
                    x.parent.color = 1
                    self.leftRotate(x.parent)
                    s = x.parent.right

                if s.left.color == 0 and s.right.color == 0:
                    s.color = 1
                    x = x.parent
                else:
                    if s.right.color == 0:
                        s.left.color = 0
                        s.color = 1
                        self.rightRotate(s)
                        s = x.parent.right

                    s.color = x.parent.color
                    x.parent.color = 0
                    s.right.color = 0
                    self.leftRotate(x.parent)
                    x = self.root
            else:
                s = x.parent.left
                if s.color == 1:
                    s.color = 0
                    x.parent.color = 1
                    self.rightRotate(x.parent)
                    s = x.parent.left

                if s.right.color == 0 and s.right.color == 0:
                    s.color = 1
                    x = x.parent
                else:
                    if s.left.color == 0:
                        s.right.color = 0
                        s.color = 1
                        self.leftRotate(s)
                        s = x.parent.left

                    s.color = x.parent.color
                    x.parent.color = 0
                    s.left.color = 0
                    self.rightRotate(x.parent)
                    x = self.root
        x.color = 0

    def __rbTransplant(self, u, v):
        if u.parent == None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    # Node deletion
    def deleteNodeHelper(self, node, key):
        self.counterNodes = (self.counterNodes) - 1
        if self.counterNodes < 0:
            self.counterNodes = 0
        if node == self.root:
            z = self.TNULL
            # node = self.TNULL
            return 
        
        while node != self.TNULL:
            if node.data == key:
                z = node
            if node.data <= key:
                node = node.right
            else:
                node = node.left
        if z == self.TNULL:
            print("Cannot find " + str(key) + " in the tree")
            return None
        y = z
        y_original_color = y.color
        if z.left == self.TNULL:
            x = z.right
            self.__rbTransplant(z, z.right)
        elif (z.right == self.TNULL):
            x = z.left
            self.__rbTransplant(z, z.left)
        else:
            y = self.minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self.__rbTransplant(y, y.right)
                y.right = z.right
                y.right.parent = y

            self.__rbTransplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if y_original_color == 0:
            self.fixDelete(x)
    
    # Balance the tree after insertion

    def fixInsert(self, k):
        while k.parent.color == 1:
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left
                if u.color == 1:
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self.rightRotate(k)
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.leftRotate(k.parent.parent)
            else:
                u = k.parent.parent.right

                if u.color == 1:
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self.leftRotate(k)
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.rightRotate(k.parent.parent)
            if k == self.root:
                break
        self.root.color = 0

    # Printing the tree
    def printHelper(self, node, indent, last):
        if node != self.TNULL:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("L----")
                indent += "|    "
            else:
                sys.stdout.write("R----")
                indent += "    "

            if node.color == 1:
                s_color = "RED" 
            else: 
                s_color = "BLACK"
            print(str(node.data) + "(" + s_color + ")")
            self.printHelper(node.left, indent, False)
            self.printHelper(node.right, indent, True)

    # Fix colors in Red Black tree
    def fixColorHelper(self, node): 
        
        def makeRed(node): 
            global mRcounter 
            mRcounter = mRcounter + 1
            # Abfangen von AttributeError: 'NoneType' object has no attribute 'color'
            # None.color exestiert nicht
            if node == None:
                return ''
            if node.color == 1:
                if node.left != None:
                    node.left.color = 0
                    makeBlack(node.left)
                if node.right != None:
                    node.right.color = 0
                    makeBlack(node.right)    
      
        def makeBlack(node):
            global mBcounter
            mBcounter = mBcounter + 1
            # Abfangen von AttributeError: 'NoneType' object has no attribute 'color'
            # None.color exestiert nicht
            if node == None:
                return ''     
            if node.color == 0:
                if node.left != None:
                    node.left.color = 1
                    makeRed(node.left)
                if node.right != None:
                    node.right.color = 1
                    makeRed(node.right)

        if node == None:
            return ''  
        
        makeBlack(node)  # falls Wurzel unbekannte Farbe hat
        makeRed(node)      
              
    def preorder(self):
        self.preOrderHelper(self.root)

    def inorder(self):
        self.inOrderHelper(self.root)

    def postorder(self):
        self.postOrderHelper(self.root)

    def searchTree(self, k):
        return self.searchTreeHelper(self.root, k)

    def leftRotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.TNULL:
            y.left.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def rightRotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.TNULL:
            y.right.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def insert(self, key):
        assert type(key) is int, " \n %r is not an integer, in this Tree is only interger accepted. \n Please modify your Input. \n Insertionprozess stopped now" % key
        if self.contains (key) == False:
            node = Node(key)
            node.parent = None
            node.data = key
            node.left = self.TNULL
            node.right = self.TNULL
            node.color = 1
            self.counterNodes = (self.counterNodes) + 1 
    
            y = None
            x = self.root
    
            while x != self.TNULL:
                y = x
                if node.data < x.data:
                    x = x.left
                else:
                    x = x.right
    
            node.parent = y
            if y == None:
                self.root = node
            elif node.data < y.data:
                y.left = node
            else:
                y.right = node
    
            if node.parent == None:
                node.color = 0
                return
            if node.parent.parent == None:
                return
            self.fixInsert(node)
        else: 
            return
        
    def fixColor(self):
        self.fixColorHelper(self.root)
        
    def insertMultipleElem (self, list):
        while list != []:
            x = list.pop()
            self.insert(x)
        self.fixColor()

    def getRoot(self):
        return self.root

    def deleteNode(self, data):
        self.deleteNodeHelper(self.root, data)

    def printTree(self):
        self.printHelper(self.root, "", True)

    def nodesInTree(self):
        return self.counterNodes
    
    def contains(self, key):
        return (self.searchTree(key) == key)

if __name__ == "__main__":
    sys.setrecursionlimit(2000)
    # print("1. Recursion allowed in this program:", sys.getrecursionlimit())
    # inputList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
    inputList1 = [1,2,3,4,5,6,7,1,2,1,1,1,1,1,1,1]
    bst = RedBlackTree()
    
    # print("2. Number of Nodes now is: ", bst.counterNodes)
    # print("3. Input in den Tree:", inputList)
    bst.insertMultipleElem(inputList1)
    # print ("das wird gesucht: bst.searchTree(5)", bst.searchTree(5))
    # print ("das wird gesucht: bst.contains(5)", bst.contains(5))
    # print("4. Number of Nodes now is: ", bst.counterNodes)
    # print ("5. Number of black and red color fixes: " + str(mBcounter) + " and " + str(mRcounter))        
    bst.printTree()

    
