#! /usr/bin/env python3
from commons.DiGraph import Graph
from commons.Node import Node


def dfs(graph: Graph, src_node: Node, dst_node: Node, current_path: [], current_shortest: [], print_current_path=False):
    current_path += [src_node]

    if print_current_path:
        print(stringify_path(current_path))

    if src_node == dst_node:
        return current_path

    for node in graph.get_children(src_node):
        if node not in current_path:
            if current_shortest is None or len(current_path) < len(current_shortest):
                new_path = dfs(graph, node, dst_node, current_path, current_shortest, print_current_path)
                if new_path is not None:
                    current_shortest = new_path
    return current_shortest


def bfs():
    return None


def stringify_path(path):
    result = ''
    for i in range(len(path)):
        result += str(path[i])
        if i != len(path) - 1:
            result += '->'
    return result


if __name__ == "__main__":
    print()
