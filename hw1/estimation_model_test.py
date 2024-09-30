import unittest
from predict_massage_mood import predict_message_mood


class TestEstimationModel(unittest.TestCase):

    def test_empty_string(self):
        prediction = predict_message_mood('')
        self.assertEqual('неуд', prediction)

    def test_rate_change(self):
        prediction = predict_message_mood('Добрый день!')
        self.assertEqual('отл', prediction)

        prediction = predict_message_mood('Добрый день!', 0.5, 1)
        self.assertEqual('норм', prediction)

        prediction = predict_message_mood('Добрый день!', 0.9, 1)
        self.assertEqual('неуд', prediction)
