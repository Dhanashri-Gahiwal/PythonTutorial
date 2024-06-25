# random module
import random

# randint() = returns the random value between 2 to 5 (both included)
print(random.randint(2,5))

# randrange() = returns the random value between 2 to 5 (only 2 included, 5 not included)
print(random.randrange(2,5))

# choice() = returns random value in given list 
ch = [1,2,3]
print(random.choice(ch))

# random() = returns random float value between 0 to 1 range
print(random.random())

# uniform() = returns random float value between 2 to 4 range
print(random.uniform(2,4))

# shuffle() = returns random value in given list
sh = [10,20,30,40]
print(random.shuffle(sh))
