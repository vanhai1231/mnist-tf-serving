import json
import requests

# Đọc input test
with open("test/input.json") as f:
    data = json.load(f)

# Gửi yêu cầu đến API Render
res = requests.post(
    "https://mnist-tf-serving.onrender.com/v1/models/mnist:predict",
    json=data
)

# Xử lý kết quả
probs = res.json()["predictions"][0]
predicted_digit = probs.index(max(probs))

print(f"Kết quả dự đoán: {predicted_digit}")
