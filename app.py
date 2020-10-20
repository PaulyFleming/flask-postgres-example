import os
from flask import Flask

app = Flask(__name__)
development = os.environ.get('DEVELOPMENT')


@app.route('/')
def hello():
    print(f"Develoment environment = {development}", flush=True)
    return "Hello World!"

@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)



if __name__ == '__main__':
    app.run()