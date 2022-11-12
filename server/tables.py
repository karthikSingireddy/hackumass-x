from flask import Flask, render_template
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


def genTables(num, name):
    tables = []
    for i in range(num):
        tables.append(Table(i, name, 0, 0, 0, 0))
    return tables

worc = DiningHall("Worcester", genTables(20, 'Worcester'))
berk = DiningHall("Berkshire", genTables(20, 'Berkshire'))
frank = DiningHall("Franklin", genTables(20, 'Franklin'))
hamp = DiningHall("Hampshire", genTables(20, 'Hampshire'))

app = Flask(__name__)

@app.route('/')
def index():
  return hamp.name

app.run()

"""
@tables.route('/woo')
def worcStatus():
  return 

@tables.route('/berk')
def berkStatus():
    return

@tables.route('/frank')
def frankStatus():
    return

@tables.route('/hamp')
def hampStatus():
    return

tables.run()
"""