FROM tensorflow/serving

# Copy model vào đúng thư mục TensorFlow Serving
COPY models/mnist /models/mnist

# Khởi chạy TensorFlow Serving REST API
ENTRYPOINT ["/usr/bin/tensorflow_model_server", "--rest_api_port=8501", "--model_name=mnist", "--model_base_path=/models/mnist"]
