from hashTable import HashTable

# Double Hashing used to resolve collisions
# Upon encountering a collision in the hash table, Double Hashing will apply a second hash function until
# it finds an empty index in the hash table. Once it finds an empty index, it inserts the (key, value)

class DoubleHashTable(HashTable):

    def __init__(self, size, capacity):
        super().__init__(size, capacity)

        # Set up table as a list of dictionaries
        self.table = list(dict() for num in range(self.capacity))

        self.HASH2 = 11

    # Function for double hashing when collision occurs
    def secondHash(self, word):
        h = 0

        for ch in word:
            h = self.HASH2 - ((100 * h + ord(ch)) % self.HASH2)\
        
        return h

    # Function to insert the word into the hash table
    def insert(self, key):
        
        # Get the index from the hash function
        index = self.hash(key)

        # Get the index from the second hash function
        index2 = self.secondHash(key)

        i = 0

        while i < self.capacity:

            # i starts at 0, so for the first iteration newIndex will be equal to index
            newIndex = (index + i * index2) % self.capacity

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

        