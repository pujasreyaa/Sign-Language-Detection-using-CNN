import cv2
import numpy as np
from findproj.predictor import predictor

def test_predictor():
    print("Testing predictor function...")
    
    # Create a test image
    test_img = np.ones((64, 64, 3), dtype=np.uint8) * 128
    cv2.imwrite('test_image.png', test_img)
    
    # Test prediction
    result = predictor('test_image.png')
    print(f"Prediction result: {result}")
    
    # Clean up
    import os
    if os.path.exists('test_image.png'):
        os.remove('test_image.png')
    
    return result

if __name__ == "__main__":
    test_predictor()