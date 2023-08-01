#!/usr/bin/env python3
"""
    Assign:
        TestGithubOrgClient Class.
"""
from unittest.mock import patch, MagicMock, PropertyMock
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

    def test_public_repos_url(self) -> None:
        """
           Testing _public_repos_urls method
        """

        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock:
            mock.return_value = {
                "repos_url": "https://api.github.com/users/google/repos"}
            self.assertEqual(GithubOrgClient('google')._public_repos_url,
                             "https://api.github.com/users/google/repos")

    def test_public_repos(self) -> None:
        """
           Testing public_repos method.
        """

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, license: dict, key: str, result: bool) -> None:
        """
           Testing has_license
        """
        org = GithubOrgClient('google')
        org_has_license = org.has_license(license, key)
        self.assertEqual(org_has_license, result)
