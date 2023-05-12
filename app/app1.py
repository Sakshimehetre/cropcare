import tensorflow as tf
from tensorflow import keras
from skimage import io
from tensorflow.keras.preprocessing import image
from flask import Flask, render_template, request, Markup
from werkzeug.utils import secure_filename
import numpy as np
import pandas as pd
from utils.suggestion import disease_dic
import os
import requests
import config
import pickle
import io
import cv2


model =tf.keras.models.load_model('D:\cropcare\models\Mymodel.h5',compile=False)
print('Model loaded. Check http://127.0.0.1:5000/')

disease_classes = ['Apple___Apple_scab',
                   'Apple___Black_rot',
                   'Apple___Cedar_apple_rust',
                   'Apple___healthy',
                   'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot',
                   'Corn_(maize)___Common_rust_',
                   'Corn_(maize)___Northern_Leaf_Blight',
                   'Corn_(maize)___healthy',
                   'Grape___Black_rot',
                   'Grape___Esca_(Black_Measles)',
                   'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)',
                   'Grape___healthy',
                   'Potato___Early_blight',
                   'Potato___Late_blight',
                   'Potato___healthy',
                   'Tomato___Bacterial_spot',
                   'Tomato___Early_blight',
                   'Tomato___Late_blight',
                   'Tomato___Leaf_Mold',
                   'Tomato___Septoria_leaf_spot',
                   'Tomato___Spider_mites Two-spotted_spider_mite',
                   'Tomato___Target_Spot',
                   'Tomato___Tomato_Yellow_Leaf_Curl_Virus',
                   'Tomato___Tomato_mosaic_virus',
                   'Tomato___healthy']

app = Flask(__name__)




def model_predict(img_path, model):
    img = image.load_img(img_path, grayscale=False, target_size=(256, 256))
    show_img = image.load_img(img_path, grayscale=False, target_size=(256, 256))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = np.array(x, 'float32')
    x /= 255
    preds = model.predict(x)
    return preds





@ app.route('/')
def home():
    title = 'CropCare - Home'
    return render_template('index.html', title=title)

@ app.route('/contactus', methods=['GET', 'POST'])
def contactus():
    title = 'CropCare - Contactus'
    return render_template('contact.html', title=title)

@ app.route('/chatus', methods=['GET'])
def chatus():
    return render_template('indexchat.html')


@app.route('/disease-predict', methods=['GET', 'POST'])
def disease_prediction():
    title = 'Harvestify - Disease Detection'

    if request.method == 'POST':
        f = request.files['file']

        # Save the file to ./uploads
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, 'uploads', secure_filename(f.filename))
        f.save(file_path)

        # Make prediction
        preds = model_predict(file_path, model)
        print(preds[0])
        a = preds[0]
        ind=np.argmax(a)
        print('Prediction:', disease_classes[ind])
        result=disease_classes[ind]
        result = Markup(str(disease_dic[disease_classes[ind]]))
        return render_template('disease-result.html', prediction=result, title=title)

        # if 'file' not in request.files:
        #     return redirect(request.url)
        # file = request.files.get('file')
        # if not file:
        #     return render_template('disease.html', title=title)
        # try:
        #     img = file.read()

        #     prediction = model_predict(img,model)
        #     print(ppreds[0])
        #     #prediction = Markup(str(disease_dic[prediction]))
        #     return render_template('disease-result.html', prediction=prediction, title=title)
        # except:
        #     pass
    return render_template('disease.html', title=title)


if __name__ == '__main__':
    app.run(debug=False)