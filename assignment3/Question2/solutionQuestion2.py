# Name: Misbah Ahmed Nauman
# ccid: misbahah
# studentId: 1830574
# operating system: Windows
# python version: 3.11.9

# Starter Code from https://www.geeksforgeeks.org/python-linked-list/
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Method to add a node at begin of LL
    def insertAtBegin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node

    # Method to add a node at any index
    # Indexing starts from 0.
    def insertAtIndex(self, data, index):
        if (index == 0):
            self.insertAtBegin(data)
            
        position = 0
        current_node = self.head
        while (current_node != None and position+1 != index):
            position = position+1
            current_node = current_node.next

        if current_node != None:
            new_node = Node(data)
            new_node.next = current_node.next
            current_node.next = new_node
        else:
            print("Index not present")

    # Method to add a node at the end of LL
    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        while(current_node.next):
            current_node = current_node.next

        current_node.next = new_node

    # Update node of a linked list at a given position
    def updateNode(self, val, index):
        current_node = self.head
        position = 0
        if position == index:
            current_node.data = val
        else:
            while(current_node != None and position != index):
                position = position+1
                current_node = current_node.next

            if current_node != None:
                current_node.data = val
            else:
                print("Index not present")

    # Print the size of linked list
    def sizeOfLL(self):
        size = 0
        if(self.head):
            current_node = self.head
            while(current_node):
                size = size+1
                current_node = current_node.next
            return size
        else:
            return 0

    # Print method for the linked list
    def printLL(self):
        current_node = self.head
        while(current_node):
            print(current_node.data, end=" ")
            current_node = current_node.next
        print()



    """I initially intended to use this in remove_duplicates() but didnt have to. might as well keep it since its functional."""
    # Removes the node from given position (index) and adjusts the pointer
    def removeNode(self, index):
        if self.head:
            current_node = self.head
            position = 0
            previousious_node = None

            if index == 0:
                self.head = current_node.next
                return  # To avoid unnecessary traversing
            else:
                while (current_node != None and position != index):
                    position += 1
                    previousious_node = current_node
                    current_node = current_node.next

                if current_node != None:
                    previousious_node.next = current_node.next
                else:
                    print("Index not present")
        else:
            print("List is empty")



    # Removes all duplicate nodes from the linked list
    def remove_duplicates(self):
        if not self.head:
            print("List is empty")
            return

        first_occurrences = set()  # stores data of each node that occurs for the first time
        previousious_node = None
        current_node = self.head

        while current_node != None:
            if current_node.data in first_occurrences:
                # Skip the current node by adjusting pointers
                previousious_node.next = current_node.next
            else:
                first_occurrences.add(current_node.data)
                previousious_node = current_node
            current_node = current_node.next



    # Merges all nodes from llist2 into the linked list object, maintains sorted order
    def merge(self, llist2):
        # Initialize pointers to the start of both linked lists
        current1 = self.head
        current2 = llist2.head

        # Handle edge cases where one or both lists are empty
        if current1 == None:
            self.head = current2
            return
        if current2 == None:
            return

        # Ensure self.head points to the smaller starting node
        if current2.data < current1.data:
            self.head = current2
            current2 = current2.next
            self.head.next = current1
            current1 = self.head

        # Pointer to maintain the current position in the merged list
        previous = current1
        current1 = current1.next

        # Merge nodes from both lists until one is exhausted
        while current1 and current2:
            if current2.data < current1.data:
                previous.next = current2
                current2 = current2.next
                previous = previous.next
                previous.next = current1
            else:
                previous = current1
                current1 = current1.next

        # If any nodes remain in llist2, attach them to the end of llist1
        if current2:
            previous.next = current2



def main():
    llist_nodes = input().split()
    if llist_nodes[0] == 'duplicate':
        llist = LinkedList()
        for i in range(1, len(llist_nodes)):
            llist.insertAtEnd(int(llist_nodes[i]))
        llist.remove_duplicates()
        llist.printLL()  
    else:
        llist1 = LinkedList()
        llist2 = LinkedList()
        llist2_index = llist_nodes.index("llist2")
        for i in range (1, llist2_index):
            llist1.insertAtEnd(int(llist_nodes[i]))
        for i in range(llist2_index + 1, len(llist_nodes)):
            llist2.insertAtEnd(int(llist_nodes[i]))
        llist1.merge(llist2)
        llist1.printLL()

if __name__ == "__main__":
    main()