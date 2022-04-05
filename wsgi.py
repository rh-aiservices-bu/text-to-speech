import json
from flask import Flask, jsonify, request
import subprocess

def ttsoutput(textinput):
    t= textinput['data']
    subprocess.run(['tts', "--text", "\"" + t + "\"", '--model_name',"tts_models/en/ljspeech/glow-tts", '--vocoder_name', "vocoder_models/universal/libri-tts/fullband-melgan"])
    return 'tts_output.wav'
application = Flask(__name__)


@application.route('/')
@application.route('/status')
def status():
    return jsonify({'status': 'ok'})


@application.route('/speech', methods=['POST'])
def speech_generation():
    data = request.data or '{}'
    body = json.loads(data)
    return jsonify(ttsoutput(body))
