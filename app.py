from flask import Flask, request
import telegram
import os
import json
import logging

# Enable Logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

global TOKEN 
TOKEN = '1135698268:AAEipBbNjrsXeTQwjhf8M9TzJL0ADHAvFho'
# TOKEN = os.environ['TOKEN']
global bot 
bot = telegram.Bot(token=TOKEN)



app = Flask(__name__)


@app.route('/{}'.format(TOKEN), methods=['POST'])
def respond():
    logger.debug("From: %s\nchat_id: %d\nText: %s" %
                (update.message.from_user,
                update.message.chat_id,
                update.message.text))

    update = telegram.Update.de_json(request.get_json(force=True), bot)

    chat_id = update.message.chat.id
    msg_id = update.message.message_id

    print("chat_id:", chat_id)
    

    # Telegram understands UTF-8, so encode text for unicode compatibility
    # mssg = update.message.text.encode('utf-8').decode()

    # msg = update.message.text.encode('utf-8').decode()
    bot.sendMessage(chat_id=chat_id, text="msg")

    return 'ok'


@app.route('/', methods=['POST'])
def index():
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 


if __name__ == '__main__':
    app.run(threaded=True)