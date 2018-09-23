from flask import Flask
from flask import request
app = Flask(__name__)


@app.route('/home', methods=['GET', 'POST'])
def server():
    if request.method == 'POST':
        print(request.data)
        for header in request.headers:
            print(header)
        return request.data
    else:
        return request.method

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
