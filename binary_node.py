

class Binary_Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.val = data

def insert_node(self, data):
    if self is None:
        return Binary_Node(data)
    else:
        if self.val == data:
            return self
        elif self.val < data:
            self.right = insert_node(self.right, data)
        else:
            self.left = insert_node(self.left, data)
    return self

def search_node(self, data):
    if self is None or self.val == data:
        return '{} has been found'.format(self.val)
    elif self.val < data:
        return search_node(self.right, data)
    else:
        return search_node(self.left, data)
 

def inorder_traversal(self):
    if self:
        inorder_traversal(self.left)
        print(self.val, end =" ")
        inorder_traversal(self.right)
        
def preorder_traversal(self):
    if self:
        print(self.val),
        preorder_traversal(self.left)
        preorder_traversal(self.right)
        
def postorder_traversal(self):
    if self:
        postorder_traversal(self.left)
        postorder_traversal(self.right)
        print(self.val),