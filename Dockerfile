# 基于 Python 的官方镜像构建
FROM python:3.9-slim

# 设置工作目录
WORKDIR /app

# 复制项目文件到工作目录
COPY . .

# 安装项目依赖
RUN pip install --no-cache-dir python-telegram-bot

# 运行主程序
CMD ["python", "main.py"]
