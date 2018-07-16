import numpy
from numpy.random import choice


probs = numpy.random.dirichlet(alpha=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10), size=None)
conditions_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

draw = choice(a=conditions_list, p=probs)

print(draw)
