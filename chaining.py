from hashTable import HashTable

class ChainingHashTable(HashTable):
    def __init__(self, size, capacity):
        super().__init__(size, capacity)
        
    table = [[{'hello', 1}, {'dude', 1}], [{'bro', 1}, {'copium', 1}]]
    
    def printTable(self):
        table1 = [list([dict()]) for num in range(self.capacity)]
        print(table1)
        