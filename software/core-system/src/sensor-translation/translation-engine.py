class TranslationEngine:
    def __init__(self):
        self.thresholds = {
            'impact': 5.0,
            'temp_cold': 15.0,
            'temp_hot': 30.0
        }

    def translate_accelerometer(self, x, y, z):
        magnitude = (x**2 + y**2 + z**2)**0.5
        if magnitude > self.thresholds['impact']:
            return "Ouch! That was a hard impact."
        return "Moving smoothly."

    def translate_temperature(self, celsius):
        if celsius < self.thresholds['temp_cold']:
            return "It's getting cold in here."
        elif celsius > self.thresholds['temp_hot']:
            return "It's getting quite hot."
        return "The temperature is comfortable."

    def translate_audio(self, transcript):
        return f"I heard someone say: '{transcript}'"\n