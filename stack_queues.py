# stack is a kind of list but from which we can only add and remove element from one end and cannot access other elements without removing the top element (consider a cricket ball containing pipe )

class Node():
    def __init__(self,value):
        self.value = value
        self.next = None


class Stack():
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def push(self,value):
        new_node = Node(value)

        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1

    def pop(self):
        if self.height == 0:
            return None

        temp = self.top
        self.top = self.top.next
        temp.next = None

        self.height -= 1

        return temp

    def print_stack(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next

stack = Stack(4)
stack.push(3)
stack.push(2)
stack.push(1)
stack.pop()
# stack.print_stack()



# queues: something like stack but we can only dequeue and enqueue from  one end (consider it a line of people infront of counter)

class Queue():
    def __init__(self,value):
        new_node = Node(value)
        self.front = new_node
        self.rear = new_node
        self.length = 1


    def enqueue(self,value):
        new_node = Node(value)

        if self.length == 0:
            self.front = new_node
            self.rear = new_node
        else:   
            self.rear.next = new_node
            self.rear = new_node

        self.length += 1

    def dequeue(self):
        if self.length == 0:
            return None

        temp = self.front
        self.front = self.front.next
        temp.next = None

        self.length -= 1

        if self.length == 0:
            self.front = None
            self.rear = None

        return temp
    
    def print_queue(self):
        temp = self.front
        while temp is not None:
            print(temp.value)
            temp = temp.next



queue = Queue(1)

queue.print_queue()