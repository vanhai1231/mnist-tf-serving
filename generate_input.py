import tensorflow as tf
import json

# Lấy một ảnh từ tập MNIST test
(_, _), (x_test, _) = tf.keras.datasets.mnist.load_data()
img = x_test[0].reshape(28, 28, 1) / 255.0  # chuẩn hoá ảnh

# Đóng gói thành JSON
data = {"instances": [img.tolist()]}

# Ghi file test
with open("test/input.json", "w") as f:
    json.dump(data, f)

print("Đã tạo file test/input.json thành công.")
