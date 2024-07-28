from node import Node
class BST:
    def __init__(self):
        self.root = None
        

    def insert_new_key(self, new_key):
        if self.root is None:
            self.root = Node(new_key)
            return
        temp_node = self.root
        while temp_node != None:
            
            if new_key == temp_node.key:
                print("We cannot insert duplicate key")
                break
            elif new_key < temp_node.key:
                # insert left or go left
                if temp_node.left is None:
                    # insert left and that's it
                    temp_node.left = Node(new_key)
                    break
                else:
                    # go left and find right place to insert
                    temp_node = temp_node.left
                    
            elif new_key > temp_node.key:
                # insert right or go right
                if temp_node.right is None:
                    # insert right and that's it
                    temp_node.right = Node(new_key)
                    break
                else:
                    # go right and find right place to insert
                    temp_node = temp_node.right
            

    def insertKey(self, new_key):
        self.insert_new_key(new_key)

    # Finds the minimum of the entire tree starting at the root
    def tree_minimum(self):
        if self.root is not None:
            return self.minimum(self.root)
        else:
            return None

    #  finds the minimum of a sub tree starting at temp_node
    # minimum of sub tree starting at a node is just the left most node in its.

    def minimum(self, temp_node):
        if temp_node is not None:
            current = temp_node
            while current.left is not None:
                current = current.left
            return current

    def delete(self, node, key):
        if node is None:
            return node
        if key < node.key:
            # the node to delete is to the left, go left
            node.left = self.delete(node.left, key)
        elif key > node.key:
            # the node to delete is to the right, go right
            node.right = self.delete(node.right, key)
        else:
            # deleting this node
            # - first case: deleting this node, that has no left child but has a right child. 
            #  in which case, the right child will replace this node
            if node.left is None and node.right is not None:
                return node.right
            elif node.right is None and node.left is not None:
            # - second case: deleting a node whose right child is None and left child is not None
                return node.left
            # this is the case where youre deleting a node that has two children.
            # the rule is to first find it's next largest key: smallest child in the right sub tree.
            # update this node's key with that childs key, then delete the child in the right sub tree
            temp = self.minimum(node.right)
            if temp is not None:
                node.key = temp.key
                node.right = self.delete(node.right, temp.key)
            else:
                return temp
        return node

    def deleteKey(self, key):
        self.root = self.delete(self.root, key)

    def search(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self.search(node.left, key)
        return self.search(node.right, key)

    def searchKey(self, key):
        return self.search(self.root, key)

    def inOrderDisplay(self, node):
        if node is not None:
            self.inOrderDisplay(node.left)
            print(node.key, end=' ')
            self.inOrderDisplay(node.right)

    def inOrderTraversal(self):
        self.inOrderDisplay(self.root)
        print()

    def preOrderDisplay(self, node):
        if node is not None:
            print(node.key, end=' ')
            self.preOrderDisplay(node.left)
            self.preOrderDisplay(node.right)

    def preOrderTraversal(self):
        self.preOrderDisplay(self.root)
        print()

    def postOrderDisplay(self, node):
        if node is not None:
            self.postOrderDisplay(node.left)
            self.postOrderDisplay(node.right)
            print(node.key, end=' ')

    def postOrderTraversal(self):
        self.postOrderDisplay(self.root)
        print()
