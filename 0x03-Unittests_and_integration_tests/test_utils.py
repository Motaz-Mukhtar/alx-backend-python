#!/usr/bin/env python3
"""
    Assign TestAccessNestedMap Class
"""
from utils import access_nested_map
from parameterized import parameterized
import unittest


class TestAccessNestedMap(unittest.TestCase):
    """
        Assign TestAccessNestedMap for testing
        utils.access_nested_map function
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
        ])
    def test_acess_nested_map(self, dict, path, excpected):
        """
            Testing utils.access_nested_map function.
        """
        tested_output = access_nested_map(dict, path)
        self.assertEqual(tested_output, excpected)