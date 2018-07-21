import SimParameters as P
from SimPy import EconEvalClasses as ce
import numpy as np

year1 = P.YearofPatients(id=1)
simulation = year1.simulate()


#print('Expected Op Smile Costs', simulation.get_OS_costs())
#print('Expected No Op Smile Costs', simulation.get_NoOS_costs())
#print('Expected Op Smile Utilites', simulation.get_OS_utilities())
#print('Expected No Op Smile Utilities', simulation.get_NoOS_utilities())
#print('Expected DALY', simulation.get_DALY())

print('Summary Stats OS Cost', simulation.get_sumStat_OS_cost().get_mean())
print('Summary Stats No OS Cost', simulation.get_sumStat_NoOS_cost().get_mean())
print('Summary Stats OS Utility', simulation.get_sumStat_OS_utility().get_mean())
print('Summary Stats No OS Utility', simulation.get_sumStat_NoOS_utility().get_mean())
print('Summary Stats DALY', simulation.get_sumStat_DALY().get_mean())
print(" ")


print('Summary Stats Condition A OS Cost', simulation.get_sumStat_con_a_OS_cost().get_mean())
print('Summary Stats Condition A NoOS Cost', simulation.get_sumStat_con_a_NoOS_cost().get_mean())
print('Summary Stats Condition A OS Utilities', simulation.get_sumStat_con_a_OS_utilities().get_mean())
print('Summary Stats Condition A NoOS Utilities', simulation.get_sumStat_con_a_NoOS_utilities().get_mean())
print('Summary Stats Condition A DALY', simulation.get_sumStat_con_a_DALY().get_mean())
print(" ")

print('Summary Stats Condition B OS Cost', simulation.get_sumStat_con_b_OS_cost().get_mean())
print('Summary Stats Condition B NoOS Cost', simulation.get_sumStat_con_b_NoOS_cost().get_mean())
print('Summary Stats Condition B OS Utilities', simulation.get_sumStat_con_b_OS_utilities().get_mean())
print('Summary Stats Condition B NoOS Utilities', simulation.get_sumStat_con_b_NoOS_utilities().get_mean())
print('Summary Stats Condition B DALY', simulation.get_sumStat_con_b_DALY().get_mean())

# currently turning out weird but hopefully will have more of a 'cloud' when we randomize the simulation parameters
s1 = ce.Strategy('OpSmile', cost_obs=simulation.get_OS_costs(), effect_obs=simulation.get_OS_utilities())
s2 = ce.Strategy('No OpSmile', cost_obs=simulation.get_NoOS_costs(), effect_obs=simulation.get_NoOS_utilities())

# alternate
s3 = ce.Strategy('OpSmile', cost_obs=simulation.get_OS_costs(), effect_obs=simulation.get_DALY())
s4 = ce.Strategy('No OpSmile', cost_obs=simulation.get_NoOS_costs(), effect_obs=simulation.get_DALY())

myCEA = ce.CEA([s1, s2], if_paired=False) # double check to see if this is paired or not

# plot with sample cloud and legend
myCEA.show_CE_plane('CE Plane with cost vs utilities', x_label='Cost', y_label='Utilities',
                    show_legend=True, show_clouds=True, figure_size=6)

myCEAb = ce.CEA ([s3, s4], if_paired=False)

myCEAb.show_CE_plane('CE Plane with cost vs DALYs',x_label='Cost', y_label='DALYs',
                    show_legend=True, show_clouds=True, figure_size=6)
