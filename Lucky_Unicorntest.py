import random

# **** Main Routine Starts Here ****

# Instructions/Introduction

print()
print("Welcome")
print()
print("How this game works")
print()
print("- Each round counts $1")
print ("- Each round you have a chance to win some of your money back or more than you payed for each round")
print()
print("- For each round, you get a token which is worth an amount of money")
print()
print("Tokens: Donkey ($0), Horse or Zebra ($2) or an Unicorn ($5)")


tokens = ["horse", "zebra", "donkey", "unicorn"]
for item in range(1, 10):

  picked = random.choice(tokens)
  print(picked)




