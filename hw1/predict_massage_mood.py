class EstimationModel:
    def predict(self, message: str) -> float:
        total = sum(ord(char) for char in message)
        return total % 1000 / 1000

def predict_message_mood(
    message: str,
    bad_thresholds: float = 0.3,
    good_thresholds: float = 0.8,
) -> str:
    model = EstimationModel()
    rate = model.predict(message)
    if rate <= bad_thresholds:
        return 'неуд'
    elif rate >= good_thresholds:
        return 'отл'
    else:
        return 'норм'
