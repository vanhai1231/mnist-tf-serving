# Triển khai MNIST TensorFlow Serving trên Render.com

Dự án này minh hoạ cách triển khai một mô hình phân loại chữ số MNIST đơn giản bằng **TensorFlow Serving** trên nền tảng miễn phí **Render.com**.

---

## Tính năng

* Triển khai mô hình TensorFlow như một REST API
* Đóng gói toàn bộ bằng Docker
* Chạy và phục vụ trên nền tảng Render.com (cloud miễn phí)

---

## 📁 Cấu trúc thư mục dự án

```
mnist-tf-serving/
├── models/
│   └── mnist/
│       └── 1/
│           ├── saved_model.pb
│           └── variables/
├── Dockerfile
├── render.yaml
├── README.md
```

---

## Mô hình

Mô hình được huấn luyện bằng TensorFlow/Keras để phân loại chữ số từ tập dữ liệu MNIST. Mô hình được xuất ra theo định dạng **SavedModel** (yêu cầu của TensorFlow Serving).

Lệnh để huấn luyện và xuất model:

```bash
python train_mnist_tf.py
```

Sau khi chạy, bạn sẽ có thư mục:

```
models/mnist/1/
├── saved_model.pb
└── variables/
```

---

## 🐳 Dockerfile

```Dockerfile
FROM tensorflow/serving
COPY models/mnist /models/mnist
ENTRYPOINT ["/usr/bin/tensorflow_model_server", 
            "--rest_api_port=8501", 
            "--model_name=mnist", 
            "--model_base_path=/models/mnist"]
```

---

## ☁️ render.yaml (cấu hình tự động cho Render)

```yaml
services:
  - type: web
    name: mnist-tf-serving
    env: docker
    plan: free
    region: singapore
    dockerfilePath: ./Dockerfile
    envVars:
      - key: PORT
        value: 8501
```

---

## 🚀 Các bước triển khai

1. Push toàn bộ repo lên GitHub.
2. Truy cập [https://render.com](https://render.com), đăng nhập.
3. Bấm **New Web Service** → kết nối repo GitHub của bạn.
4. Render sẽ tự động build Docker image từ `render.yaml` và chạy service.
5. Sau vài phút, API REST sẽ có dạng:

```
https://<tên-service>.onrender.com/v1/models/mnist:predict
```

---

## 📬 Gửi yêu cầu để test API

Tạo file `test/input.json` với dữ liệu:

```json
{
  "instances": [
    [[[...giá trị ảnh 28x28 đã chuẩn hoá...]]]
  ]
}
```

Gửi bằng curl:

```bash
curl -X POST https://<tên-service>.onrender.com/v1/models/mnist:predict \
  -H "Content-Type: application/json" \
  -d @test/input.json
```

---

## 📌 Ghi chú

* Đảm bảo thư mục model có phiên bản là số (ví dụ `1/`)
* Có thể thay thế bằng bất kỳ mô hình TensorFlow nào khác
* Tài liệu REST API của TensorFlow Serving: [https://www.tensorflow.org/tfx/serving/api\_rest](https://www.tensorflow.org/tfx/serving/api_rest)

---

