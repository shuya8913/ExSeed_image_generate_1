FROM python:3.10

WORKDIR /root/dev/src

RUN apt update -qq && \
    apt install -y build-essential \
    git \
    curl \
    wget \
    vim \
    systemctl \
    nginx \
    lsof \
    psmisc

ENV PYTHONUNBUFFERED 1
# 環境変数を設定してキャッシュディレクトリを変更
ENV HF_HOME=/root/dev/data/cache

COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt