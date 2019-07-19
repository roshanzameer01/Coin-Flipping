#coin flipping game
import random

i = 0
heads = 1
tales = 0
print("Welcome to the Coin Flipping game!")
print("0 = Tales", "1 = Heads")
print()

while(i <= 10):
	print(random.randint(tales, heads))
	i += 1

print("Number of heads:", heads)
print("Number of tales:", tales)
