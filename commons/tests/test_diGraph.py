#! /usr/bin/env python3
from unittest import TestCase
from commons.DiGraph import DiGraph
from commons.Edge import Edge
from commons.Node import Node


class TestDiGraph(TestCase):

    def test_add_edge(self):
        graph = DiGraph()
        a = Node("a")
        graph.add_node(a)
        b = Node("b")
        graph.add_node(b)

        graph.add_edge(Edge(Node("a"), b))

        self.assertTrue(b in graph.get_children(a))

    def test_add_edge_exp(self):
        graph = DiGraph()
        with self.assertRaises(ValueError):
            graph.add_edge(Edge(Node("a"), Node("b")))

    def test_add_node(self):
        graph = DiGraph()
        a = Node("a")
        graph.add_node(a)
        b = Node("b")
        graph.add_node(b)

        self.assertTrue(graph.has_node(a))
        self.assertTrue(graph.has_node(b))

    def test_add_node_exp(self):
        graph = DiGraph()
        graph.add_node(Node("a"))
        with self.assertRaises(ValueError):
            graph.add_node(Node("a"))
