import streamlit as st
import streamlit.components.v1 as components
import subprocess
import matplotlib.pyplot as plt
from scipy.io import wavfile
import IPython.display as ipd

x = 1.0

wavPath = "tts_out.wav"
defaultRate = 24000
st.set_page_config(layout="centered")
col1, col2 = st.columns([115,20])
with col1:
    st.title('Text-to-Speech with Coqui TTS')
with col2:
    st.image('Icon-Red_Hat-Volume_up-A-Black-RGB.png', width=95)


st.markdown("""<hr style="height:3px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)

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
    st.markdown(t)
    samplingFrequency, signalData = wavfile.read(wavPath)
    st.sidebar.markdown("## Output Speed")
    st.sidebar.markdown("You can **change** the audio samples per second to vary the *speed* of the audio.")

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

    plt.specgram(signalData[:120000], mode='psd',Fs=samplingFrequency, cmap = 'inferno')
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

with st.form('Form1'):
    input1 = st.text_input("Say Something")
    submit1 = st.form_submit_button('Submit')
    ttsoutput(input1)

with st.sidebar.form('Form2'):
    x = st.slider('Rate (24000 * x)', min_value=0.5, max_value=2.0, step=0.05, value=1.0, key=5)
    submit2 = st.form_submit_button('Submit')
    st.sidebar.write(f"rate={x*defaultRate*changeAudio()}")




