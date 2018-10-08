from flask import Flask
from flask import request
app = Flask(__name__)


@app.route('/<endpoint>', methods=['GET', 'POST'])
def server(endpoint):
    if request.method == 'POST':
        print(endpoint)
        for header in request.headers:
            print(header)
        print(request.data)
        return "{'status':200, 'message':'success'}"
    else:
        print(endpoint)
        return request.method

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
