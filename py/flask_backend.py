from flask import Flask,render_template, request,json, jsonify
from flask_cors import CORS

from get_emotions import random_emotions_generation
from get_tweets import tweetsRetriever
#from get_zscores import get_scores
from get_plot import plot
from send_email import sendMessage

import random, string, os, time

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello():
    return "Backend from PyPlutchik - Built on Flask"

@app.route('/getTweets', methods=['POST'])
def getTweets():
    user =  request.form['user']
    tweets = tweetsRetriever(user)
    """z_scores = get_scores(tweets)
        svgData = plot(z_scores)
        return jsonify(file=svgData)"""
    return jsonify(
        data=tweets,
    )

@app.route('/generateRandomEmotions', methods=['POST'])
def generateRandomEmotions():
    time.sleep(10)
    svgData = plot(random_emotions_generation())
    return jsonify(file=svgData)

@app.route('/textUpload', methods=['POST'])
def textUpload():
    upload = request.files.get('file')
    if(os.path.splitext(upload.filename)[1] != ".txt"):
        return jsonify(errMsg="Incorrect file format")
    else:
        fileID = generateRandomID()
        upload.save("temp/" + fileID + ".txt")
        with open("temp/"+fileID+".txt", 'r') as fr:
            text = fr.read()
        """z_scores = get_scores(text)
        svgData = plot(z_scores)
        return jsonify(file=svgData)"""
        fr.close()
        deleteFile(fileID)
        return jsonify(succMsg="Operation performed successfully")
        
    
@app.route('/userInput', methods=['POST'])
def userInput():
    text =  request.form['userInput']
    print(text)
    """z_scores = get_scores(text)
    svgData = plot(z_scores)
    return jsonify(file=svgData)"""
    return jsonify(succMsg="Operation performed successfully")

@app.route('/sendEmail', methods=['POST'])
def sendEmail():
    username =  request.form['username']
    email =  request.form['email']
    message =  request.form['message']
    try:
        sendMessage(username, email, message)
        return jsonify(succMsg="Operation performed successfully")
    except:
        return jsonify(
            errMsg="An error occurred while sending the message"
        )

def generateRandomID():
    fileID = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(32))
    return fileID

def deleteFile(fileName):
    if(os.path.isfile("temp/"+fileName+".txt")):
        os.remove("temp/"+fileName+".txt")

if __name__=="__main__":
    app.run()
