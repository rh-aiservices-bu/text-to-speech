import json
from flask import Flask, render_template, jsonify, request
import subprocess
import base64

def ttsoutput(textinput):
    t= textinput['data']
    subprocess.run(['tts', "--text", "\"" + t + "\"", '--model_name',"tts_models/en/ljspeech/glow-tts", '--vocoder_name', "vocoder_models/universal/libri-tts/fullband-melgan", '--out_path', "tts_out.wav"])
    output = open('tts_out.wav', 'rb')
    encoded_output = base64.b64encode(output.read())  # bytes
    return encoded_output
application = Flask(__name__)


@application.route('/')
def main():
    return render_template('home.html')

@application.route('/status')
def status():
    return jsonify({'status': 'ok'})


@application.route('/speech', methods=['POST'])
def speech_generation():
    data = request.form['data'] or '{}'
    body = json.loads(data)
    print('done')
    return ttsoutput(body)

if __name__ == '__main__':
    application.run(host='0.0.0.0', port=8080, debug=True)