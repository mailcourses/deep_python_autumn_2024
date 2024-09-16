import unittest
from unittest import mock

from user import User


class TestUser(unittest.TestCase):

    def test_init(self):
        usr = User("steve", 42)
        self.assertEqual("steve", usr.name)
        self.assertEqual(42, usr.age)

    def test_greetings(self):
        usr = User("steve", 42)
        self.assertEqual("steve", usr.name)
        self.assertEqual("Hello, steve!", usr.greetings())

        usr = User("", 42)
        self.assertEqual("", usr.name)
        self.assertEqual("Hello, !", usr.greetings())

    def test_birthday(self):
        usr = User("steve", 42)
        self.assertEqual(42, usr.age)
        self.assertEqual(43, usr.birthday())
        self.assertEqual(43, usr.age)

    def test_friends_not_impl(self):
        usr = User("steve", 42)

        with self.assertRaises(NotImplementedError):
            usr.get_friends()

    def test_friends_empty(self):
        usr = User("steve", 42)

        with mock.patch("user.fetch_vk_api") as mock_api:
            mock_api.return_value = []

            friends = usr.get_friends()
            self.assertEqual([], friends)

            calls = [
                mock.call("/friends", "steve", part=None),
            ]
            self.assertEqual(calls, mock_api.mock_calls)

            friends = usr.get_friends(name_part="apple")
            self.assertEqual([], friends)

            calls = [
                mock.call("/friends", "steve", part=None),
                mock.call("/friends", "steve", part="APPLE"),
            ]
            self.assertEqual(calls, mock_api.mock_calls)

    def test_friends_single(self):
        usr = User("steve", 42)

        with mock.patch("user.fetch_vk_api") as mock_api:
            mock_api.side_effect = [["voz"], ["voz", "lisa"]]

            friends = usr.get_friends()
            self.assertEqual(["voz"], friends)

            calls = [
                mock.call("/friends", "steve", part=None),
            ]
            self.assertEqual(calls, mock_api.mock_calls)

            friends = usr.get_friends("is")
            self.assertEqual(["lisa"], friends)

            calls = [
                mock.call("/friends", "steve", part=None),
                mock.call("/friends", "steve", part="IS"),
            ]
            self.assertEqual(calls, mock_api.mock_calls)

            # friends = usr.get_friends("is")

    @mock.patch("user.fetch_vk_api")
    def test_friends_no_filter(self, mock_api):
        usr = User("steve", 42)

        def get_friends(*_, **__):
            return ["voz", "lisa"]

        mock_api.side_effect = get_friends

        friends = usr.get_friends()
        self.assertEqual(["voz", "lisa"], friends)

        calls = [
            mock.call("/friends", "steve", part=None),
        ]
        self.assertEqual(calls, mock_api.mock_calls)

        friends = usr.get_friends()
        self.assertEqual(["voz", "lisa"], friends)

        calls = [
            mock.call("/friends", "steve", part=None),
            mock.call("/friends", "steve", part=None),
        ]
        self.assertEqual(calls, mock_api.mock_calls)

    @mock.patch("user.fetch_vk_api")
    def test_friends_connection_error(self, mock_api):
        usr = User("steve", 42)

        mock_api.side_effect = Exception("connection error")

        with self.assertRaises(Exception) as err:
            usr.get_friends()
            self.assertEqual("connection error", str(err.exception))

        calls = [
            mock.call("/friends", "steve", part=None),
        ]
        self.assertEqual(calls, mock_api.mock_calls)

        with self.assertRaises(Exception) as err:
            usr.get_friends("is")
            self.assertEqual("connection error", str(err.exception))

        calls = [
            mock.call("/friends", "steve", part=None),
            mock.call("/friends", "steve", part="IS"),
        ]
        self.assertEqual(calls, mock_api.mock_calls)
