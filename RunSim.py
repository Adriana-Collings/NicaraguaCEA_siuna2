import SimParameters as P

year1 = P.YearofPatients(id=1)
simulation=year1.simulate()

print('Expected Op Smile Costs', simulation.get_OS_costs())
print('Expected No Op Smile Costs', simulation.get_NoOS_costs())
print('Expected Op Smile Utilites', simulation.get_OS_utilities())
print('Expected No Op Smile Utilities', simulation.get_NoOS_utilities())
