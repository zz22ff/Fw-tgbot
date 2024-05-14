import os
from telethon import TelegramClient, events

# 从环境变量中获取api_id和api_hash
api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')

# 创建Telegram客户端实例
client = TelegramClient('session_name', api_id, api_hash)

# 要监听的频道或群组
listen_channel_or_group = 'ChannelOrGroupName'

# 要转发消息的频道或群组
forward_to_channel_or_group = 'ForwardChannelOrGroupName'

# 您想要监听的关键词列表，如果为空则转发所有消息
keywords = os.getenv('KEYWORDS', '').split(',')

@client.on(events.NewMessage(chats=listen_channel_or_group))
async def handler(event):
    # 如果关键词列表为空，或者消息包含关键词，则转发消息
    if not keywords or any(keyword.lower() in event.raw_text.lower() for keyword in keywords):
        # 将消息转发到指定的频道或群组
        await event.message.forward_to(forward_to_channel_or_group)

def main():
    # 连接到Telegram
    client.start()
    print('正在监听...')
    client.run_until_disconnected()

if __name__ == '__main__':
    main()
