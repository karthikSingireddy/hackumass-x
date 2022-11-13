from flask import Flask, render_template, jsonify
import json
from datetime import datetime
import time
from flask_cors import CORS
tables = Flask(__name__)
CORS(tables)

class DiningHall:

    def __init__(self, json):
        self.name = "Undefined"
        self.json = json
        self.tables = []
        self.convertData()
    
    def convertData(self):
        self.name = self.json["Name"]
        for i in self.json["Tables"]:
            self.tables.append(Table(i))

    def serializeTables(self):
        output = []
        for i in range(len(self.tables)):
            output.append(self.tables[i].serialize())
        return output
    
    def serialize(self):
        return {
            'name': self.name,
            'tables': self.serializeTables()
        }

class Table:  

    def __init__(self, data):
        self.tableNumber = 0
        self.taken = False
        self.x = 0
        self.y = 0
        self.height = 0
        self.width = 0
        self.startTime = "00:00"
        self.data = data
        self.convertData()
    
    def occupy(self):
        self.taken = True

    def unoccupy(self):
        self.taken = False

    def setTime(self, time):
        self.startTime = time

    def convertData(self):
        self.tableNumber = self.data["Number"]
        self.taken = self.data["Taken"]
        self.x = self.data["x"]
        self.y = self.data["y"]
        self.width = self.data["Width"]
        self.height = self.data["Height"]
        self.startTime = self.data["Time"]
 
    def serialize(self):
        return {
            'number': self.tableNumber,
            'x': self.x,
            'y': self.y,
            'width': self.width,
            'height': self.height,
            'taken': self.taken,
            'time': self.startTime
        }

woo = open('worcester.json')
berk = open('berkshire.json')
frank = open('franklin.json')
hamp = open('hampshire.json')
jsonArr = [json.load(woo), json.load(berk), json.load(frank), json.load(hamp)] 
worc = DiningHall(jsonArr[0])
berk = DiningHall(jsonArr[1])
frank = DiningHall(jsonArr[2])
hamp = DiningHall(jsonArr[3])

curFileSeek = 0
# while True:
    # print
    # inFile = open('./cardData', 'r')
    # inFile.seek(curFileSeek)
    # data = inFile.read()
    # curFileSeek = inFile.tell()
    # inFile.close()
    # time.sleep(10)


@tables.route('/worcester')
def Worcester():
  response = jsonify(DiningHall(json.load(open('worcester.json'))).serialize())
  return response

@tables.route('/berk')
def Berkshire():
    response = jsonify(DiningHall(json.load(open('berkshire.json'))).serialize())
    return response

@tables.route('/frank')
def Franklin():
    response = jsonify(DiningHall(json.load(open('franklin.json'))).serialize())
    return response

@tables.route('/hamp')
def Hampshire():
    response = jsonify(DiningHall(json.load(open('hampshire.json'))).serialize())
    return response

@tables.route('/<loc>/<int:table>')
def update(loc, table):
    dh = None
    if loc == 'worcester':
        dh = worc
    elif loc == 'hamp':
        dh = hamp
    elif loc == 'frank':
        dh = frank
    elif loc == 'berk':
        dh = berk
    else:
        return 'Failed'
    
    for x in dh.tables:
        if x.tableNumber == table:
            x.taken = True
            return 'Success'

tables.run()