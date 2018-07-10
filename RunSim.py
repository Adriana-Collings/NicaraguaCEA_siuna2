import SimParameters as P

year1 = P.YearofPatients(id=1)
simulation=year1.simulate()

print(simulation.get_costs_utilities())
