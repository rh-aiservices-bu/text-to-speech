import streamlit as st
import subprocess
import matplotlib.pyplot as plt
from scipy.io import wavfile
import IPython.display as ipd

x = 1.0
wavPath = "tts_out.wav"
defaultRate = 24000

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
    output = open(wavPath, "rb")
    st.text(t)
    samplingFrequency, signalData = wavfile.read(wavPath)

    st.audio(output)
    fig,ax = plt.subplots()
    plt.style.use('classic')

    plt.subplot(211)
    plt.title('Wave Spectogram')

    plt.plot(signalData[:120000], color='black')
    plt.xlabel('')
    plt.ylabel('Volume')
    plt.xlim((-2000,122000))


    plt.subplot(212)

    plt.specgram(signalData[:120000], mode='psd',Fs=samplingFrequency, cmap = 'magma')
    plt.xlabel('Time')
    plt.ylabel('Hz')
    st.pyplot(fig)
    #plot.show()
    #userAudio = ipd.Audio(signalData, rate=x*24000)
    return

def changeAudio():
    if not x==1.0:
        samplingFrequency, signalData = wavfile.read(wavPath)
        newRate = int(x*defaultRate)
        wavfile.write('userOut.wav', newRate, signalData)
        userOutput = open('userOut.wav', "rb")
        st.sidebar.audio(userOutput)

    return 1

x = st.sidebar.slider('Rate', min_value=0.5, max_value=2.0, step=0.05, value=1.0, key=5)
st.sidebar.write(f"rate={x*defaultRate*changeAudio()}")
st.sidebar.markdown("## Controls")
st.sidebar.markdown("You can **change** the values to change the *chart*.")


ttsoutput(st.text_input("Say Something"))

