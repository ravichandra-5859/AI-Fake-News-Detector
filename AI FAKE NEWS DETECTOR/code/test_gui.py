import unittest
from app import FakeNewsDetectorApp
import tkinter as tk

class TestFakeNewsDetectorGUI(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.app = FakeNewsDetectorApp(self.root)
        self.root.update()  # Initialize UI
        
    def test_initial_state(self):
        # Verify initial UI state
        self.assertEqual(self.app.entry.get("1.0", "end-1c"), "")
        self.assertEqual(self.app.result_box["text"], "")
        self.assertEqual(self.app.confidence_label["text"], "0%")
        
    def test_clear_function(self):
        # Test clear functionality
        self.app.entry.insert("1.0", "Test headline")
        self.app.result_box.config(text="Result", background="red")
        self.app.confidence_meter["value"] = 50
        self.app.confidence_label["text"] = "50%"
        
        self.app.clear_all()
        
        self.assertEqual(self.app.entry.get("1.0", "end-1c"), "")
        self.assertEqual(self.app.result_box["text"], "")
        self.assertEqual(self.app.confidence_label["text"], "0%")
        
    def tearDown(self):
        self.root.destroy()

if __name__ == "__main__":
    unittest.main()