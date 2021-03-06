#! /usr/bin/env python3
import unittest
from unittest import TestCase

from commons.DiGraph import DiGraph
from commons.Edge import Edge
from commons.GraphAlgs import stringify_path, dfs, bfs
from commons.Node import Node


class TestGraphAlgs(TestCase):
    @unittest.skip
    def test_print_path(self):
        path = [Node("a"), Node("b"), Node("c"), Node("d")]
        printed = stringify_path(path)
        self.assertEqual(printed, 'a->b->c->d')

    def test_dfs(self):
        digraph = TestGraphAlgs.build_digraph()
        shortest_path_via_dfs = dfs(digraph, Node("0"), Node("5"), [], None, True)
        self.assertEqual("0->2->3->5", stringify_path(shortest_path_via_dfs))

    def test_bfs(self):
        digraph = TestGraphAlgs.build_digraph()
        shortest_path_via_bfs = bfs(digraph, Node("0"), Node("5"), False)
        self.assertEqual("0->2->3->5", stringify_path(shortest_path_via_bfs))

    @classmethod
    def build_digraph(cls):
        digraph = DiGraph()
        nodes = []

        for name in range(6):
            nodes.append(Node(str(name)))
        for node in nodes:
            digraph.add_node(node)

        digraph.add_edge(Edge(nodes[0], nodes[1]))
        digraph.add_edge(Edge(nodes[1], nodes[2]))
        digraph.add_edge(Edge(nodes[2], nodes[3]))
        digraph.add_edge(Edge(nodes[2], nodes[4]))
        digraph.add_edge(Edge(nodes[3], nodes[4]))
        digraph.add_edge(Edge(nodes[3], nodes[5]))
        digraph.add_edge(Edge(nodes[0], nodes[2]))
        digraph.add_edge(Edge(nodes[1], nodes[0]))
        digraph.add_edge(Edge(nodes[3], nodes[1]))
        digraph.add_edge(Edge(nodes[4], nodes[0]))

        return digraph
