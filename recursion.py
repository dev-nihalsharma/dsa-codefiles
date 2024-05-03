def factorial(n):
    if n == 0 or n == 1:
        return 1
    
    return n * factorial(n - 1)


# print(factorial(5))
    
# ---------- Recursion In BST ----------

class Node():
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree():
    def __init__(self):
        self.root = None

    def __r_contains(self,current_node, value):
        if current_node is None:
            return False
        if current_node.value == value:
            return True
        
        if  value < current_node.value:
            return self.__r_contains(current_node.left, value)
        if value > current_node.value:
            return self.__r_contains(current_node.right, value)


    def r_contains(self,value):
        return self.__r_contains(self.root, value)

    def __r_insert(self,current_node, value):
        if current_node is None:
            return Node(value)
        
        if value < current_node.value:
            current_node.left = self.__r_insert(current_node.left, value)

        if value > current_node.value:
            current_node.right =  self.__r_insert(current_node.right, value)
        
        return current_node
    

    def r_insert(self,value):
        if self.root is None:
            self.root = Node(value)
            

        return self.__r_insert(self.root, value)
    

    
    def __r_delete(self,current_node,value):
        if current_node is None:
            return None
        
        elif value < current_node.left:
            current_node.left = self.__r_delete(current_node.left, value)
        elif value > current_node.right:
            current_node.right = self.__r_delete(current_node.right, value)
        else:
            if current_node.left is None and current_node.right is None:
                return None
            elif current_node.left == None:
                current_node = current_node.right
            elif current_node.right == None:
                current_node = current_node.left

            else:
                #finding minimum value node
                temp = current_node.right
                while temp.left is not None:
                    temp = temp.left

                # assigning minimum value node to current node
                current_node.value = temp.value
                
                # delete that min value node
                current_node.right = self.__r_delete(current_node.right, temp.value)

        return current_node

    def r_delete(self,value):
        return self.__r_delete(self.root, value)
    
        

bst = BinarySearchTree()
bst.insert(2)
bst.insert(1)
bst.insert(3)


print(bst.root.value)
print(bst.root.left.value)
print(bst.root.right.value)

print(bst.contains(3))
print(bst.contains(5))


