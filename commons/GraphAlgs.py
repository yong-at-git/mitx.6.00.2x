#! /usr/bin/env python3
from commons.DiGraph import Graph
from commons.Node import Node


def dfs(graph: Graph, src_node: Node, dst_node: Node, current_path: [], current_shortest: [], print_current_path=False):
    current_path = current_path + [src_node]
    # += operator mutate the list; while a = a + b does not

    if print_current_path:
        print("Current DFS path:", stringify_path(current_path))

    if src_node == dst_node:
        return current_path

    for node in graph.get_children(src_node):
        if node not in current_path:
            if current_shortest is None or len(current_path) < len(current_shortest):
                new_path = dfs(graph, node, dst_node, current_path, current_shortest, print_current_path)
                if new_path is not None:
                    current_shortest = new_path
    return current_shortest


def bfs(graph: Graph, src_node: Node, dst_node: Node, print_current_path=False):
    init_path = [src_node]
    path_queue = [init_path]

    while len(path_queue) != 0:
        head_path = path_queue.pop(0)
        if print_current_path:
            print("Current BFS path:", stringify_path(head_path))
        last_node = head_path[-1]
        if last_node == dst_node:
            return head_path

        for next_node in graph.get_children(last_node):
            if next_node not in head_path:
                new_path = head_path + [next_node]
                path_queue.append(new_path)
    return None


def stringify_path(path):
    result = ''
    if path is None:
        return result

    for i in range(len(path)):
        result += str(path[i])
        if i != len(path) - 1:
            result += '->'
    return result


if __name__ == "__main__":
    print()
