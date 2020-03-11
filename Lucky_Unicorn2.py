# Generate random token


import random

tokens = ["horse", "zebra", "donkey", "unicorn"]
for item in range(1, 15):

  picked = random.choice(tokens)
  print(picked)

