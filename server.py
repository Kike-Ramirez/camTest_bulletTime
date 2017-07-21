from flask import Flask, request


app = Flask(__name__)


@app.route('/start', methods=['POST'])
def start():
    # print(request.form['foo']) # should display 'bar'
    print 'start'
    return 'Received !' # response to your request.


@app.route('/stop', methods=['POST'])
def stop():
    # print(request.form['foo']) # should display 'bar'
    print 'stop'
    return 'Received !' # response to your request.

app.run(host= '127.0.0.1', port= '8000')