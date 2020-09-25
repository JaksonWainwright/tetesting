from flask import Flask

app = Flask(__name__)

@app.route('/test')
def simulate_test():
    return 'asdf'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
