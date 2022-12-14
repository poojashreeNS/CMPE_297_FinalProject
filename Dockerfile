FROM docker.io/library/python:3.8.9@sha256:49d05fff9cb3b185b15ffd92d8e6bd61c20aa916133dca2e3dbe0215270faf53

RUN pip install --no-cache-dir pip==22.0.2 && pip install --no-cache-dir datasets huggingface-hub "protobuf<4" "click<8.1"
WORKDIR /home/user/app
RUN pip install --no-cache-dir streamlit==1.15.2 gradio==2.9.0.1

COPY requirements.txt /home/user/app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

RUN useradd -m -u 1000 user

COPY packages.txt /root/packages.txt

RUN apt-get update && xargs -r -a /root/packages.txt apt-get install -y && rm -rf /var/lib/apt/lists/*

RUN apt-get update && apt-get install -y 	git 	git-lfs 	ffmpeg 	libsm6 	libxext6 	cmake 	libgl1-mesa-glx 	&& rm -rf /var/lib/apt/lists/* 	&& git lfs install

COPY --chown=user --from=lfs /app /home/user/app
COPY --chown=user ./ /home/user/