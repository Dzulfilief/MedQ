# Gunakan base image Python
FROM python:3.10-slim

# Set direktori kerja di container
WORKDIR /app

# Copy semua file ke dalam container
COPY . .

# Install dependensi
RUN pip install flask

# Buka port 5000
EXPOSE 5000

# Jalankan aplikasinya
CMD ["python", "app.py"]
