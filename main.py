from flask import Flask, request, jsonify
import io
import json
import torch
from torch.jit import Error
from torchvision import transforms
from PIL import Image
from Classifier import Classifier

#Trained model's class names
CLASS_NAMES = {0:"Fire", 1: "Neutral", 2: "Smoke"}

app = Flask(__name__)

classifier =  Classifier('model/AlexNet_v2.ptl')

@app.route('/', methods=['POST'])
def post():
	if request.method == 'POST':
		try:
			file = request.files['image']
			image = file.read()
			prediction = classifier.predict(image)
			return jsonify({'preditced-class': CLASS_NAMES[prediction]})
		except :
			return jsonify({"error": "No image file found!"}) , 404
		

if __name__ == "__main__":
	app.run(debug=True)