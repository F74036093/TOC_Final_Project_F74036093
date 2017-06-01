import sys
from io import BytesIO

import telegram
from flask import Flask, request, send_file

from fsm import TocMachine


API_TOKEN = '356912122:AAEB1o1VxZvL13rDg6GOC-jp_pQHfn8I_N8'
WEBHOOK_URL = 'https://5f190cb0.ngrok.io/hook'

app = Flask(__name__)
bot = telegram.Bot(token=API_TOKEN)
machine = TocMachine(
    states=[
        'user',
        #'state1',
        #'state2'
        'ready',
        'watch_monster',
        'watch_dog',
        'watch_bird',
        'monster_sad',
        'monster_happy',
        'dog_shibe',
        'dog_beagle',
        'bird_seagull'
    ],
    transitions=[
        #{
        #    'trigger': 'advance',
        #    'source': 'user',
        #    'dest': 'state1',
        #    'conditions': 'is_going_to_state1'
        #},
        #{
        #    'trigger': 'advance',
        #    'source': 'user',
        #    'dest': 'state2',
        #    'conditions': 'is_going_to_state2'
        #},
        #{
        #    'trigger': 'go_back',
        #    'source': [
        #        'state1',
        #        'state2'
        #    ],
        #    'dest': 'user'
        #}
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'ready',
            'conditions': 'is_going_to_ready'
        },
        {
            'trigger': 'advance',
            'source': 'ready',
            'dest': 'watch_monster',
            'conditions': 'is_going_to_watch_monster'
        },
        {
            'trigger': 'advance',
            'source': 'ready',
            'dest': 'watch_dog',
            'conditions': 'is_going_to_watch_dog'
        },
        {
            'trigger': 'advance',
            'source': 'ready',
            'dest': 'watch_bird',
            'conditions': 'is_going_to_watch_bird'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'watch_monster',
            'conditions': 'is_going_to_watch_monster'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'watch_dog',
            'conditions': 'is_going_to_watch_dog'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'watch_bird',
            'conditions': 'is_going_to_watch_bird'
        },
        {
            'trigger': 'advance',
            'source': 'watch_monster',
            'dest': 'monster_sad',
            'conditions': 'is_going_to_monster_sad'
        },
        {
            'trigger': 'advance',
            'source': 'watch_monster',
            'dest': 'monster_happy',
            'conditions': 'is_going_to_monster_happy'
        },
        {
            'trigger': 'advance',
            'source': 'watch_dog',
            'dest': 'dog_shibe',
            'conditions': 'is_going_to_dog_shibe'
        },
        {
            'trigger': 'advance',
            'source': 'watch_dog',
            'dest': 'dog_beagle',
            'conditions': 'is_going_to_dog_beagle'
        },
        {
            'trigger': 'advance',
            'source': 'watch_bird',
            'dest': 'bird_seagull',
            'conditions': 'is_going_to_bird_seagull'
        },
        {
            'trigger': 'advance',
            'source': [
                'watch_monster',
                'watch_dog',
                'watch_bird'
            ],
            'dest': 'user',
            'conditions': 'is_going_to_user'
        },
        {
            'trigger': 'go_back',
            'source': [
                #'watch_monster',
                #'watch_bird'
                'monster_sad',
                'monster_happy',
                'dog_shibe',
                'dog_beagle',
                'bird_seagull'
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
