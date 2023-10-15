from flask import Flask, request, jsonify, render_template
import os
from flask_cors import CORS, cross_origin
from cnn_classifier.utils.common import decodeImage
from cnn_classifier.pipeline.predication import PredictionPipeline
from src.cnn_classifier import logger

app= Flask(__name__)
CORS(app)

class Clientapp: 
    def __init__(self): 
        self.filename="inputImage.jpg"
        self.classifer= PredictionPipeline(self.filename)

@app.route("/", methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')

@app.route("/train", methods=['GET', 'POST'])
@cross_origin()
def training():
    os.system("python main.py")
    return "Training done sucessfully..."

@app.route("/predict", methods=['POST'])
@cross_origin()
def predictRoute():
    try: 
        image=request.json['image']
        decodeImage(image, ClApp.filename)
        result=ClApp.classifer.predict()
        return jsonify(result)
    except Exception as e:
        raise e


if __name__ == "__main__": 
    ClApp=Clientapp()
    app.run(host="0.0.0.0", debug=True)
