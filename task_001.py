import math

pi = math.pi
print(pi)

num = input()
n = str.split(num, '.')
long = len(n[1])
pi = round(pi, long)
print(pi)
