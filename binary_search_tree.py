class tree_node:
    def __init__(self, key, value,
     left=None, right=None, parent=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

    def has_left_child(self):
        return self.left

    def has_right_child(self):
        return self.right

    def is_left_child(self):
        return self.parent and self.parent.left == self

    def is_right_child(self):
        return self.parent and self.parent.right == self

    def is_root(self):
        return not self.parent

    def is_leaf(self):
        return not (self.right or self.left)

    def has_any_children(self):
        return self.right or self.left

    def has_both_children(self):
        return self.right and self.left

class binary_search_tree:

    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

#pick up here tomorrow
    def put(self, key, value):
        if self.root:
            self._put(key, value, self.root)
        else:
            self.root = tree_node(key, value)

    def _put(self, key, value, current_node):
        if key < current_node.key:
            if current_node.has_left_child():
                self._put(key,value,current_node.left)
            else:
                current_node.left = tree_node(key,value,parent=current_node)
        else:
            if current_node.has_right_child():
                self._put(key,value,current_node.right)
            else:
                current_node.right = tree_node(key,value,parent=current_node)

    '''def add(self, key, value, current=self.root):
        if self.root == None:
            self.root = tree_node(key, value)
            print "was empty so made something", self.root
        elif key < current.key:
            if current.has_left_child:
                add(key, value, current.left)
            else:
                current.left = tree_node(key, value, parent=current)
                print "added to the left"
        else:
            if current.has_right_child:
                add(key, value, current.right)
            else:
                current.right = tree_node(key, value, parent=current)
                print "added to the right"'''


    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()
