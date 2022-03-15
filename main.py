import sys
import time
import timeit
from controlers.parse_sql import Parser
import json
from controlers.generateGraph import ObtainDatabaseModel
import os
from controlers.parse_map import ParserMap
import util.sql.Mysql_util as ms
from controlers.generateUniverse import GenUniverse


def main(deep, database, verbose):
    check = True
    if not os.path.isfile('/home/pobe/PycharmProjects/SemanticUniverse/data/map_queries.json') or check:
        fd = open('/home/pobe/PycharmProjects/SemanticUniverse/data/queries_final.txt', 'r')
        sql_file = fd.read()
        fd.close()
        sql_commands = sql_file.split(';')

        t1 = time.time()
        queries = Parser(sql_commands)
        t2 = time.time()
        print("%s, Time=%s" % ("Parse sql", t2 - t1))
        print("Queries parse: " + str(get_size(queries)))
        map_queries = queries.map
        with open('/home/pobe/PycharmProjects/SemanticUniverse/data/map_queries.json', 'w', encoding='utf-8') as f:
            json.dump(map_queries, f, ensure_ascii=False, indent=4)

    data_model = ObtainDatabaseModel()
    fd = open('/home/pobe/PycharmProjects/SemanticUniverse/data/map_queries.json', 'r')
    map_queries = json.load(fd)

    t1 = time.time()
    result = ParserMap(map_queries=map_queries, graph=data_model, filtro=True, max_queries=1000000)
    t2 = time.time()
    print("%s, Time=%s" % ("Generate Nodes and Joins", t2 - t1))
    # print("Initial cost: " + str(get_size(result)))

    t1 = time.time()
    result.graph.calculate_hamiltonian_path()
    t2 = time.time()
    print("%s, Time=%s" % ("Calculate relationship ranks", t2 - t1))

    # print("Complete Graph: " + str(get_size(result)))

    with open('/home/pobe/PycharmProjects/SemanticUniverse/data/rank_iteration1.json', 'w', encoding='utf-8') as f:
        json.dump(result.graph.rank_in_nodes, f, ensure_ascii=False, indent=4)
    json_nodes = result.graph.generate_dict()
    with open('/home/pobe/PycharmProjects/SemanticUniverse/data/db_iteration1.json', 'w', encoding='utf-8') as f:
        json.dump(json_nodes, f, ensure_ascii=False, indent=4)

    result.calculate_best_choice()
    result.graph.rank_in_nodes = {}
    result.graph.calculate_hamiltonian_path()

    # print("Complete Graph: " + str(get_size(result)))

    with open('/home/pobe/PycharmProjects/SemanticUniverse/data/rank_iteration2.json', 'w', encoding='utf-8') as f:
        json.dump(result.graph.rank_in_nodes, f, ensure_ascii=False, indent=4)
    json_nodes = result.graph.generate_dict()
    with open('/home/pobe/PycharmProjects/SemanticUniverse/data/db_iteration2.json', 'w', encoding='utf-8') as f:
        json.dump(json_nodes, f, ensure_ascii=False, indent=4)

    result.calculate_best_choice()
    result.graph.rank_in_nodes = {}
    result.graph.calculate_hamiltonian_path()

    # vaya movida tocah tocha
    # print("Complete Graph: " + str(get_size(result)))

    with open('/home/pobe/PycharmProjects/SemanticUniverse/data/rank_iteration3.json', 'w', encoding='utf-8') as f:
        json.dump(result.graph.rank_in_nodes, f, ensure_ascii=False, indent=4)
    
    json_nodes = result.graph.generate_dict()
    with open('/home/pobe/PycharmProjects/SemanticUniverse/data/db_iteration3.json', 'w', encoding='utf-8') as f:
        json.dump(json_nodes, f, ensure_ascii=False, indent=4)

    result.calculate_best_choice()
    result.graph.rank_in_nodes = {}
    result.graph.calculate_hamiltonian_path()

    # vaya movida tocah tocha
    # print("Complete Graph: " + str(get_size(result)))

    with open('/home/pobe/PycharmProjects/SemanticUniverse/data/rank_iteration4.json', 'w', encoding='utf-8') as f:
        json.dump(result.graph.rank_in_nodes, f, ensure_ascii=False, indent=4)

    json_nodes = result.graph.generate_dict()
    with open('/home/pobe/PycharmProjects/SemanticUniverse/data/db_iteration4.json', 'w', encoding='utf-8') as f:
        json.dump(json_nodes, f, ensure_ascii=False, indent=4)
    
    result.calculate_best_choice()
    result.graph.rank_in_nodes = {}
    result.graph.calculate_hamiltonian_path()

    # vaya movida tocah tocha
    # print("Complete Graph: " + str(get_size(result)))

    with open('/home/pobe/PycharmProjects/SemanticUniverse/data/rank_iteration5.json', 'w', encoding='utf-8') as f:
        json.dump(result.graph.rank_in_nodes, f, ensure_ascii=False, indent=4)

    json_nodes = result.graph.generate_dict()
    with open('/home/pobe/PycharmProjects/SemanticUniverse/data/db_iteration5.json', 'w', encoding='utf-8') as f:
        json.dump(json_nodes, f, ensure_ascii=False, indent=4)
        
    result.calculate_best_choice()
    result.graph.rank_in_nodes = {}
    result.graph.calculate_hamiltonian_path()

    # vaya movida tocah tocha
    # print("Complete Graph: " + str(get_size(result)))

    with open('/home/pobe/PycharmProjects/SemanticUniverse/data/rank_iteration6.json', 'w', encoding='utf-8') as f:
        json.dump(result.graph.rank_in_nodes, f, ensure_ascii=False, indent=4)

    json_nodes = result.graph.generate_dict()
    with open('/home/pobe/PycharmProjects/SemanticUniverse/data/db_iteration6.json', 'w', encoding='utf-8') as f:
        json.dump(json_nodes, f, ensure_ascii=False, indent=4)

    print("Job Done!!!")



def get_size(obj, seen=None):
    """
    Recursively finds size of objects
    """
    size = sys.getsizeof(obj)
    if seen is None:
        seen = set()
    obj_id = id(obj)
    if obj_id in seen:
        return 0
    seen.add(obj_id)
    if isinstance(obj, dict):
        size += sum([get_size(v, seen) for v in obj.values()])
        size += sum([get_size(k, seen) for k in obj.keys()])
    elif hasattr(obj, '__dict__'):
        size += get_size(obj.__dict__, seen)
    elif hasattr(obj, '__iter__') and not isinstance(obj, (str, bytes, bytearray)):
        size += sum([get_size(i, seen) for i in obj])
    return size

def test(filename, id):
    GenUniverse(10,filename, "data/Iteration_"+id+"/db_"+id)
    

if __name__ == '__main__':
    main(None, None, None)
    # test('data/rank_iteration1.json', "1")
    # test('data/rank_iteration2.json', "2")
    # test('data/rank_iteration3.json', "3")
    
    
    # test('data/rank_iteration4.json', "4")
    # test('data/rank_iteration5.json', "5")
