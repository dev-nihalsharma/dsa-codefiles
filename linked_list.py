# ----------- LINKED LIST ---------------


class Node():
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList():
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
            self.tail = new_node
        self.length += 1
    def pop(self):
        if self.length == 0:
            return None

        temp = self.head
        pre=self.head
        while temp.next is not None:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1

        if self.length == 0:
            self.head = None
            self.tail = None
        return temp.value # returning value which got popped

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        
        else:
            new_node.next = self.head
            self.head = new_node
        
        self.length += 1

    def pop_first(self):
        if self.length == 0:
            return None
        
        temp  = self.head
        self.head = temp.next
        temp.next = None

        self.length -= 1

        if self.length == 0:
            self.tail = None

        return temp.value

    def get(self, index):
        if index < 0 or index >= self.length:
            return None

        temp = self.head
        for _ in range( index):
            temp = temp.next

        return temp.value
    
    def set_value(self, value ,index):
        temp = self.get(index)
        
        if temp:
            temp.value = value
            return True
        
        return False
        
    def insert(self, value, index):
        if index < 0 or index > self.length:
            return False

        if index == 0:
            self.prepend(value)
        if index == self.length:
            self.append(value)
        else:
            temp = self.get(index-1)
            new_node = Node(value)
            new_node.next = temp.next
            temp.next = new_node

        self.length += 1

    def reverse(self): # IMPORTANT
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None

        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after

        


def print_ll(ll):
    current_node = ll.head
    while current_node is not None:
        print(current_node.value)
        current_node = current_node.next


my_linked_list = LinkedList(4)

# -- Appending --
my_linked_list.append(5)
my_linked_list.append(6)
my_linked_list.append(7)
print('Appending')
print_ll(my_linked_list)

print('Pop')
# -- Pop --
print(my_linked_list.pop())


# -- Prepending --
my_linked_list.prepend(3)
print('Prepending')
print_ll(my_linked_list)


# -- Pop First --
my_linked_list.pop_first()
print('Pop First')
print_ll(my_linked_list)

# -- Reverse --
my_linked_list.reverse()
print('Reverse')
print_ll(my_linked_list)