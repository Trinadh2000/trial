# angelone.py
import time
import threading

####from flask import Blueprint, jsonify

#from fyers_apiv3.FyersWebsocket import data_ws
#from fyers_apiv3 import fyersModel
from app.api.brokers import config

# Replace the sample access token with your actual access token obtained from Fyers
access_token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJhcGkuZnllcnMuaW4iLCJpYXQiOjE3MjY4MDU5OTIsImV4cCI6MTcyNjg3ODY1MiwibmJmIjoxNzI2ODA1OTkyLCJhdWQiOlsieDowIiwieDoxIiwieDoyIiwiZDoxIiwiZDoyIiwieDoxIiwieDowIl0sInN1YiI6ImFjY2Vzc190b2tlbiIsImF0X2hhc2giOiJnQUFBQUFCbTdQZm9EZUhncFlZUi1yWnppRzFQWnAwc0JvdW5XekJCSUdqU1k3MVZBZDRYcmtkVXZJdk00MlhGTC11dElGeHRpZzctQVo2RlZxVGs0b0p0N3ZoRUhSSl9lLXBqd296bUZoYm8yYVZTVWJiMV92az0iLCJkaXNwbGF5X25hbWUiOiJTQUkgR0FORVNIIEtBTlVQQVJUSEkiLCJvbXMiOiJLMSIsImhzbV9rZXkiOiIwYTgzNjI0ZmEwYjA1ZmViODJmNDBlMDdiY2Y3MmYxYWEwMGY1ODFhMTIxOTNkNWM3Y2ZlZTI2YiIsImZ5X2lkIjoiWVMxNzE5NSIsImFwcFR5cGUiOjEwMCwicG9hX2ZsYWciOiJOIn0.tw5a6UvmFzuJeuf569Z3EXZPBzpLA7JMkUBvYXNDs6c',

def retrieve_fyers_live_feed(access_token):
    def onmessage(message):
        config.LIVE_FEED_JSON[message['symbol']] = message

    def onerror(message):
        print("Error:", message)

    def onclose(message):
        print("Connection closed:", message)

    def onopen():
        data_type = "SymbolUpdate"
        symbols = ["NSE:NIFTY50-INDEX", "NSE:NIFTYBANK-INDEX", "NSE:FINNIFTY-INDEX", "BSE:SENSEX-INDEX"]
        fyers.subscribe(symbols=symbols, data_type=data_type)
        fyers.keep_running()

    fyers = data_ws.FyersDataSocket(
        access_token=access_token,
        log_path="",
        litemode=False,
        write_to_file=False,
        reconnect=True,
        on_connect=onopen,
        on_close=onclose,
        on_error=onerror,
        on_message=onmessage
    )

    threading.Thread(target=fyers.connect).start()

def print_fyers_live_feed():
    while True:
        print('LIVE_FEED_JSON:', config.LIVE_FEED_JSON)
        time.sleep(2)

get_live_feed_blueprint = Blueprint('get_live_feed', __name__)

@get_live_feed_blueprint.route('/get_live_feed', methods=['GET'])
def get_live_feed():
    return jsonify(config.LIVE_FEED_JSON)