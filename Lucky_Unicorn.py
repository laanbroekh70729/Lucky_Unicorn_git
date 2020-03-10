# get input



# ask user for name
name = input ("What is your name")

# ask user for two numbers
num_1 = int(input("What is your favourite number? "))
num_2 = int(input("What is your second favourite number? "))

# add numbers together
add = num_1 + num_2

# multiply numbers together

# greet user and display match
print ('Hello',name)

print (" {} + {} = {}".format (num_1, num_2, add ))

#ask user how much money the user would like to play with, min $1 or max $5
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

balance=intcheck("How much money would you like to play with? (Whole dollars between $1 or $5)",(1, 10)
