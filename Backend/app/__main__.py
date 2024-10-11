# __main__.py
from flask import Flask
from api.brokers.angelone import get_live_feed_blueprint



app = Flask(__name__)
app.register_blueprint(get_live_feed_blueprint)

if __name__ == '__main__':
    app.run(debug=True, port=1919, host="0.0.0.0")