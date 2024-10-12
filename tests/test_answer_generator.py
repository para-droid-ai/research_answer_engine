import unittest
from engine.answer_generator import generate_answer

class TestAnswerGenerator(unittest.TestCase):
    def test_generate_answer(self):
        self.assertEqual(generate_answer(["step1", "step2"]), "This is the generated answer.")

if __name__ == '__main__':
    unittest.main()
