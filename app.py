from flask import Flask, render_template, request, send_file, redirect, url_for
import numpy as np
import os
from model import image_pre, predict
import time

app = Flask(__name__)

UPLOAD_FOLDER = "C:/Users/NISCHITHA/Desktop/covid/app/static"
ALLOWED_EXTENSIONS = set(['png'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
image_filename = None  # Initialize image_filename as None

@app.route('/')
def home():
    return render_template('index.html', image_filename=image_filename)

@app.route('/', methods=['POST'])
def upload_file():
    global image_filename  # Access the global image_filename variable
    if 'file1' not in request.files:
        return 'There is no file1 in the form!'

    file1 = request.files['file1']

    if file1.filename == '':
        return render_template('index.html', result="No selected file")  # Display a message in the result area

    if file1:
        # Generate a unique filename for the uploaded image, e.g., using a timestamp
        timestamp = str(int(time.time()))
        filename = f'upload_{timestamp}.png'
        path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file1.save(path)
        data = image_pre(path)
        s = predict(data)
        if s == 1:
            result = 'No COVID detected'
        else:
            result = 'COVID detected'

        # Clear the uploaded file data to avoid displaying "No selected file" on subsequent submissions
        request.files['file1'].filename = ''
        image_filename = filename  # Update the global image_filename

        return render_template('index.html', result=result, image_filename=image_filename)

if __name__ == "__main__":
    app.run(debug=True)
