import numpy as np
import pandas as pd
from scipy import stats
import random
import secrets
import pickle

truerandombytes = []
for i in range(1,31):
    if(i < 10):
        filename = '2020-08-0'+str(i)+'.bin'
    else:
        filename = '2020-08-'+str(i)+'.bin'
    with open(filename, 'rb') as f:
        while(byte := f.read(1)):
            byte = ord(byte)
            byte = bin(byte)[2:].rjust(8,'0')
            truerandombytes.append(byte)
    print(filename)

sampleSize = len(truerandombytes)

# for i in range(sampleSize):
#     byte = ''
#     for j in range(8):
#         byte += str(random.getrandbits(1))
#     pseudorandombytes.append(byte)
    
# for i in range(sampleSize):
#     byte = ''
#     for j in range(8):
#         byte += str(secrets.randbits(1))
#     securerandombytes.append(byte)

def analyze(unique_elements, counts_elements):
    total = counts_elements.sum()
    print("Sample Size:",str(int(total/1000000)),'million')
    for num in unique_elements:
        count = counts_elements[int(num)]
        print(num, str(int(count/total*100))+'%')

def truerandom():
    coin = []
    fourbinary = []
    dicesix = []
    dicetwenty = []
    print("True Random")
    for i in range(sampleSize):
        byte = truerandombytes[random.randint(0,sampleSize)]
        onebit = byte[0]
        threebit = byte[:3]
        fourbit = byte[:4]
        fivebit = byte[:5]
        dicesixnum = int(threebit,2)
        dicetwentynum = int(fivebit,2)
        if(dicesixnum < 6):
            dicesix.append(dicesixnum)
        if(dicetwentynum < 20):
            dicetwenty.append(dicetwentynum)
        coin.append(int(onebit))
        fourbinary.append(fourbit.count('1'))
    fourbinary = np.array(fourbinary)
    a, b = np.unique(fourbinary, return_counts=True)
    analyze(a,b)

    dicesix = np.array(dicesix)
    a, b = np.unique(dicesix, return_counts=True)
    analyze(a,b)

    coin = np.array(coin)
    a, b = np.unique(coin, return_counts=True)
    analyze(a,b)

    dicetwenty = np.array(dicetwenty)
    a, b = np.unique(dicetwenty, return_counts=True)
    analyze(a,b)

truerandom()