

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

if __name__ == '__main__':

    tree = Binary_Node(50)
    tree = insert_node(tree, 30)
    tree = insert_node(tree, 20)
    tree = insert_node(tree, 40)
    tree = insert_node(tree, 70)
    tree = insert_node(tree, 60)
    tree = insert_node(tree, 80)
    inorder_traversal(tree)
    print(search_node(tree, 40))