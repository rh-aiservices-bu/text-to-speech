FROM quay.io/thoth-station/ps-cv-pytorch:v0.1.2 
USER 0 
RUN dnf -y install libsndfile 
USER 1001 
RUN pip install tts==0.6.0
RUN git clone https://github.com/rh-aiservices-bu/text-to-speech.git
