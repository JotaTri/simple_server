from flask import Flask
from flask import request
from flask import jsonify
app = Flask(__name__)
import json

@app.route('/<endpoint>', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def server(endpoint=None):
    if request.method == 'POST':
        print('Endpoint - /' + (str(endpoint) if endpoint else ''))
        print('Headers:')
        for header in request.headers:
            print(header)
        print('Body:')
        print(request.data.decode('utf-8'))
        return jsonify({'status':200, 'message':'success'})
    else:
        print(endpoint)
        return request.method

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000, debug=True)
