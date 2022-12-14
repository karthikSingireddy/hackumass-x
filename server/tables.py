from flask import Flask, render_template, jsonify
import json
from datetime import datetime
import time
from flask_cors import CORS
tables = Flask(__name__)
CORS(tables)

class DiningHall:

    def __init__(self, data):
        self.name = "Undefined"
        self.data = data
        self.tables = []
        self.convertData()
    
    def convertData(self):
        self.name = self.data["Name"]
        for i in self.data["Tables"]:
            self.tables.append(Table(i))
    
    def updateTable(self, num):
        self.tables[num].changeOccupancy()
        self.tables[num].setTime(datetime.now().strftime("%H:%M:%S"))

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
        self.startTime = "00:00:00"
        self.data = data
        self.convertData()
    
    def changeOccupancy(self):
        self.taken = not (self.taken)

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
        
@tables.route('/worcester')
def Worcester():
  return jsonify(DiningHall(json.load(open('worcester.json'))).serialize())

@tables.route('/berk')
def Berkshire():
    return jsonify(DiningHall(json.load(open('berkshire.json'))).serialize())
    
@tables.route('/frank')
def Franklin():
    return jsonify(DiningHall(json.load(open('franklin.json'))).serialize())

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

