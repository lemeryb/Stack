class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_head(self,data):
        self.data = data
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.tail = self.head

    def add_to_end(self,data):
        new_node = Node(data)
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node


    def remove_from_head(self):
        new_node = self.head
        self.head = self.head.next
        return(new_node.data)

    def remove_end(self):
        current_node = self.head
        previous_node = self.head
        while current_node.next:
            previous_node = current_node
            current_node = current_node.next
        previous_node.next = None
        return(current_node.data)

    def search_node(self,data):
        current_node = self.head
        while current_node:
            if current_node.data == data:
                return True
            current_node = current_node.next

    def remove_node(self,data):
        previous_node = None

        current_node = self.head
        while current_node:
            if current_node.data == data:
                if previous_node:
                    previous_node = current_node.next
                else:
                    self.head = current_node.next
                return True

    def clear(self):
        self.head = None
        self.tail = None