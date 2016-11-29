from binary_search_tree import tree_node
from binary_search_tree import binary_search_tree

my_node = tree_node('k', 'kyle')

'''my_node.right = tree_node('m', 'matias')

my_node.left = tree_node('g', 'giorgi')'''

my_tree = binary_search_tree()
my_tree.put("k", "kyle")
my_tree.put('g', 'giorgi')

my_tree.put('m', 'matias')

print my_tree.root.left.value
