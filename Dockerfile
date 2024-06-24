# Based on the code on https://www.pybootcamp.com/blog/how-to-write-dockerfile-python-apps/
# Thanks!
#
# In the future docker-ci-run.py may be more functional.
FROM python:3.8.3-slim-buster

ENV TINI_VERSION="v0.19.0"

ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /tini
RUN chmod +x /tini

# STYLE YOUR DOCKERFILE LIKE A PRO
RUN pip install -U \
    pip \
    setuptools \
    wheel

WORKDIR /project

RUN useradd -m -r user && \
    chown user /project

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

USER user

ARG GIT_HASH
ENV GIT_HASH=${GIT_HASH:-dev}

ENTRYPOINT ["/tini", "--"]
