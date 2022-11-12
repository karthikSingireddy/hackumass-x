from flask import Flask, render_template, jsonify
##import RPi.GPIO as GPIO
##import SimpleMFRC522

tables = Flask(__name__)

class Observerable:

    def _init_(self):
        self.observers = []

    def notify(self, modifier = None):
        for observer in self.observers:
            if modifier != observer:
                observer.update(self)

    def attach(self, observer):
        if observer not in self.observers:
            self.observers.append(observer)
    
    def detach(self, observer):
        try:
            self.observers.remove(observer)
        except ValueError:
            pass

class DiningHall:
    def __init__(self, name, tables):
        self.name = name
        self.tables = tables
    
    def serializeTables(self):
        output = []
        for i in range(20):
            output.append(self.tables[i].serialize())
        return output
    
    def serialize(self):
        return {
            'Name': self.name,
            'Tables': self.serializeTables()
        }


class Table:
    def __init__(self, tableNumber, diningHall, x, y, height, width):
        self.tableNumber = tableNumber
        self.diningHall = diningHall
        self.taken = False
        self.x = x
        self.y = y
        self.height = height
        self.width = width
    
    def occupy(self):
        self.taken = True

    def unoccupy(self):
        self.taken = False
    
    def serialize(self):
        return {
            'Number': self.tableNumber,
            'Hall': self.diningHall,
            'x': self.x,
            'y': self.y,
            'Width': self.width,
            'Height': self.height
        }


def genTables(num, name):
    tables = []
    for i in range(num):
        tables.append(Table(i, name, 0, 0, 0, 0))
    return tables

worc = DiningHall("Worcester", genTables(20, 'Worcester'))
berk = DiningHall("Berkshire", genTables(20, 'Berkshire'))
frank = DiningHall("Franklin", genTables(20, 'Franklin'))
hamp = DiningHall("Hampshire", genTables(20, 'Hampshire'))

tables = Flask(__name__)
@tables.route('/')
def index():
  return {
        'Worcester-Dining': worc.serialize(),
        'Berk-Dining': berk.serialize(),
        'Frank-Dining': frank.serialize(),
        'Hamp-Dining': hamp.serialize()
  }

tables.run()