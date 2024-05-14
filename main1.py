#!/usr/local/bin/python

from dotenv import load_dotenv
from telethon import TelegramClient, events
import os

# 指定容器内部的 .env 文件路径
dotenv_path = '/app/.env'
load_dotenv(dotenv_path=dotenv_path)

# 从环境变量中获取api_id和api_hash
api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')

# 从环境变量中获取电话号码
phone_number = os.getenv('PHONE_NUMBER')

# 创建Telegram客户端实例
client = TelegramClient(phone_number, api_id, api_hash)

# 从环境变量中获取要监听的频道ID列表
source_channel_ids = os.getenv('SOURCE_CHANNEL_IDS', '').split(',')

# 从环境变量中获取要转发消息的频道ID列表
destination_channel_ids = os.getenv('DESTINATION_CHANNEL_IDS', '').split(',')

# 您想要监听的关键词列表，如果为空则转发所有消息
keywords = os.getenv('KEYWORDS', '').split(',')

@client.on(events.NewMessage(chats=source_channel_ids))
async def handler(event):
    # 如果关键词列表为空，或者消息包含关键词，则转发消息
    if not keywords or any(keyword.lower() in event.raw_text.lower() for keyword in keywords):
        # 遍历目标频道ID列表，将消息转发到每个频道
        for destination_channel_id in destination_channel_ids:
            await event.message.forward_to(destination_channel_id)

def main():
    # 连接到Telegram
    client.start(phone=phone_number)
    print('正在监听...')
    client.run_until_disconnected()

if __name__ == '__main__':
    main()
