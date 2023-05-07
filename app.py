from flask import Flask,request
from flask_cors import CORS,cross_origin
import easyocr
import cv2
import numpy as np
import requests


app = Flask(__name__)
CORS(app)


@app.route('/api/textrec',methods=["GET","POST"])
def text_rec():
    image = request.data
    nparr = np.fromstring(image, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    cv2.imwrite("frame.jpg",img)
    
    # Initialize the OCR reader
    reader = easyocr.Reader(['en'])

    # Get the text from the image
    result = reader.readtext(image)
    #print(result)
    text = ''
    for item in result:
        text += item[1] + ' '

    # Print the text
    print(">>>")
    print(text)
    print(">>>")

  
    data = {"key1": "value1", "key2": "value2"}

    response = requests.post("https://bingchattest.onrender.com/api/message/api/message", json={"message":f"Please tell me what this text is about -> {text}"})
    print(response.json())
    description = response.json()["text"]

    return {"text":text,"description":description}

app.run(debug=False)