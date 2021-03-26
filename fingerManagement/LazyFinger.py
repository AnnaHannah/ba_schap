

# meine Datenstruckturen
from red_black_tree.RedBlackTree import * 
from skiplist.SkipList import * 
import csv

    # def getFinger(self):
    # read finger from outside, so last use get stored global
    #    return key
    
def setFinger(filename, key):
    # write last used Node in csv file
    with open (filename, 'w', newline='') as file:
        writer = csv.writer(file, delimiter =',')
        writer.writerows(str(key))

if __name__ == '__main__':
    
    sys.setrecursionlimit(2000)
    # init
    layzyfinger = setFinger('lazyFinger.csv', 0)