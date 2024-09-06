from flask import Blueprint, request, jsonify, current_app
import os

upload_image = Blueprint('upload_image', __name__)

@upload_image.route('/upload', methods=['POST'])
def upload_image_route():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400

    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file:
        # Save the file to the upload folder
        file_path = os.path.join(current_app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)
        
        # Simulate model processing (you can add model code here later)
        return jsonify({'message': 'File successfully uploaded', 'file_path': file_path}), 200
