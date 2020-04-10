from flask import Flask, request
import telegram
import os

TOKEN = os.environ['TOKEN']
bot = telegram.Bot(token=TOKEN)

app = Flask(__name__)


@app.route('/{}'.format(TOKEN), methods=['POST'])
def respond():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    chat_id = update.message.chat.id
    msg_id = update.message.message_id
    text = update.message.text.encode('utf-8').decode()
    bot.sendMessage(chat_id=chat_id, text="Hi there!", reply_to_message_id=msg_id)
    return TOKEN


if __name__ == '__main__':
    app.run(threaded=True)
