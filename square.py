import random
lst=[random.randint(-15,15) for i in range(11)]
a=map(lambda a:a**2,lst)
print(list(a))


output:
[25, 225, 25, 9, 36, 196, 1, 36, 1, 121, 196]
