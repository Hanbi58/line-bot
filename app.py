from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('zCe0ioRrh3MBa8AOrdRVqzyAm8UIURnv0zjHBJru3KZJm8D+MurRMlyXwOQCGZRZgJxrT32ICuehuXLmIgsHQoSRaX5YZ/23a+1TY9v0evxi2xMsW1cOIcvm9Ur2N1BEIKASnrJDrzfwu6Ypx9IIVwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('7a5f60df3f3987d1595da5e40326db82')


@app.route("/callback", methods=['POST'])  #route是路径  比如我们的网址是www.line-bot.com 那么有人访问网站的时候
#就会用www.line-bot.com/callback 来敲门， 那么我们的代码看到callback 就会执行下面的代码
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)  #handle这个function会触发下面那个handle_message
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):  #这个地方的功能就是 回复信息
    # msg=event.message.text
    msg='How are you doing today?'
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=(msg))


if __name__ == "__main__":  #python常见 需要这一行来判定是否执行以上代码 如果没有这一行 比人import就app.run
    app.run()   #这行意思就是 架设服务器