#!flask/bin/python
import os
import sys
from flask import Flask, render_template, request

app = Flask(__name__)
sys.path.append(os.getcwd() + "/src/")

@app.route('/')
def output():
    # serve index template
    return render_template('index.html')


if __name__ == '__main__':
    # run!
    from waitress import serve
    port = int(os.environ.get('PORT', 9000))
    serve(app, host="0.0.0.0", port=port)
    # app.run(host='0.0.0.0', threaded=True, port=port)
