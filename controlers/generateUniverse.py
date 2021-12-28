from util.sql.Mysql_util import *
import json

class GenUniverse:
    def __init__(self, deep, map, output):
        self.deep = deep
        self.cursor = obtain_tables()
        self.universe = []
        self.map = self.load_json(map, output)
        #self.parse_map(self.map)
        
        
    def load_json(self, map_path, mp_output):
        with open(map_path) as f:
            map = json.load(f)
        for entry in map.keys():
            t_rel = entry
            a_rel = map[entry]
            t_left = t_rel.split('@')[0]
            t_rigth = t_rel.split('@')[-1]
            for i in a_rel.keys():
                a_left = i.split('@')[0]
                a_rigth = i.split('@')[-1]
            query = "select * from " + t_left + " a , " + t_rigth + " b where "
            query += "a." + a_left + "=b." + a_rigth
            write_to_file(self.cursor, query, "" + mp_output + t_left + "@" + t_rigth + ".csv")
           
                
            
            
        
    # def generate_query(self):
    #     pass
    
    # def load_data(self, query):
    #     pass
    
    # def parse_map(self, map):
    #     self.mappings = self.load_mapping(map)
    #     self.universe.append(self.load_data(self.generate_query()))
        