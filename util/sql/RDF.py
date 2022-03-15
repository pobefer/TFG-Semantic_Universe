import rdflib
from rdflib.graph import ConjunctiveGraph as Graph
from rdflib import plugin
from rdflib.store import Store
from rdflib.store import NO_STORE
from rdflib.store import VALID_STORE
from rdflib import Literal
from rdflib import Namespace
from rdflib import URIRef

default_graph_uri = "http://pobe.net/test"
configString = "host=localhost,user=root,password=root,db=test"

# Get the mysql plugin. You may have to install the python mysql libraries
store = plugin.get('MySQL', Store)('test')

# Open previously created store, or create it if it doesn't exist yet
rt = store.open(configString,create=False)
if rt == NO_STORE:
    # There is no underlying MySQL infrastructure, create it
    store.open(configString,create=True)
else:
    assert rt == VALID_STORE,"There underlying store is corrupted"

# There is a store, use it
graph = Graph(store, identifier = URIRef(default_graph_uri))

print("Triples in graph before add: %s" % len(graph))


print("Triples in graph after add: %" % len(graph))

# display the graph in RDF/XML
print(graph.serialize())