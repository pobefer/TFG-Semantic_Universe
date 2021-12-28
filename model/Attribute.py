

class Attribute:
    def __init__(self, name, parent_node):
        self.parent_node = parent_node
        self.name = name
        self.rank = 0

    def increment_rank(self):
        self.rank += 1
