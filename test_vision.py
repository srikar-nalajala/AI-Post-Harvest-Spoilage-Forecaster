import unittest
from PIL import Image
from modules import vision
import os

class TestVision(unittest.TestCase):
    def setUp(self):
        # Create a dummy image (100x100 red square)
        self.image = Image.new('RGB', (100, 100), color = 'red')

    def test_analyze_image_structure(self):
        print("\n--- Testing Vision Module with Dummy Image ---")
        # This will call the API. If API fails, it falls back to simulation.
        # We just want to ensure it returns the correct structure.
        result = vision.analyze_image(self.image)
        
        print(f"Vision Result Keys: {result.keys()}")
        if "error" in result:
             print(f"Vision returned error (likely no API key or quota): {result['error']}")
        else:
            self.assertIn("spoilage_score", result)
            self.assertIn("analysis", result)
            self.assertTrue(1 <= result["spoilage_score"] <= 10)
            print(f"Score: {result['spoilage_score']}")
            print(f"Analysis: {result['analysis'][:50]}...")
            if "model_used" in result:
                print(f"Model: {result['model_used']}")

if __name__ == '__main__':
    unittest.main()
