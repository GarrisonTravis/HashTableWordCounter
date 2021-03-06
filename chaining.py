from hashTable import HashTable

# Separate Chaining used to resolve collisions
# Upon encountering a collision, Separate Chaining will add in the (key, value)
# into the index where the collision happened, but it will be the next element in the list at
# that index. So every index in the hash table can store multiple elements.

class ChainingHashTable(HashTable):

    def __init__(self, size, capacity):
        super().__init__(size, capacity)

        # Set up table as a list of dictionaries
        self.table = list(dict() for num in range(self.capacity))

    # Function to insert the word into the hash table
    def insert(self, key):
        
        # Get the index from the hash function
        index = self.hash(key)

        # If the key exists in the table at the index add 1 to the value
        if key in self.table[index]:
            self.table[index][key] += 1
        # Else add in the key at the index
        else:
            self.table[index][key] = 1
            self.size += 1

    # Function to get the number of times a word appears in the file
    def getNumTimes(self, key):

        index = self.hash(key)

        if key in self.table[index]:
            return self.table[index][key]
        else:
            print('Word not found!')

    # Function to print out the unique words and the amount of times they appear
    def printAll(self):
        for dict in self.table:
            for key, value in dict.items():
                print(key + ' = ' + str(value))

    def printTable(self):
        print(self.table)

        