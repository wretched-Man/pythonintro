"""
Building a singly-linked list in python
"""
from dataclasses import dataclass

@dataclass
class Node():
    """
    A single node. Helper class for SinglyLinkedList.
    """

    def __init__(self, val):
        self.val = val
        self.next = None
        


class SingleLinkedList:
    """
    Python implementation of a SinglyLinkedList
    """

    def __init__(self, head = None):
        #count = number of nodes
        self.count = 0
        self._head = None

        if head is None:
            pass            
        elif isinstance(head, Node):
            self._head = head
            self.count = 1
        else:
            raise TypeError(f"Wrong input. Expected an object of type {type(Node)}. {type(head)}"
                            " given instead.")

    
    def insert(self, new_node):
        """
        Insert Node at end of the list.
        """

        if type(new_node) is not Node:
            raise TypeError(f"The insert method expects a Node object."
                            f" Received {type(new_node)} instead!")

        #if there's none, make node the head
        if self._head is None:
            self._head = new_node
        else:
            #Iterate until the last element
            temp = self._head.next

            if temp is None:
                self._head.next = new_node
            else:
                while temp is not None:
                    prev , temp = temp, temp.next
                #since temp is none, the last node has been
                #reached
                prev.next = new_node
        self.count += 1
    
    def delete(self, pos = None):
        #If pos is an integer, delete according to pos
        #else, delete according to value

        #do nothing
        if pos is None:
            return
        #delete according to pos
        elif isinstance(pos, int):
            if self.count - 1 < pos or pos < 0:
                raise IndexError(f"The linked list is of size {self.count}, "
                                 f"but pos {pos} requested!")

            prev, temp = Node(None), self._head

            if pos == 0:
                #delete first element
                self._head = self._head.next
            else:
                while pos > 0:
                    prev, temp = temp, temp.next
                    pos-=1
                prev.next = temp.next
            del temp
        #delete according to value
        #elif isinstance():
        self.count -=1


    def printlist(self):
        temp = self._head
        print('[ ', end = '')
        while temp is not None:
            print(temp.val, end=', ')
            temp = temp.next
        print(']')

#Building a linked list
list1 = SingleLinkedList(Node(10))

#Inserting multiple elements
ll = [2, 5, 6, 7]

for elem in ll:
    list1.insert(Node(elem))

#Printing the list
list1.printlist()

#Removing element `x` from the list
list1.delete(2)

#Printing the new list
list1.printlist()
