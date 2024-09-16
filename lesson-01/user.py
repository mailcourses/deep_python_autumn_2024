from vk_api import fetch_vk_api


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greetings(self):
        return f"Hello, {self.name}!"

    def birthday(self):
        self.age += 1
        return self.age

    def get_friends(self, name_part=None):
        if name_part:
            name_part = name_part.upper()

        friends = fetch_vk_api(
            "/friends", self.name, part=name_part
        )

        if name_part is not None:
            name_part = name_part.lower()
            friends = [
                fr for fr in friends if name_part in fr
            ]

        return friends
