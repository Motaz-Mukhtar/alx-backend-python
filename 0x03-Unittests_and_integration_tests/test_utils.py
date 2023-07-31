#!/usr/bin/env python3
"""
    Assign:
        TestAccessNestedMap Class
        TestGetJson Class
        TestMemoize Class
"""
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized
from unittest.mock import Mock, patch
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
    def test_access_nested_map(self, dict_map, path, excpected):
        """
            Testing utils.access_nested_map function.
        """
        tested_output = access_nested_map(dict_map, path)
        self.assertEqual(tested_output, excpected)

    @parameterized.expand([
        ({}, ("a",), 'a'),
        ({"a": 1}, ("a", "b"), 'b')
        ])
    def test_access_nested_map_exception(self, dict_map, path, excpected):
        """
            Testing utils.access_nested map function Exception.
        """
        with self.assertRaises(KeyError):
            tested_output = access_nested_map(dict_map, path)


class TestGetJson(unittest.TestCase):
    """
        Assign TestGetJson class for testing get_json().
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
        ])
    def test_get_json(self, test_url, test_payload):
        """
            Testing get_json().
        """
        mock = Mock()
        mock.json.return_value = test_payload
        with patch('requests.get', return_value=mock):
            response = get_json(test_url)
            self.assertEqual(response, test_payload)
            mock.json.assert_called_once()


class TestMemoize(unittest.TestCase):
    """
        Assign TestMemoize Class for testing
        meoize decorator.
    """

    def test_memoize(self):
        """
            Test memoize decorator.
        """

        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method',
                          return_value=42) as mock_method:
            test_spec = TestClass()
            test_spec.a_property
            test_spec.a_property
            mock_method.assert_called_once()
