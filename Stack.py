from LinkedList import LinkedList

# Title: Stacks
# Date: 3/9/20
# Author: Benjamin Lemery
# This program demonstrates how to create and manipulate a stack FIFO

class Stack:
    def __init__(self):
        self.list = LinkedList()

    def push (self,data):
        self.list.add_to_head(data)

    def pop(self):
        self.list.remove_from_head()
