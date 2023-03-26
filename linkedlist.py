
class Node:
    def __init__(self, data):
        self.next = None
        self.data = data
    
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
       
    def append_node(self, data):
        node = Node(data)
        
        if self.head is None:
            self.head = node
            self.tail = node
            return
        else:
            self.tail.next = node
            self.tail = self.tail.next
            
    def find_node(self, data):
        nodes = self.head
        while nodes is not None:
            if data == nodes.data:
                return True
            else:
                nodes = nodes.next
        else:
            return False
        