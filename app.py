from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import pandas as pd
import numpy as np
import random

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

def initialize_randomness():
    for i in range(1,31):
        if(i < 10):
            filename = '2020-08-0'+str(i)+'.bin'
        else:
            filename = '2020-08-'+str(i)+'.bin'
        with open(filename, 'rb') as f:
            while(byte := f.read(1)):
                randombytes.append(byte)
                
randombytes = []
initialize_randomness()
sampleSize = len(randombytes)

@app.route('/integer', methods=['GET'])
@cross_origin()
def integer():
    n = request.args.get('n')
    m = request.args.get('m')
    if(n == None):
        n = 1
    else:
        n = int(n)
    if(m == None):
        m = 255
    else:
        m = int(m)
    integers = []
    for i in range(n):
        byte = randombytes[random.randint(0,sampleSize)]
        byte = ord(byte)
        byte = bin(byte)[2:].rjust(8,'0')
        integer = int(byte,2) 
        while(integer >= m):
            byte = randombytes[random.randint(0,sampleSize)]
            byte = ord(byte)
            byte = bin(byte)[2:].rjust(8,'0')
            integer = int(byte,2) 
        integers.append(integer)
    return jsonify(integers)

@app.route('/bit', methods=['GET'])
@cross_origin()
def bit():
    n = request.args.get('n')
    if(n == None):
        n = 1
    else:
        n = int(n)
    bits = []
    for i in range(n):
        byte = randombytes[random.randint(0,sampleSize)]
        byte = ord(byte)
        byte = bin(byte)[2:].rjust(8,'0')
        bits.append(int(byte[0]))
    return jsonify(bits)

# A welcome message to test our server
@app.route('/')
@cross_origin()
def index():
    return "<h1>Welcome to the Randomness API!</h1>"

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
