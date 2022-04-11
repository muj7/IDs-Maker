import random as rand

def makeID():
  numbers = "1234568790"
  Letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

  All = numbers + Letter

  len = 16

  ID = "".join(rand.sample(All, len))
  print(ID)

i = 0

while i < 35:
  makeID()
  i += 1