#!/usr/bin/env python3
"""
    Assign:
        TestGithubOrgClient Class.
"""
from unittest.mock import patch, MagicMock
from parameterized import parameterized
from client import GithubOrgClient
from utils import get_json
import unittest


class TestGithubOrgClient(unittest.TestCase):
    """
        Assign TestGithubOrgClient Class to test
        org method of GithubOrgClinet class.
    """

    @parameterized.expand([
        ("google", {"login": "google"}),
        ("abc", {"login": "abc"})
        ])
    @patch('client.get_json')
    def test_org(self, orgs: str, resp: dict, mock_response: MagicMock):
        """
            Testing org method.
        """
        mock_response.return_value = MagicMock(return_value=resp)
        github_org = GithubOrgClient(orgs)
        self.assertEqual(github_org.org(), resp)
        mock_response.assert_called_once_with(
            "https://api.github.com/orgs/{}".format(orgs)
        )
