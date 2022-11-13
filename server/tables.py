from flask import Flask, render_template, jsonify
import json
from datetime import datetime
import time

tables = Flask(__name__)

def validateCard(num):
    return str(num)[0:8] == "21206600"

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
            'Number': self.tableNumber,
            'x': self.x,
            'y': self.y,
            'Width': self.width,
            'Height': self.height,
            'Taken': self.taken,
            'Time': self.startTime
        }

worc = open('worcester.json')
berk = open('berkshire.json')
frank = open('franklin.json')
hamp = open('hampshire.json')
jsonArr = [json.load(worc), json.load(berk), json.load(frank), json.load(hamp)] 
worc = DiningHall(jsonArr[0])
berk = DiningHall(jsonArr[1])
frank = DiningHall(jsonArr[2])
hamp = DiningHall(jsonArr[3])

'''
curFileSeek = 0
while curFileSeek <= 16:
    inFile = open('./cardData', 'r')
    inFile.seek(curFileSeek)
    cardNum = int(inFile.readline())
    if (validateCard(cardNum)):
        worc.updateTable(cardNum % 20)
    curFileSeek = inFile.tell()
    inFile.close()
'''

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