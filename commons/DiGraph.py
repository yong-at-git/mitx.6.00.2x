#! /usr/bin/env python3
from commons.Edge import Edge
from commons.Node import Node


class DiGraph(object):

    def __init__(self) -> None:
        self._nodes = []
        self._edges = {}
        super().__init__()

    def add_node(self, node):
        if node in self._nodes:
            raise ValueError("Node={} already exists".format(str(node)))
        self._nodes.append(node)
        self._edges[node] = []

    def add_edge(self, edge):
        if edge.get_src() not in self._nodes or edge.get_dst() not in self._nodes:
            raise ValueError("Src and dst has to be existing nodes for edge={}".format(str(edge)))
        self._edges[edge.get_src()].append(edge.get_dst())

    def get_children(self, src):
        return self._edges[src]

    def has_node(self, node):
        return node in self._nodes

    def __str__(self) -> str:
        result = ""
        for node in self._nodes:
            children = '.'.join(list(map(str, self._edges[node]))) if len(self._edges[node]) > 0 else ""
            result += str(node) + "->" + "[" + children + "]" + "\n"
        return result


if __name__ == "__main__":
    graph = DiGraph()

    for i in range(1, 7):
        graph.add_node(Node(str(i)))

    graph.add_edge(Edge(Node("1"), Node("2")))
    graph.add_edge(Edge(Node("1"), Node("3")))
    graph.add_edge(Edge(Node("2"), Node("4")))
    graph.add_edge(Edge(Node("2"), Node("5")))
    graph.add_edge(Edge(Node("3"), Node("6")))
    graph.add_edge(Edge(Node("4"), Node("3")))

    print(str(graph))
