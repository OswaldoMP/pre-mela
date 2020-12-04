import json
import os

from flask import Flask, request, url_for
from flask_cors import CORS
from werkzeug.utils import secure_filename

from service.Binarizacion import Binarizacion

UPLOAD_FOLDER = './public/files'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

CORS(app)

@app.route('/')
def hello():
    return 'Hello word'

@app.route('/analyze', methods=['POST'])
def analyze():
    if request.method == 'POST':
        image_file = request.files['image']
        file_name = secure_filename(image_file.filename)
        # image_file.save('./public/files/'  + secure_filename(image_file.filename))
        image_file.save(os.path.join(app.config['UPLOAD_FOLDER'], file_name))
        
        print(f'{UPLOAD_FOLDER}/{file_name}', os.path.join(app.config['UPLOAD_FOLDER']))
        binarization = Binarizacion(f'./public/files/{file_name}')
        binarization.binaryImage()
        binarization.otsuImage()
        binarization.adatativeImage()
        binarization.fondoMorfologico()
        
        m, color, diametro, pre = binarization.analize()
        
        return json.dumps({'ok': True, 'url': f'./public/files/{file_name}',
                           'm': m,
                           'color': color,
                           'diametro': diametro,
                           'pre': pre})
        
    return json.dumps({'ok': False})
