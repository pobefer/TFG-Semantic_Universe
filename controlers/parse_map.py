

class ParserMap:
    def __init__(self, map_queries, graph, filtro, max_queries):
        self.map = map_queries
        self.graph = graph.graph
        self.filtro = filtro
        self.max_queries = max_queries
        self.map_entities()

    def map_entities(self):
        counter = 0
        for query in self.map.keys():
            counter += 1
            if self.filtro:
                if counter == self.max_queries:
                    return
            for table in self.map[query]["table"].keys():
                if table == "":
                    continue
                alias = table
                name = self.map[query]["table"][table]
                if alias in self.map[query]["attrs"].keys():
                    for attr in self.map[query]["attrs"][alias]:
                        self.graph.put_node(name=name, attr=attr)
                        
            for relationship in self.map[query]["joins"].keys():
                attributes_affected = []
                for table in self.map[query]["table"].keys():
                    if table == "":
                        continue
                    alias = table
                    name = self.map[query]["table"][table]
                    if alias in self.map[query]["attrs"].keys():
                        for attr in self.map[query]["attrs"][alias]:
                            attributes_affected.append(name+"@"+attr)
                if relationship == "":
                    continue
                if relationship == "affected":
                    continue
                tabla_1 = self.map[query]["table"][relationship.split(".")[0]]
                for obj in self.map[query]["joins"][relationship]:
                    if obj.split(".")[0] in self.map[query]["table"].keys():
                        tabla_2 = self.map[query]["table"][obj.split(".")[0]]
                        self.graph.put_relationship(left=tabla_1, right=tabla_2,
                                                    attr_left=relationship.split(".")[-1],
                                                    attr_right=obj.split(".")[-1],
                                                    affected=attributes_affected)

    def map_relationships(self):
        # TODO: I had an idea here, will come back
        pass

    def calculate_best_choice(self):
        choice = self.graph.get_current_choice()
        rel_choice = choice[1]
        attr_choice = choice[0]
        
        self.graph.merge_current_best_choice(rel_choice=rel_choice, attr_choice=attr_choice)