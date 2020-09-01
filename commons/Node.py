#! /usr/bin/env python3
from typing import Any


class Node(object):

    def __init__(self, name):
        self._name = name
        super().__init__()

    def get_name(self) -> Any:
        return self._name

    def __str__(self) -> str:
        return self._name

    def __hash__(self) -> int:
        return hash(self._name)

    def __eq__(self, o: object) -> bool:
        return isinstance(o, Node) and self._name == o.get_name()


if __name__ == "__main__":
    print(Node("new_node"))
