import random as r
num = r.random()
print(num)

numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

print(r.choice(numbers))

print(r.randrange(100))

print(r.random())

r.seed(5)

print(r.random())
