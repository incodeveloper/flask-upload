from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
import os


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    image = request.files['image']
    allowed_ext = {'png', 'jpg', 'jpeg'}

    if '.' in image.filename and image.filename.rsplit('.', 1)[1].lower() in allowed_ext:
        image_name = secure_filename(image.filename)
        image.save(os.path.join('uploads/', image_name))

        return jsonify({'status': 'ok'})
    else:
        return jsonify({'status': 'error'})
        


if __name__ == "main":
    app.run()