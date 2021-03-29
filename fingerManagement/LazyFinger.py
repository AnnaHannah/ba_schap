

# meine Datenstruckturen
from red_black_tree.RedBlackTree import * 
from skiplist.SkipList import * 
import csv

def getLazyFinger(self):
    # read finger from outside, so last use get stored global
    return key
    
def setlazyFinger(filename, key):
    # write last used Node in csv file
    with open (filename, 'w', newline='') as file:
        writer = csv.writer(file, delimiter =',')
        writer.writerows(str(key))

if __name__ == '__main__':
    
    sys.setrecursionlimit(2000)
    # init
    layzyfinger = setlazyFinger('lazyFinger.csv', 0)