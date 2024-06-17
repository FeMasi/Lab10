import networkx as nx

from database.DAO import DAO


class Model:

    def __init__(self):
        self._graph = nx.Graph()

    def buildGraph(self, year):
        self._countries = DAO.getAllCountries(year)
        self._idMap = {}

        for country in self._countries:
            self._idMap[country.CCode] = country

        self._graph.clear()
        borders = DAO.getCountryPairs(self._idMap, year)
        self._graph.add_nodes_from(self._countries)
        #for b in borders:
        #    self._graph.add_edge(b.c1, b.c2)
        self._graph.add_edges_from(borders)

    def getNumCompConnesse(self):
        return nx.number_connected_components(self._graph)

    def getNumConfinanti(self, v):
        return len(list(self._graph.neighbors(v)))

    def getNodes(self):
        return list(self._graph.nodes())

