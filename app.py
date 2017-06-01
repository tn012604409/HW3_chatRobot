import sys
from io import BytesIO

import telegram
from flask import Flask, request, send_file

from fsm import TocMachine


API_TOKEN = '337410858:AAFL4ulEbOuHUoP5KrIO42IE4FWqBryanc4'
WEBHOOK_URL = 'https://524e11bb.ngrok.io/hook'

app = Flask(__name__)
bot = telegram.Bot(token=API_TOKEN)
machine = TocMachine(
     states=[
        'user',
        'menu',
        'chinese',
        'fry',
        'spring',
        'yam',
        'saute',
        'beef',
        'egg',
        'Italy',
        'spaghetti',
        'tomato',
        'butter',
        'stew',
        'wine',
        'sea',
        'Thiland',
        'squid',
        'thaiNoodle',
        'USA',
        'chicken',
        'Ham',
        'order',
    ],
    transitions=[
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'menu',
            'conditions': 'is_going_to_menu'
        },
        {
            'trigger': 'advance',
            'source': 'menu',
            'dest': 'order',
            'conditions': 'is_going_to_order'
        },
        {
            'trigger': 'advance',
            'source': 'menu',
            'dest': 'chinese',
            'conditions': 'is_going_to_chinese'
        },
        {
            'trigger': 'advance',
            'source': 'chinese',
            'dest': 'fry',
            'conditions': 'is_going_to_fry'
        },
        {
            'trigger': 'advance',
            'source': 'fry',
            'dest': 'spring',
            'conditions': 'is_going_to_spring'
        },
        {
            'trigger': 'advance',
            'source': 'fry',
            'dest': 'yam',
            'conditions': 'is_going_to_yam'
        },
        {
            'trigger': 'advance',
            'source': 'chinese',
            'dest': 'saute',
            'conditions': 'is_going_to_saute'
        },
        {
            'trigger': 'advance',
            'source': 'saute',
            'dest': 'beef',
            'conditions': 'is_going_to_beef'
        },
        {
            'trigger': 'advance',
            'source': 'saute',
            'dest': 'egg',
            'conditions': 'is_going_to_egg'
        },
        {
            'trigger': 'advance',
            'source': 'menu',
            'dest': 'Italy',
            'conditions': 'is_going_to_Italy'
        },
        {
            'trigger': 'advance',
            'source': 'Italy',
            'dest': 'spaghetti',
            'conditions': 'is_going_to_spaghetti'
        },
        {
            'trigger': 'advance',
            'source': 'Italy',
            'dest': 'stew',
            'conditions': 'is_going_to_stew'
        },
        {
            'trigger': 'advance',
            'source': 'spaghetti',
            'dest': 'tomato',
            'conditions': 'is_going_to_tomato'
        },
        {
            'trigger': 'advance',
            'source': 'spaghetti',
            'dest': 'butter',
            'conditions': 'is_going_to_butter'
        },
        {
            'trigger': 'advance',
            'source': 'stew',
            'dest': 'wine',
            'conditions': 'is_going_to_wine'
        },
        {
            'trigger': 'advance',
            'source': 'stew',
            'dest': 'sea',
            'conditions': 'is_going_to_sea'
        },
        {
            'trigger': 'advance',
            'source': 'menu',
            'dest': 'Thiland',
            'conditions': 'is_going_to_Thiland'
        },
        {
            'trigger': 'advance',
            'source': 'Thiland',
            'dest': 'squid',
            'conditions': 'is_going_to_squid'
        },
        {
            'trigger': 'advance',
            'source': 'Thiland',
            'dest': 'thaiNoodle',
            'conditions': 'is_going_to_thaiNoodle'
        },
        {
            'trigger': 'advance',
            'source': 'menu',
            'dest': 'USA',
            'conditions': 'is_going_to_USA'
        },
        {
            'trigger': 'advance',
            'source': 'USA',
            'dest': 'chicken',
            'conditions': 'is_going_to_chicken'
        },
        {
            'trigger': 'advance',
            'source': 'USA',
            'dest': 'Ham',
            'conditions': 'is_going_to_Ham'
        },

        {
            'trigger': 'go_back',
            'source': [
                'spring',
                'yam',
                'beef',
                'egg',
                'tomato',
                'butter',
                'wine',
                'sea',
                'squid',
                'thaiNoodle',
                'chicken',
                'Ham',
                'order',
            ],
            'dest': 'user'
        }
    ],
    initial='user',
    auto_transitions=False,
    show_conditions=True,
)


def _set_webhook():
    status = bot.set_webhook(WEBHOOK_URL)
    if not status:
        print('Webhook setup failed')
        sys.exit(1)
    else:
        print('Your webhook URL has been set to "{}"'.format(WEBHOOK_URL))


@app.route('/hook', methods=['POST'])
def webhook_handler():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    machine.advance(update)
    return 'ok'


@app.route('/show-fsm', methods=['GET'])
def show_fsm():
    byte_io = BytesIO()
    machine.graph.draw(byte_io, prog='dot', format='png')
    byte_io.seek(0)
    return send_file(byte_io, attachment_filename='fsm.png', mimetype='image/png')


if __name__ == "__main__":
    _set_webhook()
    app.run()
