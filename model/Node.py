

class Node:
    def __init__(self,name, attributes):
        self.name = name
        self.attrs = attributes
        self.rank = 0

    def calculate_rank(self):
        """
            calculate rank of the node
        :return:
        """
        self.rank = 0
        return self.rank
