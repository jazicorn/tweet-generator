#!python

class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None
        # self.size???

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class LinkedList(object):

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        # Create an empty list of results
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None
        # 0(1) time to return because it's only checking 1 variable

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        TODO: Running time: O(n) Why and under what conditions?"""

        # stretch challenge
        # return self.size

        # Loop through all nodes and count one for each
        node = self.head
        count = 0

        while (node):
            count += 1
            node = node.next

        return count

    def append(self, item):
        """Insert the given item at the tail of this linked list.
        TODO: Running time: O(1) Why and under what conditions?"""
        # Create new node to hold given item
        node = Node(item)
        # Append node after tail, if it exists

        if self.is_empty():
            self.head = node
            self.tail = node

        else:
            # Otherwise insert new node after tail
            self.tail.next = node
        # Update tail to ew node regardless
        self.tail = node



    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        TODO: Running time: O(1) Why and under what conditions?"""
        # Create new node to hold given item
        node = Node(item)
        # Prepend node before head, if it exists
        if self.is_empty():
            # Assign tail to a new node
            self.tail = node

        else:
            # Make next of new Node as head
            node.next = self.head
        # Move the head to point to new Node
        self.head = node


    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        TODO: Best case running time: O(1) Why and under what conditions?
        TODO: Worst case running time: O(n) Why and under what conditions?"""
        # Loop through all nodes to find item where quality(item) is True
        # Check if node's data satisfies given quality function

        node = self.head # Constant time to assign a variable reference

        while node is not None: # Up
            if quality(node.data) is True:
                return node.data
            
            else:
                node = node.next

        return None



    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?"""
        # Loop through all nodes to find one whose data matches given item
        # Update previous node to skip around node with matching data

        current  = self.head
        prev = None
        found = False
        while current:
            if self.head.data == item:
                # if there is an item after head
                if self.head.next is not None:
                    self.head = self.head.next
                    found = True
                    break
                else:
                    self.head = None
                    self.tail = None
                    found = True
                    break
    
            elif current.data == item:
                # checking the node that the data belongs to
                if current == self.tail:
                    prev.next = None
                    self.tail = prev 
                    found = True
                    break
                else:
                    prev.next = current.next
                    found = True
                    break

            else:
                prev = current
                current = current.next


        if not found:
            raise ValueError('Item not found: {}'.format(item))

def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))

    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()
