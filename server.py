import socket
import pymongo
import json

HOST = '0.0.0.0'
PORT = 5000

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']
coll = db['events']

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by, adder')
        while True:
            data = conn.recv(1024)
            print(data)
            coll.insert_one(json.loads(data))