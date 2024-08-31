import secrets
import os.path
from PIL import Image

from flask import current_app

def save_image(image):
    random_hex = secrets.token_hex(15)
    _, f_ext = os.path.splitext(image.filename)
    image_fn = random_hex + f_ext
    image_path = os.path.join(current_app.config['SERVER_PATH'], image_fn)
    output_size = (1000, 1000)
    i = Image.open(image)
    i.thumbnail(output_size)
    i.save(image_path)
    return image_fn