# run.py
import threading
from flask import Flask
from app.api.brokers.angelone import retrieve_fyers_live_feed, print_fyers_live_feed,access_token
#from fyers_apiv3.FyersWebsocket import data_ws
#from fyers_apiv3 import fyersModel


app = Flask(__name__)

if __name__ == '__main__':
    # Start threads for retrieving live feed and printing it.
    threading.Thread(target=retrieve_fyers_live_feed, args=(access_token,)).start()
    threading.Thread(target=print_fyers_live_feed).start()

    app.run(debug=True, port=1919, host="0.0.0.0")