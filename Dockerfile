FROM python:3.10-slim

WORKDIR /workspace

# 環境変数でタイムゾーンを事前設定
ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=Asia/Tokyo

# タイムゾーンを設定
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# システム依存パッケージのインストール（-y オプションと組み合わせて非対話的にインストール）
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    git \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Pythonパッケージのインストール
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# プロジェクト構造の作成
RUN mkdir -p /workspace/src /workspace/notebooks /workspace/data /workspace/models

# 作業ディレクトリの設定
WORKDIR /workspace

# JupyterLabとFlaskのポートを開放
EXPOSE 8888 5000