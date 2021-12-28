from util.sql.Mysql_util import *
from model.Attribute import Attribute
from model.Node import Node
from model.Relationship import Relationship
from model.Graph import Graph


class ObtainDatabaseModel:
    def __init__(self):
        self.cursor = None
        self.cursor = obtain_tables()
        self.graph = None
        self.generate_model()

    def generate_model(self):
        cursor_tables = obtain_full_tables(self.cursor)
        tables = []
        for result in cursor_tables:
            tables.append(result[0])
        nodes = []
        for table in tables:
            cursor_table = execute_command(self.cursor, "SHOW COLUMNS FROM " + table + ";")
            attributes = []
            for column in cursor_table:
                attributes.append(Attribute(name=column[0], parent_node=table))
            nodes.append(Node(name=table, attributes=attributes))
        self.graph = Graph(nodes=nodes, joins=[])
