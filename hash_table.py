class HashTable:
    def __init__(self, size=7):
        self.data_map = [None] * size

    def __hash(self, keys):
        hash = 0
        for letter in keys:
            """
            creates a hash value for specific letter then,
            we keep adding on to it to create address of key
            Note: two different keys can have same hash value (address) 
            """
            hash = (hash + ord(letter) * 23) % len(self.data_map) # always produce number between 0 to map-size

        return hash
    
    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": " , val)

    def set_item(self, key, value):
        # getting the address
        index = self.__hash(key)

        if self.data_map[index] == None:
            self.data_map[index] = []

        self.data_map[index].append([key, value])

    def get(self, key):
        index = self.__hash(key)

        if self.data_map[index] == None:
            return None

        for array in self.data_map[index]:
            if array[0] == key:
                return array[1]
        pass

    def keys(self):

        keys = []
        for i in self.data_map:
            if i!= None:
                for j in i:
                    keys.append(j[0])
            
        return keys        
        

hash_table = HashTable()

hash_table.set_item('name', 'nihal')
hash_table.set_item('age', 17)
hash_table.set_item('profession', 'Programmer')
hash_table.print_table()

print(hash_table.get('name'))
print(hash_table.keys())



# ---------- Interview Question --------------
# check if any item in two lists is common 


def check_is_item_common(list1, list2):
    """
    By this method we can check is item common in two lists with a BigO of 2n,
    but if we do it standard way(loop through one list and another nested in it) BigO will be n^2
    """
    hash_dict = {}
    for i in range(len(list1)):
        hash_dict[list1[i]] = True
    
    for i in range(len(list2)):
        if list2[i] in hash_dict:
            return True


print(check_is_item_common([1,2,4,5,6], [1,2,3,4,5]))

