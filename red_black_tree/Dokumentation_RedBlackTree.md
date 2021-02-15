#Das ist eine zusammenfassung von Funktionen welche in dem Rot Schwarz Baum verwendet werden:

Allgemein der Rotschwarzebaum besteht aus Nodes welcher in einem Binärbaum Strucktur zusammengestellt werden.
Kleinere Werte der Nodes werden nach rechts und größere nach Links einsortiert.

Folgende Funktionen sind verfügbar:

### bst = RedBlackTree()
init von leerem RorSchwarzTree

### inputList = [1, 2, 3, 4, 5, 6]
Empfohlen den Input als Liste zudefinieren

### bst.insertMultipleElem(inputList)
So kann man mehere Elementen aus der Liste in den RS-Baum einfügen, Achtung: Beschränkung wurde auferlegt, dass nur Integer als Input zugelassen sind.

### deleteFullTree (bst) - 
löscht den gesammten Baum und löscht alle Nodes

### bst.preorder()
Gibt die eingetragenen Zahlen preoder gelesen heraus

### bst.inorder()
Gibt die eingetragenen Zahlen inorder gelesen heraus

### bst.postorder()
Gibt die eingetragenen Zahlen postorder gelesen heraus

### bst.searchTree(key)
sucht was node data bei dem Key abgelegt hat