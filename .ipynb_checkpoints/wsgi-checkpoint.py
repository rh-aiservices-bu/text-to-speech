import json
from flask import Flask, jsonify, request
import subprocess
import base64

def ttsoutput(textinput):
    t= textinput['data']
    subprocess.run(['tts', "--text", "\"" + t + "\"", '--model_name',"tts_models/en/ljspeech/glow-tts", '--vocoder_name', "vocoder_models/universal/libri-tts/fullband-melgan"])
    output = open('tts_output.wav', 'rb')
    encoded_output = base64.b64encode(output.read())  # bytes
    return encoded_output
application = Flask(__name__)


@application.route('/')
@application.route('/status')
def status():
    return jsonify({'status': 'ok'})


@application.route('/speech', methods=['POST'])
def speech_generation():
    data = request.data or '{}'
    body = json.loads(data)
    return ttsoutput(body)
