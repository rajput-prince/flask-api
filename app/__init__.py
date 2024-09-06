from flask import Flask
import os

def create_app():
    app = Flask(__name__)

    # Ensure the upload folder exists
    UPLOAD_FOLDER = 'uploads/'
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)

    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

    # Import and register the blueprint
    from .routes import upload_image
    app.register_blueprint(upload_image, url_prefix='/')

    return app
