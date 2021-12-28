import rdflib as _rdf
import sqlalchemy as _sqla

db_str = "mysql://localhost:3306/test?user=root&password=root"
db = _sqla.create_engine(db_str)
graph = _rdf.Graph()
graph.open(db)

print(graph.serialize(format=''))