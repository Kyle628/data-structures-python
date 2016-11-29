class hash_table:
    def __init(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size
    def hash_function(self, key, size):
        return key % size

    def rehash(self, oldhash, size):
        return (oldhash+1) % size

    def put(self, key, data):

        hash_value= self.hash_function(key, len(self.slots))

        #case of no collision
        if self.slots[hash_value] == None:
            self.slots[hash_value] = key
            self.data[hash_value] = data
        #collision
        else:
            #key already exists at this slot
            if self.slots[hash_value] == key:
                self.data[hash_value] = data
            #collision and key is not the same as existing key at this slot
            else:
                #find a new slot for this key
                next_slot = self.rehash(hash_value, len(self.slots))
                #keep looking for slots until we find one
                while self.slots[next_slot] != None and self.slots[next_slot] != key:
                    next_slot = self.rehash(next_slot, len(self.slots))

                #did we find an empty spot or were there previous collisions so we just found our key?
                if self.slots[nextslot] == None:
                    self.slots[nextslot]=key
                    self.data[nextslot]=data
                else:
                    self.data[nextslot] = data
