# Fw-tgbot
telegram自动监听并转发的机器人
安装运行
docker run -d --name Fw-tgbot \
    -e BOT_TOKEN=YOUR_BOT_TOKEN \
    -e SOURCE_CHANNEL_IDS=@channel1,@channel2,@channel3 \
    -e DESTINATION_CHANNEL_IDS=@destination_channel1,@destination_channel2 \
    -e KEYWORDS="keyword1,keyword2,keyword3" \
    yourusername/mytelegrambot:latest
