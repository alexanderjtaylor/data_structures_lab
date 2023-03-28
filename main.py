import implementation
from linkedlist import LinkedList
from binary_node import Binary_Node
from binary_node import insert_node
from binary_node import inorder_traversal
from binary_node import search_node

if __name__ == '__main__':
    # linked_list = LinkedList()

    
# linked_list.append_node(22)
# linked_list.append_node(33)
# linked_list.append_node(44)
# print(linked_list.find_node(33))


    tree = Binary_Node(50)
    tree = insert_node(tree, 30)
    tree = insert_node(tree, 20)
    tree = insert_node(tree, 40)
    tree = insert_node(tree, 70)
    tree = insert_node(tree, 60)
    tree = insert_node(tree, 80)

    inorder_traversal(tree)
    print(search_node(tree, 40))