from hashTable import HashTable

# Linear Probing used to resolve collisions
# Upon encountering a collision in the hash table, Linear Probing will continue adding 1 until
# it finds an empty index in the hash table. Once it finds an empty index, it inserts the (key, value)

class ProbingHashTable(HashTable):

    def __init__(self, size, capacity):
        super().__init__(size, capacity)

        # Set up table as a list of dictionaries
        self.table = list(dict() for num in range(self.capacity))

    # Function to insert the word into the hash table
    def insert(self, key):
        
        # Get the index from the hash function
        index = self.hash(key)
        i = 0

        while i < self.capacity:
            # Linear probing
            newIndex = (index + i) % self.capacity

            # If the dictionary at newIndex is empty add in the word
            if not bool(self.table[newIndex]):
                self.table[newIndex][key] = 1
                self.size += 1
                return
            # If the key exists in the table at the index add 1 to the value
            elif key in self.table[newIndex]:
                self.table[newIndex][key] += 1
                return
            # Else add one to i
            else:
                i += 1

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

        