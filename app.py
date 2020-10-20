import os
from flask import Flask
from environs import Env

app = Flask(__name__)

env = Env()
env.read_env()
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