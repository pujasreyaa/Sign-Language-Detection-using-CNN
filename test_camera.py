import cv2

def test_camera():
    print("Testing camera access...")
    
    # Try to access camera
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("Cannot access camera 0, trying other indices...")
        for i in range(1, 4):
            cap = cv2.VideoCapture(i)
            if cap.isOpened():
                print(f"Camera found at index {i}")
                break
        else:
            print("No camera found!")
            return False
    else:
        print("Camera 0 is working!")
    
    # Test reading a frame
    ret, frame = cap.read()
    if ret:
        print(f"Successfully captured frame: {frame.shape}")
        print("Camera test PASSED!")
    else:
        print("Failed to capture frame")
        print("Camera test FAILED!")
    
    cap.release()
    return ret

if __name__ == "__main__":
    test_camera()