import unittest
from detector import NewsDetector

class TestNewsDetector(unittest.TestCase):
    def setUp(self):
        self.detector = NewsDetector()
    
    def test_preprocessing(self):
        test_cases = [
            ("HELLO World!", "hello world"),
            ("Visit https://example.com", "visit"),
            ("This costs $100!", "this costs 100"),
            ("Extra   spaces", "extra spaces")
        ]
        
        for input_text, expected in test_cases:
            with self.subTest(input=input_text):
                self.assertEqual(self.detector.preprocess_text(input_text), expected)
    
    def test_detection(self):
        test_cases = [
            ("BREAKING: Shocking discovery!", ("Fake News", 100)),
            ("Official government statement confirms", ("Real News", 100)),
            ("Peer-reviewed scientific study", ("Real News", 100)),
            ("Viral unbelievable secret exposed", ("Fake News", 100)),
            ("Regular news without keywords", ("Unclear", 0)),
            ("Satire: unbelievable news", ("Unclear", 50))  # Context modifier test
        ]
        
        for headline, expected in test_cases:
            with self.subTest(headline=headline):
                result = self.detector.detect_fake_news(headline)
                self.assertEqual(result[0], expected[0])
                self.assertAlmostEqual(result[1], expected[1], delta=10)  # Allow 10% variance
                
    def test_edge_cases(self):
        test_cases = [
            ("", ("Unclear", 0)),  # Empty input
            ("   ", ("Unclear", 0)),  # Whitespace only
            ("A" * 1000, ("Unclear", 0))  # Long text without keywords
        ]
        
        for headline, expected in test_cases:
            with self.subTest(headline=headline):
                self.assertEqual(self.detector.detect_fake_news(headline), expected)

if __name__ == "__main__":
    unittest.main()