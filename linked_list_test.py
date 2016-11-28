from linked_list import node
from linked_list import linked_list

my_node = node(1, None)


my_linked_list = linked_list(my_node)

my_linked_list.append(2)
my_linked_list.append(3)

my_linked_list.append(4)

my_linked_list.remove(4)
my_linked_list.reverse()
my_linked_list.print_list()
