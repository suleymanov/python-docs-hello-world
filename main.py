from flask import Flask
from pymongo import MongoClient


app = Flask(__name__)


@app.route('/')
def hello_world():
  return 'Hello, World!'


if __name__ == '__main__':
  app.run()
