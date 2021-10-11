# HashTableWordCounter

This repository contains the Python code for a word counter. It takes the words from a dictionary file and counts how many times each word appears in the file. It uses a hash table to store the words and their number of occurences. The hash table has three different implementations: Separate Chaining, Linear Probing, and Double Hashing.

# Separate Chaining

Separate Chaining is an Open Hashing technique used to resolve collisions in the hash table. It does this by creating a list at each index of the hash table, and if a collision happens, then it will store the key in this list. This way each index of the hash table can actually contain multiple keys.

# Linear Probing

Linear Probing is an Open Addressing or Closed Hashing technique used to resolve collisions in the hash table. It does this by adding one to the hash value each time a collision occurs until an empty index in the hash table is found. Once an empty index is found, it inserts the key.

# Double Hashing

Double Hashing is an Open Addressing or Closed Hashing technique used to resolve collisions in the hash table. It does this by applying a second hash function until it finds an empty index in the hash table. Once it finds an empty index, it inserts the key.
