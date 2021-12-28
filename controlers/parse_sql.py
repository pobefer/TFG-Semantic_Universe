def get_tables(query):
    tables = {}
    raw_tables = query.split("from")[-1].split("where")[0].split(",")
    for table in raw_tables:
        table = table.strip()
        alias = table.split(" ")[-1]
        name = table.split(" ")[0]
        tables[alias] = name
    return tables


def get_attributes(query):
    attributes = {}
    raw_attributes = query.split("from")[0].split("select")[-1].split(",")
    for attribute in raw_attributes:
        attribute = attribute.strip()
        alias = attribute.split(".")[0]
        name = attribute.split(".")[-1]
        if alias in attributes.keys():
            attributes[alias].append(name)
        else:
            attributes[alias] = []
            attributes[alias].append(name)
    return attributes


def get_joins(query):
    joins = {}
    counter = 0
    raw_joins = query.split("where")[-1].split("and")
    #attributes = get_attributes(query=query)
    #joins["affected"] = attributes
    for join in raw_joins:
        join = join.strip()
        left = join.split("=")[0].strip()
        right = join.split("=")[-1].strip()
        # TODO: tenia una idea aqui, tendre que volver mas tarde
        # alias_left = left.split(".")[0]
        # name_left = left.split(".")[-1]
        # alias_right = right.split(".")[0]
        # name_right = right.split(".")[-1]
        if left in joins.keys():
            joins[left].append(right)
        else:
            joins[left] = []
            joins[left].append(right)
        counter += 1
    return joins


class Parser:
    def __init__(self, queries):
        self.queries = queries
        self.map = self.parse_sql()

    def parse_sql(self):
        counter = 0
        queries_map = {}
        for query in self.queries:
            tables = get_tables(query)
            attrs = get_attributes(query)
            joins = get_joins(query)
            counter += 1
            queries_map[str(counter)] = {
                "table": tables,
                "attrs": attrs,
                "joins": joins
            }
        return queries_map


