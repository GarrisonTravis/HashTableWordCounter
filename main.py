from chaining import ChainingHashTable
from probing import ProbingHashTable

cht = ChainingHashTable(0, 50)
pht = ProbingHashTable(0, 54)

# Open the file
inFile = open('Dictionary.txt', 'r')

# Insert each line into the hash table
for line in inFile:
    cht.insert(line.rstrip())
    pht.insert(line.rstrip())

# Close the file
inFile.close()

# Print all the unique words in the file and the number of times they appear
print("CHT:")
cht.printAll()
print(cht.size)

print("\nPHT:")
pht.printAll()
print(pht.size)
