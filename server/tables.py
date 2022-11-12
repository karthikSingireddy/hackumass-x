from flask import Flask

tables = Flask(__name__)

class DiningHall:
    def __init__(self, name, tables):
        self.name = name
        self.tables = tables


class Table:
    def __init__(self, tableNumber, diningHall):
        self.tableNumber = tableNumber
        self.diningHall = diningHall
        self.taken = False

worc = DiningHall("Worcester", 20)

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