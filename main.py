from hashTable import HashTable
from chaining import ChainingHashTable

cht = ChainingHashTable(0, 5)

print(cht.size)
print(cht.capacity)

hVal = cht.hash('hi')
print(hVal)

print(cht.isEmpty())

print(ChainingHashTable.table)
cht.printTable()