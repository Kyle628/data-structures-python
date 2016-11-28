class node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

    def set_data(self, data):
        self.data = data

class linked_list:
    def __init__(self, head=None):
        self.head = head

    def prepend(self, some_data):
        new_node = node(some_data)
        new_node.set_next(self.head)
        self.head = new_node

    def append(self, some_data):
        if self.head == None:
            self.head = node(some_data)
        elif self.head.get_next() == None:
            self.head.set_next(node(some_data))
        else:
            current = self.head
            while current.get_next() != None:
                current = current.get_next()
            current.set_next(node(some_data))

    def remove(self, value):
        current = self.head
        if current.get_data() == value:
            self.head.set_data(None)
        else:
            while current != None:
                if current.get_next().get_data() == value:
                    current.set_next(current.get_next().get_next())
                current = current.get_next()

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count

    def reverse(self):
        current = self.head
        # last node in linked list always points to None
        node_before = None
        while current:
            #keep track of node in front before we point to what is behind us
            next_node = current.next_node
            #point to what is behind because we are reversing
            current.next_node = node_before
            #remember this node so we can point what is next back to this node in the next iteration
            node_before = current
            #go to next node but cant use .next_node because we already moved what it is pointing to
            current = next_node
        self.head = node_before

    def print_list(self):
        head = self.head
        curr = head
        result = ''
        while curr.get_next() != None:
            result += str(curr.get_data()) + " "
            curr = curr.get_next()
        result += str(curr.get_data()) + " "
        print result
