# Das ist eine Zusammenfassung von Funktionen welche in dem Rot Schwarz Baum verwendet werden:  

Allgemein der RotSchwarzBaum besteht aus Nodes welcher in einer Binärbaum Strucktur zusammengestellt werden.
Kleinere Werte der Nodes werden nach rechts und größere nach Links einsortiert.

Folgende Funktionen sind verfügbar:

### bst = RedBlackTree()
init/Initiation von leerem rot-Schwarz Baum

### inputList = [1, 2, 3, 4, 5, 6]
Empfohlen den Input als Liste zudefinieren, besonders für die folgende funktion: insertMultipleElem

### bst.insertMultipleElem(inputList)
So kann man mehere Elementen aus der Liste in den RS-Baum einfügen, Achtung: Beschränkung wurde auferlegt, dass nur Integer als Input zugelassen sind. Farbe wird automatisch nach korrigiert.

### deleteFullTree (bst) - 
löscht den gesammten Baum und löscht alle Nodes

### bst.searchTree(key)
Sucht was für node data bei dem Key abgelegt wurde

### bst.deleteNode(1)
Löscht den Node mit dem Wert 1 aus BST

### bst.printTree()
Nutzt vorallem die print Funktion um in der Konsole einen Baum zuprinten.




--- weniger wichtige Funktionen ---




### bst.nodesInTree()
Gibt die Anzahl der Nodes zurück, welche aktuell im Baum enthalten sind.

### bst.preorder()
Gibt die eingetragenen Zahlen preoder gelesen heraus

### bst.inorder()
Gibt die eingetragenen Zahlen inorder gelesen heraus

### bst.postorder()
Gibt die eingetragenen Zahlen postorder gelesen heraus

### bst.getRoot()
Gibt die aktuelle Wurzel des Baumes zurück

### bst.leftRotate(x)
Linksrotation um die Node x im BST

### bst.rightRotate(x)
Rechtsrotation um die Node x im BST

### bst.insert(1)
die 1 als Integer wird in den BST reingetan

### bst.fixColor()
Rot schwarz Baum wird Rotschwarz, doppelt kontrolliert


--- Beispielcode für main ---

if __name__ == "__main__":
    sys.setrecursionlimit(2000)
    print("1. Recursion allowed in this program:", sys.getrecursionlimit())
    inputList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
    bst = RedBlackTree()
    print("2. Number of Nodes now is: ", bst.counterNodes)
    print("3. Input in den Tree:", inputList)
    bst.insertMultipleElem(inputList)
    print("4. Number of Nodes now is: ", bst.counterNodes)
    print ("5. Number of black and red color fixes: " + str(mBcounter) + " and " + str(mRcounter))        
    bst.printTree()
  

