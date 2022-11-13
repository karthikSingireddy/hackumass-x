import json
from datetime import datetime
import time
import math

epoch_time = datetime(1970, 1, 1)

def validateCard(num):
    return str(num)[0:8] == "21206600"

while True:
  num = input("Scan your card: ")
  if validateCard(num):
    print("You are from UMass!")
    diningHall = input("Enter the dining hall [worcester, berkshire, hampshire, franklin]: ")
    tableNum = int(input("Enter your table number: "))
    occupying = input("If you are vacating the table enter 1. If you are occupying the table enter 2: ") == "2"
    with open(diningHall + ".json", "r") as jsonFile:
        data = json.load(jsonFile)
    data["Tables"][tableNum]["Taken"] = occupying
    if occupying:
        data["Tables"][tableNum]["Time"] = math.floor((datetime.now() - epoch_time).total_seconds() * (10**3))
    else:
        data["Tables"][tableNum]["Time"] = 0
    with open(diningHall + ".json", "w") as jsonFile:
        json.dump(data, jsonFile)
  else:
    print("You are not from UMass!")