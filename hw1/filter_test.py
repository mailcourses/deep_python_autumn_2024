import unittest
from text_file_filtration import Filtratrion


class TestFilter(unittest.TestCase):
    
    def test_1(self):
        file = '/Users/dkravchenko/deep_python_autumn_2024/hw1/text1.txt'
        search_words = []
        stop_words = []
        model = Filtratrion(file, search_words, stop_words)
        answer = []
        self.assertEqual(answer, model.filter())

    def test_2(self):
        file = '/Users/dkravchenko/deep_python_autumn_2024/hw1/text1.txt'
        search_words = ['бычок', 'доска']
        stop_words = []
        model = Filtratrion(file, search_words, stop_words)
        answer = ['Идет бычок качается\n',
                  'Ох доска кончается\n']
        self.assertEqual(answer, model.filter())

    def test_3(self):
        file = '/Users/dkravchenko/deep_python_autumn_2024/hw1/text1.txt'
        search_words = ['бычок', 'доска']
        stop_words = ['Ох']
        model = Filtratrion(file, search_words, stop_words)
        answer = ['Идет бычок качается\n']
        self.assertEqual(answer, model.filter())

    def test_4(self):
        file = '/Users/dkravchenko/deep_python_autumn_2024/hw1/text1.txt'
        search_words = ['бычок', 'доска']
        stop_words = ['идет', 'ох']
        model = Filtratrion(file, search_words, stop_words)
        answer = []
        self.assertEqual(answer, model.filter())

    def test_5(self):
        file = '/Users/dkravchenko/deep_python_autumn_2024/hw1/text1.txt'
        search_words = ['бычок', 'идет']
        stop_words = []
        model = Filtratrion(file, search_words, stop_words)
        answer = ['Идет бычок качается\n']
        self.assertEqual(answer, model.filter())

    def test_6(self):
        file = '/Users/dkravchenko/deep_python_autumn_2024/hw1/text2.txt'
        search_words = ['love']
        stop_words = []
        model = Filtratrion(file, search_words, stop_words)
        answer = ['My love is beyond the pain\n',
                  'My love is beyond the pain\n',
                  'My love is beyond the pain Hey\n']
        self.assertEqual(answer, model.filter())

    def test_7(self):
        file = '/Users/dkravchenko/deep_python_autumn_2024/hw1/text2.txt'
        search_words = ['love']
        stop_words = ['hey']
        model = Filtratrion(file, search_words, stop_words)
        answer = ['My love is beyond the pain\n',
                  'My love is beyond the pain\n']
        self.assertEqual(answer, model.filter())

    def test_8(self):
        file = '/Users/dkravchenko/deep_python_autumn_2024/hw1/text2.txt'
        search_words = ['love', 'ooh', 'faith']
        stop_words = ['hey', 'oh']
        model = Filtratrion(file, search_words, stop_words)
        answer = ['My love is beyond the pain\n',
                  'My love is beyond the pain\n',
                  'Ooh yeah\n',
                  'Ooh\n',
                  'Ooh Indescribable\n',
                  'So just have faith Just have faith in me\n']
        self.assertAlmostEqual(len(answer), len(model.filter()))
