class HashTable:

    def __init__(self, size, capacity):
        self.size = size
        self.capacity = capacity
    
    # Hash function 
    def hash(self, word):
        h = 0

        for ch in word:
            h = (13 * h + ord(ch)) % self.capacity
        
        return h

    def isEmpty(self):
        if self.size == 0:
            return True
        else:
            return False