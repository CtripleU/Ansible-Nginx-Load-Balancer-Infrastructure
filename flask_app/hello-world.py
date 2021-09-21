from flask import Flask, render_template
import requests
import json
import socket

app = Flask(__name__)


@app.route('/', method=['GET'])
def index():
    req = requests.get('https://animechan.vercel.app/api/random')
    data = json.loads(req.content)
    return render_template('index.html', data=data)

if __name__ == '__main__':
            app.run(debug = True, host='0.0.0.0', port='5000')
