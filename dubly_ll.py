class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList():
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:    
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        self.length += 1

    def pop(self):
        if self.length == 0:
            return None

        temp = self.tail
        self.tail = self.tail.prev
        self.tail.next = None
        temp.prev = None

        self.length -= 1

        if self.length == 0:
            self.head = None
            self.tail = None

        return temp.value
    
    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        self.length += 1


    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        self.head.prev = None
        temp.next = None

        self.length -= 1

        if self.length == 0:
            self.head = None
            self.tail = None

        return temp
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        if index < self.length/2:  
            temp = self.head
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for i in range(self.length - 1, index,  -1): #reverse counting
                temp = temp.prev

        return temp
    
    def set_value(self, value, index):
        temp = self.get(index)
        
        if temp:
            temp.value = value
            return True
        
        return False
    
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False

        if index == 0:
            return self.prepend(value)

        if index == self.length:
            return self.append(value)
        
        before = self.get(index - 1)
        after = before.next

        new_node = Node(value)

        after.prev = new_node
        before.next = new_node

        new_node.next = after
        new_node.prev = before

        self.length += 1

        return True
    
    def remove(self,index):
        if index < 0 or index >= self.length:
            return False

        if index == 0:
            return self.pop_first()

        if index == self.length - 1:
            return self.pop()

        temp =self.get(index)

        temp.next.prev = temp.prev
        temp.prev.next = temp.next

        temp.next = None
        temp.prev = None

        self.length -= 1
        return temp

        

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

        

doubly_ll = DoublyLinkedList(2)
doubly_ll.append(3)
doubly_ll.append(4)
doubly_ll.append(5)
doubly_ll.append(6)
# doubly_ll.pop()
doubly_ll.prepend(1)
# doubly_ll.pop_first()
# print(doubly_ll.get(3))

doubly_ll.insert(2, 555)

doubly_ll.print_list()