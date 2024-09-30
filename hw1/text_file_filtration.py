class Filtratrion():
    def __init__(self, file_path: str, search_words: list, stop_words: list):
        self.file_path = file_path
        self.search_words = tuple({word.lower() for word in set(search_words)})
        self.stop_words = tuple({word.lower() for word in set(stop_words)})

    def generator(self, file):

        for line in file:
            words = {word.lower() for word in line.split()}
            stop = False
            for stop_word in self.stop_words:
                if stop_word in words:
                    stop = True
                    break
            if stop:
                continue

            for search_word in self.search_words:
                if search_word in words:
                    yield line
                    break

    def filter(self) -> list:
        try:
            with open(self.file_path, 'r') as file:
                return list(self.generator(file))
        except FileNotFoundError:
            print('File Not Found')
