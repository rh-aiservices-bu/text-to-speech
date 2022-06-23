import streamlit as st
import subprocess


def ttsoutput(textinput):
    t = textinput
    subprocess.run(
        [
            "tts",
            "--text",
            '"' + t + '"',
            "--model_name",
            "tts_models/en/ljspeech/glow-tts",
            "--vocoder_name",
            "vocoder_models/universal/libri-tts/fullband-melgan",
        ]
    )
    output = open("text-to-speech/tts_output.wav", "rb")
    st.text(t)
    st.audio(output)
    return


ttsoutput(st.text_input("Say Something"))
