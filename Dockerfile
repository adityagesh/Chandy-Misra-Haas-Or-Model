from python:3.7-slim
RUN mkdir /deadlock-detection
COPY requirements.txt /deadlock-detection
WORKDIR /deadlock-detection
RUN pip install -r requirements.txt
COPY . /deadlock-detection
ENTRYPOINT ["python", "run.py"]