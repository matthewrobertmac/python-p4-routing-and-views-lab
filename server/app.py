#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run(port=5555, debug=True)

@app.route('/')
def index():
  return <h1>Python Operations with Flask Routing and Views</h1>

@app.route('/print/parameter')
def print_string(str):
  print(str)
  return <h1>{len(str)}</h1>

@app.route('/count/parameter')
def count(int):
  for i in range(int):
    return \ni

@app.route('/math/<num1>/<operation>/<num2>')



