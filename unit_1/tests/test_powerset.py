from unittest import TestCase
from solutions import powerset_with_itertools


class TestPowerset(TestCase):
    def test_powerset(self):
        expected = [(),
                    (1,),
                    (2,),
                    (3,),
                    (1, 2),
                    (1, 3),
                    (2, 3),
                    (1, 2, 3)]
        items = [1, 2, 3]
        actual = powerset_with_itertools.powerset(items)

        for comb in actual:
            expected.remove(comb)

        self.assertTrue(len(expected) == 0)


