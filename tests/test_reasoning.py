import unittest
from engine.reasoning import reason

class TestReasoning(unittest.TestCase):
    def test_reason(self):
        self.assertEqual(reason({"intent": "research_query"}), ["step1", "step2"])

if __name__ == '__main__':
    unittest.main()
