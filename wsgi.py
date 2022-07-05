import json
from flask import Flask, render_template, jsonify, request
import subprocess
import base64

def ttsoutput(textinput):
    t= textinput['data']
    subprocess.run(
        [
            "tts",
            "--text",
            '"' + t + '"',
            "--model_name",
            "tts_models/en/ljspeech/glow-tts",
            "--vocoder_name",
            "vocoder_models/universal/libri-tts/fullband-melgan",
            "--out_path",
            "output/tts_output.wav"
        ])
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
    if request.data:
        data = request.data
    else:
        data = request.form['data'] or '{}'
    body = json.loads(data)
    print('done')
    return ttsoutput(body)

