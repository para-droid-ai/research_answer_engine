import unittest
from engine.query_parser import parse_query

class TestQueryParser(unittest.TestCase):
    def test_parse_query(self):
        self.assertEqual(parse_query("What is AI?")['intent'], "research_query")

if __name__ == '__main__':
    unittest.main()
