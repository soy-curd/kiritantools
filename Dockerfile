# Dockerfile for NEUTRINO.
# fork from https://gist.github.com/lazykyama/2f2035626c30ed68b65c6d48b283219e
FROM nvcr.io/nvidia/cuda:10.0-cudnn7-runtime-ubuntu18.04
LABEL maintainer="soy-curd"

RUN apt update && \
    apt install -y python3 python3-pip curl unzip && \
    apt clean && \
    rm -rf /var/lib/apt/lists/*
RUN ln -s /usr/bin/python3 /usr/bin/python
RUN ln -s /usr/bin/pip3 /usr/bin/pip
RUN pip install numpy scipy

WORKDIR /opt
ENV FILE_NAME NEUTRINO-Online_v0.200.zip
ADD ${FILE_NAME} .
RUN unzip ${FILE_NAME}
RUN chmod +x ./NEUTRINO/Run.sh \
    ./NEUTRINO/bin/NEUTRINO ./NEUTRINO/bin/NSF_IO ./NEUTRINO/bin/WORLD ./NEUTRINO/bin/musicXMLtoLabel
RUN chmod +x ./NEUTRINO/NSF/Run.sh ./NEUTRINO/NSF/bin/currennt