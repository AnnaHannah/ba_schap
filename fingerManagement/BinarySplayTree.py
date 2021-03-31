# Splay tree implementation in python
# Author: AlgorithmTutor
# Tutorial URL: http://algorithmtutor.com/Data-Structures/Tree/Splay-Trees/

# Finger Management system, für optimierte suchen

import sys
from pickle import FALSE

class Node:
    def  __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None
        

class BinarySplayTree:
    def __init__(self):
        self.root = None
        self.counterNodes = 0

    def recrusive_print(self, currPtr, indent, last):
        # print the tree structure on the screen
        if currPtr != None:
            sys.stdout.write(indent)
            if last == True:
                  sys.stdout.write("R----")
                  indent += "     "
            else:
                sys.stdout.write("L----")
                indent += "|    "

            print (currPtr.data)

            self.recrusive_print(currPtr.left, indent, False )
            self.recrusive_print(currPtr.right, indent, True)
    
    def binary_search(self, startNode, key):
        if startNode == None or key == startNode.data:
            return startNode

        if key < startNode.data:
            return self.binary_search(startNode.left, key)
        return self.binary_search(startNode.right, key)

    def deleteElem(self, startNode, key):
        x = None
        t = None 
        s = None
        while startNode != None:
            if startNode.data == key:
                x = startNode
            if startNode.data <= key:
                startNode = startNode.right
            else:
                startNode = startNode.left
        self.counterNodes -= 1
        if x == None:
            print ("Couldn't find key in the tree")
            return
        
        # split operation
        self.moveToTop(x)
        if x.right != None:
            t = x.right
            t.parent = None
        else:
            t = None

        s = x
        s.right = None
        x = None

        # join operation
        if s.left != None:
            s.left.parent = None

        self.root = self.joinToOneTree(s.left, t)
        s = None

    # rotate left at node x
    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != None:
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

    # rotate right at node x
    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != None:
            y.right.parent = x
        
        y.parent = x.parent;
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        
        y.right = x
        x.parent = y

    # Splaying operation. It moves x to the root of the tree
    def moveToTop(self, x):
        while x.parent != None:
            if x.parent.parent == None:
                if x == x.parent.left:
                    # zig rotation
                    self.right_rotate(x.parent)
                else:
                    # zag rotation
                    self.left_rotate(x.parent)
            elif x == x.parent.left and x.parent == x.parent.parent.left:
                # zig-zig rotation
                self.right_rotate(x.parent.parent)
                self.right_rotate(x.parent)
            elif x == x.parent.right and x.parent == x.parent.parent.right:
                # zag-zag rotation
                self.left_rotate(x.parent.parent)
                self.left_rotate(x.parent)
            elif x == x.parent.right and x.parent == x.parent.parent.left:
                # zig-zag rotation
                self.left_rotate(x.parent)
                self.right_rotate(x.parent)
            else:
                # zag-zig rotation
                self.right_rotate(x.parent)
                self.left_rotate(x.parent)

    # joins two trees s and t
    def joinToOneTree(self, s, t):
        if s == None:
            return t

        if t == None:
            return s

        x = self.maximumNode(s)
        self.moveToTop(x)
        x.right = t
        t.parent = x
        return x

    def __pre_order_helper(self, node):
        if node != None:
            sys.stdout.write(node.data + " ")
            self.__pre_order_helper(node.left)
            self.__pre_order_helper(node.right)

    def __in_order_helper(self, node):
        if node != None:
            self.__in_order_helper(node.left)
            sys.stdout.write(node.data + " ")
            self.__in_order_helper(node.right)

    def __post_order_helper(self, node):
        if node != None:
            self.__post_order_helper(node.left)
            self.__post_order_helper(node.right)
            std.out.write(node.data + " ")

    # Pre-Order traversal
    # Node->Left Subtree->Right Subtree
    def preorder(self):
        self.__pre_order_helper(self.root)

    # In-Order traversal
    # Left Subtree -> Node -> Right Subtree
    def inorder(self):
        self.__in_order_helper(self.root)

    # Post-Order traversal
    # Left Subtree -> Right Subtree -> Node
    def postorder(self):
        self.__post_order_helper(self.root)

    # search the tree for the key k
    # and return the corresponding node
    def searchTree(self, k):
        x = self.binary_search(self.root, k)
        if x != None:
            self.moveToTop(x)
    
    def findMultipleElem(self, list):       
        foundList = []
        while list != []:
            x = list.pop()
            self.searchTree(x)
            # if self.searchTree(x) != None:
                # foundList.append(self.searchTree(x))
        # return foundList 
            
    def minimumNode(self, node):
        while node.left != None:
            node = node.left
        return node

    def maximumNode(self, node):
        while node.right != None:
            node = node.right
        return node

    # find the successor of a given node
    def successor(self, x):
        # if the right subtree is not null,
        # the successor is the leftmost node in the
        # right subtree
        if x.right != None:
            return self.minimum(x.right)

        # else it is the lowest ancestor of x whose
        # left child is also an ancestor of x.
        y = x.parent
        while y != None and x == y.right:
            x = y
            y = y.parent
        return y

    # find the predecessor of a given node
    def predecessor(self, x):
        # if the left subtree is not null,
        # the predecessor is the rightmost node in the 
        # left subtree
        if x.left != None:
            return self.maximum(x.left)

        y = x.parent
        while y != None and x == y.left:
            x = y
            y = y.parent
        return y

    # insert the key to the tree in its appropriate position
    def insert(self, key):
        node =  Node(key)
        y = None
        x = self.root

        while x != None:
            y = x
            if node.data < x.data:
                x = x.left
            else:
                x = x.right
        self.counterNodes += 1       
             
        # y is parent of x
        node.parent = y
        if y == None:
            self.root = node
        elif node.data < y.data:
            y.left = node
        else:
            y.right = node
        # splay the node
        self.moveToTop(node)
        
    def insertMultipleElem(self, list):
        while list != []:
            x = list.pop()
            self.insert(x)
            

    def deleteNode(self, data):
        # delete the node from the tree
        self.deleteElem(self.root, data)

    def printSplaytree(self):
        self.recrusive_print(self.root, "", True)

if __name__ == '__main__':
    
    sys.setrecursionlimit(2000)
    
    
    list = [9,8,7,6,5,4,3,2,1]
    tree = BinarySplayTree()
    tree.insertMultipleElem(list)
    print("tree.counterNodes = ", tree.counterNodes)
    tree.printSplaytree()
    tree.findMultipleElem([9,7,9,7])
    tree.printSplaytree()
    print ("\n  tree.deleteNode(9) und 7 \n")
    tree.deleteNode(9)
    tree.deleteNode(7)
    tree.printSplaytree()
    
    