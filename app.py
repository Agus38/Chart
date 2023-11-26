from flask import Flask, render_template, request, jsonify
import os
import cv2
import numpy as np
from tensorflow.keras.models import load_model

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def identify_candlestick(image_path):
    # Membaca gambar
    image = cv2.imread(image_path)
    
    # Proses identifikasi candlestick (sama seperti contoh sebelumnya)

    return "Sinyal Buy (Posisi Buy)"  # Gantilah dengan logika identifikasi yang sesuai

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/identify_candlestick', methods=['POST'])
def identify_candlestick_route():
    if 'image' in request.files:
        image_file = request.files['image']
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], image_file.filename)
        image_file.save(image_path)

        result = identify_candlestick(image_path)

        os.remove(image_path)  # Hapus file setelah diproses

        return jsonify({'result': result})
    else:
        return jsonify({'error': 'No image uploaded'})

if __name__ == '__main__':
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    app.run(debug=True)
