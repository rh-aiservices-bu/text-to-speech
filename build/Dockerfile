FROM quay.io/thoth-station/ps-cv-pytorch:v0.1.2 
USER 0 
RUN dnf -y install libsndfile 
USER 1001 
COPY build/requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
RUN git clone https://github.com/rh-aiservices-bu/text-to-speech.git
RUN pip list > piplist.txt

# #FROM python:3.10.4

# WORKDIR /app

# COPY app/requirements.txt ./requirements.txt

# RUN pip install -r requirements.txt

# RUN pip list > piplist.txt

# # override default port (from 8501 to 8080)
ENV STREAMLIT_SERVER_PORT=8080
# # these variables might be needed for the right info (logging) to show up in the log
ENV PYTHONUNBUFFERED=1
# ENV PYTHONIOENCODING=UTF-8

EXPOSE 8080

COPY ./build .

ENTRYPOINT ["streamlit", "run"]

CMD ["app.py"]

