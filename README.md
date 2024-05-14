# Fw-tgbot
自用telegram自动监听并转发的机器人\
安装运行命令，测试
```
docker run -d --name Fw-tgbot \
    -e BOT_TOKEN=YOUR_BOT_TOKEN \
    -e SOURCE_CHANNEL_IDS=@channel1,@channel2,@channel3 \
    -e DESTINATION_CHANNEL_IDS=@destination_channel1,@destination_channel2 \
    -e KEYWORDS="keyword1,keyword2,keyword3" \
    zz22ff/fw-tgbot:latest
```
```
docker run -d --name Fw-tgbot \
-e API_ID='your_api_id' \
-e API_HASH='your_api_hash' \
-e SOURCE_CHANNEL_IDS='channel_id1,channel_id2' \
-e DESTINATION_CHANNEL_IDS='destination_id1,destination_id2' \
-e KEYWORDS='关键词1,关键词2' \
zz22ff/fw-tgbot:latest
```
