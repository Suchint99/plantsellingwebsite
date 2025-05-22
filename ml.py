# Sample training data format
import tensorflow as tf
import numpy as np

# Real-world training data format
X = np.array([
    [0.8, 0.1, 0.9],  # High stress, low energy, needs air purification
    [0.2, 0.9, 0.3],  # Low stress, high energy
    # ... more samples
])

y = np.array([
    [1, 0, 0],  # Peace Lily
    [0, 0, 1],  # Jasmine
    # ... more labels
])

model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(3,)),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(3, activation='softmax')
])

model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])
model.fit(X, y, epochs=100)
model.save('plant_recommender.h5')