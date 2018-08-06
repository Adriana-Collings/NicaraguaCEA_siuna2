import SimParameters as P
from SimPy import EconEvalClasses as ce
import numpy as np

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

# summary statistics for condition A
print('Summary Stats Condition A OS Cost', simulation.get_sumStat_con_a_OS_cost().get_mean())
print('95% Confidence Interval for Condition A OS Cost', simulation.get_sumStat_con_a_OS_cost().get_t_CI(alpha))
print('Summary Stats Condition A NoOS Cost', simulation.get_sumStat_con_a_NoOS_cost().get_mean())
print('95% Confidence Interval for Condition A NoOS Cost', simulation.get_sumStat_con_a_NoOS_cost().get_t_CI(alpha))
print('Summary Stats Condition A OS Utilities', simulation.get_sumStat_con_a_OS_utilities().get_mean())
print('95% Confidence Interval for Condition A OS Utilities', simulation.get_sumStat_con_a_OS_utilities().get_t_CI(alpha))
print('Summary Stats Condition A NoOS Utilities', simulation.get_sumStat_con_a_NoOS_utilities().get_mean())
print('95% Confidence Interval for Condition A NoOS Utilities', simulation.get_sumStat_con_a_NoOS_utilities().get_t_CI(alpha))
print(" ")

# summary statistics for condition B
print('Summary Stats Condition B OS Cost', simulation.get_sumStat_con_b_OS_cost().get_mean())
print('Summary Stats Condition B NoOS Cost', simulation.get_sumStat_con_b_NoOS_cost().get_mean())
print('Summary Stats Condition B OS Utilities', simulation.get_sumStat_con_b_OS_utilities().get_mean())
print('Summary Stats Condition B NoOS Utilities', simulation.get_sumStat_con_b_NoOS_utilities().get_mean())
print (" ")

# summary statistics for condition C
print('Summary Stats Condition C OS Cost', simulation.get_sumStat_con_c_OS_cost().get_mean())
print('Summary Stats Condition C NoOS Cost', simulation.get_sumStat_con_c_NoOS_cost().get_mean())
print('Summary Stats Condition C OS Utilities', simulation.get_sumStat_con_c_OS_utilities().get_mean())
print('Summary Stats Condition C NoOS Utilities', simulation.get_sumStat_con_c_NoOS_utilities().get_mean())

# CEA plot
# currently turning out weird but hopefully will have more of a 'cloud' when we randomize the simulation parameters
s1 = ce.Strategy('OpSmile', cost_obs=simulation.get_OS_costs(), effect_obs=simulation.get_OS_utilities())
s2 = ce.Strategy('No OpSmile', cost_obs=simulation.get_NoOS_costs(), effect_obs=simulation.get_NoOS_utilities())
myCEA = ce.CEA([s1, s2], if_paired=False) # double check to see if this is paired or not
myCEA.show_CE_plane('CE Plane with cost vs utilities', x_label='Cost', y_label='Utilities',
                   show_legend=True, show_clouds=True, figure_size=6)

# ICER table
print('')
# return none and write result into csv
#print(myCEA.build_CE_table(ce.Interval.PREDICTION))
#print(myCEA.build_CE_table())

