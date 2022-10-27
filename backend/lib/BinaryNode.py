
class BinaryNode:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None
    def add_left(self, child):
        self.left_child = child
    def add_right(self, child):
        self.right_child = child
    def __str__(self):
        result = f'{self.value}:'
        if (self.left_child == None):
            result += ' None'
        else:
            result += f' {self.left_child.value}'
        if (self.right_child == None):
            result += ' None'
        else:
            result += f' {self.right_child.value}'
        return result


# Create two nodes named "root" and "a".
#root = BinaryNode('Root')
#a = BinaryNode('A')

# Make "a" be the left child of "root."
#root.add_left(a)