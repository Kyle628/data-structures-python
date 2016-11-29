class tree_node:
    def __init__(self, key=None, value, left=None, right=None, parent=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

class binary_search_tree:
    def __init__(self):
        self.root = None

    def put(self, key, value):
        if self.root:
            _put(key, value, self.root)
        else:
            self.root = tree_node(key, value)

    def _put(self, key, value, current):
        if key < current.key:
            #left
            if current.left:
                _put(self, key, value, current.left)
            else:
                current.left = tree_node(key, value)
        else:
            if current.right:
                _put(self, key, value, current.right)
            else:
                current.right = tree_node(key, value)
