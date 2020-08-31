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
            result += str(node) + '->'.join(self._edges[node]) if len(self._edges[node]) > 0 else None + "\n"


def test_add_edge_without_node():
    di_graph = DiGraph()
    di_graph.add_edge(Edge(Node("a"), Node("b")))


def test_add_duplicated_node():
    di_graph = DiGraph()
    di_graph.add_node(Node("a"))
    di_graph.add_node(Node("a"))


if __name__ == "__main__":
    test_add_duplicated_node()
