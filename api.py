import json
from flask import Flask, request, jsonify
from flask_cors import CORS
from grpc import server

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def index():
    return '不要亂看啦>///<'

@app.route('/api', methods=['GET'])
def api():

    date = []
    count = []

    f = open('form.diff', 'r' )
    for line in f.readlines():
        data = line.split("|")
        if data[0] not in date:
            if "#" not in data[0]:
                date.append(data[0])
            else:
                if "來亂的人" in date:
                    continue
                else:
                    date.append("來亂的人")
    f.close()
    date.pop(0)
    date.sort()
    count = [0]*len(date)

    f = open('form.diff', 'r')
    for line in f.readlines():
        data = line.split("|")
        if "日期" not in data[0]:
            if "#" in data[0]:
                key = date.index("來亂的人")
                count[key] += 1
            else:
                key = date.index(data[0])
                count[key] += 1
    api = dict(zip(date,count))
    api = {"jsonarray":[api]}
    return jsonify(api)

@app.route('/txt', methods=['GET'])
def txt():
    data = ""
    with open('form.diff', 'r' ) as f:
        data = f.read()
    # f = open('form.diff', 'r' )
    # for line in f.readlines():
        
    #     data += line
        
    # f.close()
    # print(data)
    return data

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)