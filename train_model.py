import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import numpy as np
import os

def create_and_train_model():
    """
    Create and train a CNN model for ASL alphabet recognition
    Note: You need the dataset to train this properly
    """
    
    # Model architecture
    model = keras.Sequential([
        layers.Conv2D(32, (3, 3), activation='relu', input_shape=(64, 64, 3)),
        layers.BatchNormalization(),
        layers.MaxPooling2D((2, 2)),
        
        layers.Conv2D(64, (3, 3), activation='relu'),
        layers.BatchNormalization(),
        layers.MaxPooling2D((2, 2)),
        
        layers.Conv2D(128, (3, 3), activation='relu'),
        layers.BatchNormalization(),
        layers.MaxPooling2D((2, 2)),
        
        layers.Flatten(),
        layers.Dropout(0.5),
        layers.Dense(512, activation='relu'),
        layers.Dropout(0.5),
        layers.Dense(26, activation='softmax')  # 26 classes A-Z
    ])
    
    model.compile(
        optimizer='adam',
        loss='categorical_crossentropy',
        metrics=['accuracy']
    )
    
    print("Model created successfully!")
    print("To train this model, you need:")
    print("1. ASL alphabet dataset (45,000 training + 6,500 test images)")
    print("2. Images organized in folders A-Z")
    print("3. Run training with your dataset")
    
    return model

if __name__ == "__main__":
    model = create_and_train_model()
    model.summary()