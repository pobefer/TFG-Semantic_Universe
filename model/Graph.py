from model.Relationship import Relationship
from util.string import string_util as str_util
import copy


class Graph:
    def __init__(self, nodes, joins):
        self.nodes = nodes
        self.joins = joins
        self.hamiltonian_rank = 0
        self.rank_in_nodes = {}

    def calculate_hamiltonian_path(self):
        """
            Calculate value of ham path of the graph
        :return:  hamiltonian rank
        """
        for relationship in self.joins:
            node_left = self.search_node(relationship.node_left.name)
            node_right = self.search_node(relationship.node_right.name)
            attr_left = relationship.attribute_left
            attr_right = relationship.attribute_right
            node_left.rank += 1
            node_right.rank += 1
            if node_left.name + "@" + node_right.name not in self.rank_in_nodes.keys():
                self.rank_in_nodes[node_left.name + "@" + node_right.name] = \
                    {
                        attr_left + "@" + attr_right: 0
                    }
            if attr_left + "@" + attr_right not in self.rank_in_nodes[node_left.name + "@" + node_right.name].keys():
                self.rank_in_nodes[node_left.name + "@" + node_right.name][attr_left + "@" + attr_right] = 0
            self.rank_in_nodes[node_left.name + "@" + node_right.name][attr_left + "@" + attr_right] += 1
        self.hamiltonian_rank = 0
        return self.hamiltonian_rank

    def put_node(self, attr, name):
        table = list(filter(lambda x: x.name == name, self.nodes))[0]
        attribute = list(filter(lambda x: x.name == attr, table.attrs))[0]
        attribute.rank += 1

    def put_relationship(self, left, right, attr_left, attr_right, affected):
        node_left = list(filter(lambda x: x.name == left, self.nodes))[0]
        node_right = list(filter(lambda x: x.name == right, self.nodes))[0]
        self.joins.append(Relationship(node_left=node_left, node_right=node_right,
                                       attr_left=attr_left, attr_right=attr_right,
                                       attributes_affected=affected))

    def search_node(self, node):
        table = list(filter(lambda x: x.name == node, self.nodes))[0]
        return table

    def get_current_choice(self):
        current_choice = None
        current_best = 0
        current_rel = None
        for rel in self.rank_in_nodes.keys():
            for attr in self.rank_in_nodes[rel].keys():
                if self.rank_in_nodes[rel][attr] > current_best:
                    current_best = self.rank_in_nodes[rel][attr]
                    current_choice = attr
                    current_rel = rel
        return current_choice, current_rel

    def merge_current_best_choice(self, rel_choice, attr_choice):
        node_left = self.find_node(str_util.get_left_split(rel_choice))
        node_right = self.find_node(str_util.get_right_split(rel_choice))
        attr_left = str_util.get_left_split(attr_choice)
        attr_right = str_util.get_right_split(attr_choice)

        if not node_left or not node_right:
            return "No way"

        self.remove_node(node_right, node_left, attr_choice)
        attrs_append = list(filter(lambda x: x.name != attr_left and x.name != attr_right, node_right.attrs))
        for a in attrs_append:
            a.name = node_right.name + "_" + a.name
        node_left.attrs.extend(attrs_append)

    def find_node(self, node_string):
        node = filter(lambda x: x.name == node_string, self.nodes)
        return next(node) if node else None

    def remove_node(self, node_right, node_left, attr_choice):
        rels = copy.deepcopy(self.joins)
        for rel in rels:
            if (node_left.name == rel.node_left.name and node_right.name == rel.node_right.name) or (
                    node_right.name == rel.node_left.name and node_left.name == rel.node_right.name):
                rel.to_delete = True
            if node_right.name == rel.node_left.name and node_right.name != rel.node_right.name:
                rel.node_left = node_left
            if node_right.name == rel.node_right.name and node_left.name != rel.node_left.name:
                rel.node_right = node_left
        self.joins = list(filter(lambda x: x.to_delete is False, rels))

        self.nodes.remove(node_right)

    def generate_dict(self):
        dic = {}
        for node in self.nodes:
            node_dic = {}
            for attr in node.attrs:
                node_dic[attr.name] = attr.parent_node+"@"+attr.name
            dic[node.name] = node_dic
        return dic
    