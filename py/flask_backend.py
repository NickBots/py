from flask import Flask,render_template, request,json, jsonify
from flask_cors import CORS

from get_emotions import random_emotions_generation
from get_tweets import tweetsRetriever

import random, string, os

app = Flask(__name__)
CORS(app)


@app.route('/')
def hello():
    return "Backend from PyPlutchik - Built on Flask"

@app.route('/getTweets', methods=['POST'])
def getTweets():
    user =  request.form['user']
    tweets = tweetsRetriever(user)
    return jsonify(
        data=tweets,
    )

@app.route('/generateRandomEmotions', methods=['POST'])
def generateRandomEmotions():
    data = random_emotions_generation()
    json_f = json_formatter(data)
    fileID = write_json(json_f)
    plot2()
    return jsonify(fileID=fileID)

@app.route('/deleteFile', methods=['POST'])
def deleteFile():
    fileName =  request.form['fileID']
    os.path.isfile("./temp/"+fileName+".json")
    os.remove("./temp/"+fileName+".json")
    return "success"

@app.route('/textUpload', methods=['POST'])
def textUpload():
    fileID = generateRandomID()
    upload = request.files.get('file')
    upload.save("./temp/" + fileID + ".txt")
    return "success"

@app.route('/userInput', methods=['POST'])
def userInput():
    text =  request.form['userInput']
    print(text)
    return jsonify(input=text)



def json_formatter(unformatted_data):
    formatted_data = []
    formatted_data.append('[\n{\n"emotion": "joy",\n "degree_0": "'+str(unformatted_data['joy'])+'",\n "degree_1": "0",\n "degree_2": "0",\n "total": "'+str(unformatted_data['joy'])+'"\n}')
    formatted_data.append('{\n"emotion": "trust",\n "degree_0": "'+str(unformatted_data['trust'])+'",\n "degree_1": "0",\n "degree_2": "0",\n "total": "'+str(unformatted_data['trust'])+'"\n}')
    formatted_data.append('{\n"emotion": "fear",\n"degree_0": "'+str(unformatted_data['fear'])+'",\n "degree_1": "0",\n "degree_2": "0",\n "total": "'+str(unformatted_data['fear'])+'"\n}')
    formatted_data.append('{\n"emotion": "surprise",\n "degree_0": "'+str(unformatted_data['surprise'])+'",\n "degree_1": "0",\n "degree_2": "0",\n "total": "'+str(unformatted_data['surprise'])+'"\n}')
    formatted_data.append('{\n"emotion": "sadness",\n "degree_0": "'+str(unformatted_data['sadness'])+'",\n "degree_1": "0",\n "degree_2": "0",\n "total": "'+str(unformatted_data['sadness'])+'"\n}')
    formatted_data.append('{\n"emotion": "disgust",\n "degree_0": "'+str(unformatted_data['disgust'])+'",\n "degree_1": "0",\n "degree_2": "0",\n "total": "'+str(unformatted_data['disgust'])+'"\n}')
    formatted_data.append('{\n"emotion": "anger",\n "degree_0": "'+str(unformatted_data['anger'])+'",\n "degree_1": "0",\n "degree_2": "0",\n "total": "'+str(unformatted_data['anger'])+'"\n}')
    formatted_data.append('{\n"emotion": "anticipation",\n "degree_0": "'+str(unformatted_data['anticipation'])+'",\n "degree_1": "0",\n "degree_2": "0",\n "total": "'+str(unformatted_data['anticipation'])+'"\n}]\n')
    return formatted_data

def write_json(formatted_data):
    fileID = generateRandomID()
    temp_file = open("./temp/"+fileID+".json","w+")
    temp_file.write(",\n".join(map(str, formatted_data)))
    temp_file.close()
    return fileID

def generateRandomID():
    fileID = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(32))
    return fileID

"""import matplotlib.pyplot as plt
from pyplutchik import plutchik

def plot2():
    scores = random_emotions_generation
    filename = "./temp/"+generateRandomID+".png"
    plutchik(scores)
    plt.savefig(filename, bbox_inches = 'tight')"""


if __name__=="__main__":
    app.run()

""" export FLASK_APP=flask_backend.py
python -m flask run """
