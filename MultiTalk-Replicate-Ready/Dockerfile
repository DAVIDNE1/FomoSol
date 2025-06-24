
FROM nvidia/cuda:11.8.0-cudnn8-runtime-ubuntu20.04

WORKDIR /code

RUN apt-get update && apt-get install -y git ffmpeg libgl1-mesa-glx

COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

RUN mkdir -p weights

ENTRYPOINT ["python3", "predict.py"]
