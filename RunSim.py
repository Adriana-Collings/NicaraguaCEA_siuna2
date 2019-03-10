import SimParameters as P
from SimPy import EconEvalClasses as ce
import numpy as np

np.random.seed(1)

# run simulation of patients
year1 = P.YearofPatients(id=1)
simulation = year1.simulate()

alpha=0.05

# summary statistics for all conditions
print('Summary Stats OS Cost', simulation.get_sumStat_OS_cost().get_mean())
print('95% Confidence Interval for OS Cost', simulation.get_sumStat_OS_cost().get_t_CI(alpha))
print('Summary Stats No OS Cost', simulation.get_sumStat_NoOS_cost().get_mean())
print('95% Confidence Interval for No OS Cost', simulation.get_sumStat_NoOS_cost().get_t_CI(alpha))
print('Summary Stats OS Utility', simulation.get_sumStat_OS_utility().get_mean())
print('95% Confidence Interval for OS Utility', simulation.get_sumStat_OS_utility().get_t_CI(alpha))
print('Summary Stats No OS Utility', simulation.get_sumStat_NoOS_utility().get_mean())
print('95% Confidence Interval for No OS Utility', simulation.get_sumStat_NoOS_utility().get_t_CI(alpha))
print(" ")

print (" ")

# CEA plot
s1 = ce.Strategy('Intervention', cost_obs=simulation.get_OS_costs(), effect_obs=simulation.get_OS_utilities())
s2 = ce.Strategy('No Intervention', cost_obs=simulation.get_NoOS_costs(), effect_obs=simulation.get_NoOS_utilities())
myCEA = ce.CEA([s2, s1], if_paired=False)
myCEA.show_CE_plane('CE Plane with Cost vs Utilities, Siuna', x_label='Utilities', y_label='Cost',
                   show_legend=True, show_clouds=True, figure_size=6)

# ICER table
print('')
# return none and write result into csv
print(myCEA.build_CE_table(ce.Interval.PREDICTION))
print(myCEA.build_CE_table())

