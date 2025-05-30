import tensorflow as tf
import json

(_, _), (x_test, _) = tf.keras.datasets.mnist.load_data()
img = x_test[0].reshape(28, 28, 1).tolist()  # reshape và convert sang list

data = {"instances": [img]}

with open("test/input.json", "w") as f:
    json.dump(data, f)
print("Saved test/input.json")
