import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackContext, filters
from queue import Queue

# 通过环境变量获取你的 Bot 令牌
TOKEN = os.environ.get('BOT_TOKEN')

# 通过环境变量获取要监控的频道 ID
SOURCE_CHANNEL_IDS = os.environ.get('SOURCE_CHANNEL_IDS').split(',') if os.environ.get('SOURCE_CHANNEL_IDS') else []

# 通过环境变量获取要转发到的频道 ID
DESTINATION_CHANNEL_IDS = os.environ.get('DESTINATION_CHANNEL_IDS').split(',') if os.environ.get('DESTINATION_CHANNEL_IDS') else []

# 设置要筛选的关键词
KEYWORDS = os.environ.get('KEYWORDS', '').split(',') if os.environ.get('KEYWORDS') else []

# 处理 /start 命令的函数
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Bot 已启动，开始监控频道！')

# 处理新消息的函数
def echo(update: Update, context: CallbackContext) -> None:
    message = update.message
    # 如果关键词列表为空，转发所有监控的消息
    if not KEYWORDS:
        if message.chat.username in SOURCE_CHANNEL_IDS:
            for dest_channel_id in DESTINATION_CHANNEL_IDS:
                context.bot.forward_message(chat_id=dest_channel_id, from_chat_id=message.chat_id, message_id=message.message_id)
    # 否则，检查消息文本是否包含关键词
    elif any(keyword in message.text for keyword in KEYWORDS):
        # 如果消息来自监控的频道，就转发到指定的频道
        if message.chat.username in SOURCE_CHANNEL_IDS:
            for dest_channel_id in DESTINATION_CHANNEL_IDS:
                context.bot.forward_message(chat_id=dest_channel_id, from_chat_id=message.chat_id, message_id=message.message_id)

def main() -> None:
    # 创建 Bot 对象
    bot = Bot(token=TOKEN)
    updater = Updater(bot=bot, update_queue=Queue())

    # 获取调度器和调度处理程序
    dispatcher = updater.dispatcher

    # 添加命令处理程序
    dispatcher.add_handler(CommandHandler("start", start))

    # 添加消息处理程序
    dispatcher.add_handler(MessageHandler(filters.TEXT & ~filters.command, echo))

    # 启动 Bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
