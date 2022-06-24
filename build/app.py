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
            "--out_path",
            "tts_out.wav"
        ]
    )
    output = open("tts_out.wav", "rb")
    st.text(t)
    st.audio(output)
    return


ttsoutput(st.text_input("Say Something"))
