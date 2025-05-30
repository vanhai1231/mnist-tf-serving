FROM tensorflow/serving

# Copy model vào thư mục mặc định của TF Serving
COPY models/mnist /models/mnist

# Chạy TF Serving với model "mnist"
ENTRYPOINT ["/usr/bin/tensorflow_model_server", 
            "--rest_api_port=8501", 
            "--model_name=mnist", 
            "--model_base_path=/models/mnist"]
