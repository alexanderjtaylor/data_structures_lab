import implementation
from linkedlist import LinkedList

if __name__ == '__main__':
    linked_list = LinkedList()
    
linked_list.append_node(22)
linked_list.append_node(33)
linked_list.append_node(44)
print(linked_list.find_node(33))