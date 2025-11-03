import tensorflow as tf
from tensorflow import keras
import numpy as np

def create_dummy_model():
    """Create a simple dummy model for testing purposes"""
    print("Creating dummy model for testing...")
    
    # Create a simple CNN model
    model = keras.Sequential([
        keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(64, 64, 3)),
        keras.layers.MaxPooling2D((2, 2)),
        keras.layers.Conv2D(64, (3, 3), activation='relu'),
        keras.layers.MaxPooling2D((2, 2)),
        keras.layers.Conv2D(64, (3, 3), activation='relu'),
        keras.layers.Flatten(),
        keras.layers.Dense(64, activation='relu'),
        keras.layers.Dense(26, activation='softmax')  # 26 classes for A-Z
    ])
    
    model.compile(optimizer='adam',
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])
    
    # Save the model
    model.save('Trained_model.h5')
    print("Dummy model saved as Trained_model.h5")
    print("Note: This is just for testing. You need a properly trained model for accurate predictions.")

if __name__ == "__main__":
    create_dummy_model()