

class Relationship:
    def __init__(self, node_left, node_right, attr_left, attr_right, attributes_affected):
        self.node_left = node_left
        self.node_right = node_right
        self.attribute_left = attr_left
        self.attribute_right = attr_right
        self.attributes_affected = attributes_affected
        self.to_delete = False
