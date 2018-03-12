from flask import Flask
from pymongo import MongoClient


app = Flask(__name__)
client = MongoClient('mongodb://macrodb:umQucbmm86HkVJSbq7JwBMbsalBn4nuX2WEO5cc171LyudHCAG4ixa1FeS00ssm4JO6V69dy850pP9qWrccpnA==@macrodb.documents.azure.com:10255/?ssl=true&replicaSet=globaldb')


@app.route('/')
def hello_world():
  return 'Hello, World!'


if __name__ == '__main__':
  app.run()
