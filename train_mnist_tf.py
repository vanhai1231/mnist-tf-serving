import tensorflow as tf
from tensorflow import keras
import os

# Load dữ liệu
(x_train, y_train), _ = keras.datasets.mnist.load_data()
x_train = x_train.reshape(-1, 28, 28, 1).astype("float32") / 255.0

# Tạo model đơn giản
model = keras.Sequential([
    keras.layers.Conv2D(16, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    keras.layers.Flatten(),
    keras.layers.Dense(10, activation='softmax')
])
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

model.fit(x_train, y_train, epochs=1)

# Lưu dưới định dạng TensorFlow Serving
save_path = os.path.join("models", "mnist", "1")
model.export(save_path) 
print(f"Model saved to {save_path}")
