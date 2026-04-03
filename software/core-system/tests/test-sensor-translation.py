import unittest
from sensor_translation.translation_engine import TranslationEngine

class TestSensorTranslation(unittest.TestCase):
    def setUp(self):
        self.engine = TranslationEngine()

    def test_impact_translation(self):
        result = self.engine.translate_accelerometer(10, 10, 10)
        self.assertIn("Ouch", result)

    def test_temp_translation(self):
        result = self.engine.translate_temperature(10)
        self.assertIn("cold", result)

if __name__ == '__main__':
    unittest.main()\n