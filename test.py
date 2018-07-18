import numpy
from numpy.random import choice

probs = numpy.random.dirichlet(alpha=(1, 1), size=None)  # dirichlet distribution: the numbers of alpha
# determine the concentration of the probability for each option
conditions_list = ['a', 'b']

draw = choice(a=conditions_list, p=probs)

print(probs, draw)