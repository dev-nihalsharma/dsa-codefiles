class Node():
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree():
    def __init__(self):
        self.root = None

    
    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
        
        temp = self.root
        while temp is not None:
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                else:
                    temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                else:
                    temp = temp.right
    
    def contains(self, value):
        if self.root is None:
            return False
        
        temp = self.root
        while temp is not None:
            if value == temp.value:
                return True
            if value < temp.value:
                temp = temp.left
            else:
                temp = temp.right
        return False
    
    def BreathFirstSearch(self):
        """
        returns all the elements of Tree, from the top
        """
        current_node = self.root
        queues = []
        results = []

        queues.append(current_node)
        while len(queues) > 0:
            current_node = queues.pop(0)
            results.append(current_node.value)
            if current_node.left is not None:
                queues.append(current_node.left)
            if current_node.right is not None:
                queues.append(current_node.right)

        return results
    
    def DFSPreOrder(self):
        """
        Depth First Search - PreOder method
        """
        results = []
        def traverse(current_node):
            results.append(current_node.value)
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse (current_node.right)

        traverse(self.root)            
        return results

        

bst = BinarySearchTree()
bst.insert(2)
bst.insert(1)
bst.insert(3)


print(bst.root.value)
print(bst.root.left.value)
print(bst.root.right.value)

print(bst.contains(3))
print(bst.contains(5))

print(bst.BreathFirstSearch())
print(bst.DFSPreOrder())

