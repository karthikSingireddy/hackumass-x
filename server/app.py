def validateCard(num):
    return str(num)[0:8] == "21206600"

while True:
  num = input("Scan your card: ")
  if validateCard(num):
    print("You are from UMass!")
  else:
    print("who tf r u b?")