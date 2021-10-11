from chaining import ChainingHashTable
from probing import ProbingHashTable
from double import DoubleHashTable

# Open the file
val = input("Do you have your own file? (y/n): ")
if val == 'y' or val == 'Y' or val == 'yes' or val == 'Yes' or val == 'YES':
    fileName = input("Enter file name (include path if not in this directory): ")

    inFile = open(fileName, 'r')
else :
    inFile = open('Dictionary.txt', 'r')

# Print Selection Menu
print("\n1. Separate Chaining")
print("2. Linear Probing")
print("3. Double Hashing")
choice = input("Please select a hashing method from above: ")

# Make instance of the hash table
if choice == '3':
    ht = DoubleHashTable(0, 10000)
elif choice == '2':
    ht = ProbingHashTable(0, 10000)
else:
    ht = ChainingHashTable(0, 10000)

# Insert each line into the hash table
for line in inFile:
    ht.insert(line.rstrip())

# Close the file
inFile.close()

# Print all the unique words in the file and the number of times they appear
print("\nThere are " + str(ht.size) + " unique words in the file:")
ht.printAll()
