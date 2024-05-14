# 使用官方Python镜像作为基础镜像
FROM python:3.8-slim

# 设置工作目录
WORKDIR /app

# 将脚本复制到容器中
COPY . /app

# 安装python-telegram-bot库
RUN pip install python-telegram-bot telethon
RUN pip install python-dotenv

# 运行脚本
CMD ["python", "./main1.py"]
