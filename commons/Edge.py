#! /usr/bin/env python3
from commons.Node import Node


class Edge(object):

    def __init__(self, src, dst) -> None:
        self._src = src
        self._dst = dst
        super().__init__()

    def get_src(self):
        return self._src

    def get_dst(self):
        return self._dst

    def get_reversed_copy(self):
        return Edge(self._dst, self._src)

    def __str__(self) -> str:
        return '<' + str(self._src) + ',' + str(self._dst) + '>'


if __name__ == "__main__":
    print(Edge(Node("src"), Node("dst")))
