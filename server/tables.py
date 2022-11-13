from flask import Flask, render_template, jsonify
import json
from datetime import datetime
import time

tables = Flask(__name__)

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
            'Name': self.name,
            'Tables': self.serializeTables()
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
            'Number': self.tableNumber,
            'x': self.x,
            'y': self.y,
            'Width': self.width,
            'Height': self.height,
            'Taken': self.taken,
            'Time': self.startTime
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
while True:
    print
    inFile = open('./cardData', 'r')
    inFile.seek(curFileSeek)
    data = inFile.read()
    curFileSeek = inFile.tell()
    inFile.close()
    time.sleep(10)


@tables.route('/Worcester')
def Worcester():
  return worc.serialize()

@tables.route('/Berkshire')
def Berkshire():
    return berk.serialize()

@tables.route('/Franklin')
def Franklin():
    return frank.serialize()

@tables.route('/Hampshire')
def Hampshire():
    return hamp.serialize()
tables.run()