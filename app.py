from flask import Flask, request
import telegram
import os
import json
import logging

global TOKEN 
TOKEN = '1135698268:AAEipBbNjrsXeTQwjhf8M9TzJL0ADHAvFho'
# TOKEN = os.environ['TOKEN']
global bot 
bot = telegram.Bot(token=TOKEN)



app = Flask(__name__)


@app.route('/{}'.format(TOKEN), methods=['POST'])
def respond():
    print('enter respond fun')
    update = telegram.Update.de_json(request.get_json(force=True), bot)

    chat_id = update.message.chat.id
    msg_id = update.message.message_id

    # Telegram understands UTF-8, so encode text for unicode compatibility
    # mssg = update.message.text.encode('utf-8').decode()

    # msg = update.message.text.encode('utf-8').decode()
    bot.sendMessage(chat_id=chat_id, text="msg")

    return 'ok'


@app.route('/', methods=['POST'])
def index():
    print('logss')
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 


if __name__ == '__main__':
    app.run(threaded=True)