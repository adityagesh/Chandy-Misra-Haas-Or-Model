from python:3.7-slim
RUN mkdir /deadlock-detection
COPY . /deadlock-detection
WORKDIR /deadlock-detection
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "run.py"]