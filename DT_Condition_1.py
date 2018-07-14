import DT as DT
import InputData_Condition1 as D

# dictionary for decision nodes
#               // key: cost, utility, [future nodes]
dictDecisions_OS = {'d1': [5, 5, ['OpSmile', 'toss']]}
dictDecisions_NoOS = {'d2': [5, 5, ['NoOS', 'toss2']]}

#           // key: cost, utility, [future nodes], [probabilities]
dictChances_OS = {
    'OpSmile': [D.OpSmile_C, D.OpSmile_U, ['Access', 'NoAccess'], [D.PR_OS_Access, (1-D.PR_OS_Access)]],
    'Access': [D.OS_Access_C, D.OS_Access_U, ['Surgery', 'NoSurgery'],
                          [D.PR_OS_A_Surgery, (1-D.PR_OS_A_Surgery)]],
    'Surgery': [D.OS_A_Surgery_C, D.OS_A_Surgery_U, ['OS_S_Die', 'OS_S_Survive'],
                [D.PR_OS_S_Die, (1-D.PR_OS_S_Die)]],
    'OS_S_Survive': [D.OS_A_S_Survive_C, D.OS_A_S_Survive_U, ['OS_S_S_Comp', 'OS_S_S_NoComp'],
                     [D.PR_OS_S_S_Comp, (1-D.PR_OS_S_S_Comp)]],
    'OS_S_S_Comp': [D.OS_A_S_S_Comp_C, D.OS_A_S_S_Comp_U, ['OS_S_S_C_Major', 'OS_S_S_C_Minor'],
                    [D.PR_OS_S_S_C_Major, (1-D.PR_OS_S_S_C_Major)]],
    'OS_S_S_C_Major': [D.OS_A_S_S_C_Major_C, D.OS_A_S_S_C_Major_U, ['OS_S_S_C_Major_Die', 'OS_S_S_C_Major_Survive'],
                       [D.PR_OS_S_S_C_Major_Die, (1-D.PR_OS_S_S_C_Major_Die)]],
    'NoSurgery': [D.OS_A_NoSurgery_C, D.OS_A_NoSurgery_U, ['NoSurgery_Die', 'NoSurgery_Survive'],
                  [D.PR_OS_A_NoSurgery_Die, (1-D.PR_OS_A_NoSurgery_Die)]],
    'NoAccess': [D.OS_NoAccess_C, D.OS_NoAccess_U, ['OS_Managua', 'OS_Disease'],
                 [D.PR_OS_Managua, (1-D.PR_OS_Managua)]],
    'OS_Managua': [D.OS_NA_Managua_C, D.OS_NA_Managua_U, ['OS_Managua_Die', 'OS_Managua_Survive'],
                [D.PR_OS_Managua_Die, (1-D.PR_OS_Managua_Die)]],
    'OS_Managua_Survive': [D.OS_NA_M_Survive_C, D.OS_NA_M_Survive_U, ['OS_M_S_Comp', 'OS_M_S_NoComp'],
                          [D.PR_OS_M_S_Comp, (1-D.PR_OS_M_S_Comp)]],
    'OS_M_S_Comp': [D.OS_NA_M_S_Comp_C, D.OS_NA_M_S_Comp_U, ['OS_M_S_C_Major', 'OS_M_S_C_Minor'],
                    [D.PR_OS_M_S_C_Major, (1-D.PR_OS_M_S_C_Major)]],
    'OS_M_S_C_Major': [D.OS_NA_M_S_C_Major_C, D.OS_NA_M_S_C_Major_U, ['OS_M_S_C_Major_Die', 'OS_M_S_C_Major_Survive'],
                       [D.PR_OS_M_S_C_Major_Die, (1-D.PR_OS_M_S_C_Major_Die)]],
    'OS_Disease': [D.OS_NA_Disease_C, D.OS_NA_Disease_U, ['OS_Disease_Survive', 'OS_Disease_Die'],
                   [D.PR_OS_Disease_Die, (1-D.PR_OS_Disease_Die)]]}
dictChances_NoOS = {
    # no opsmile
    'NoOS': [D.NoOS_C, D.NoOS_U, ['NoOS_Access', 'NoOS_NoAccess'], [D.PR_NoOS_Access, (1-D.PR_NoOS_Access)]],
    'NoOS_Access': [D.NoOS_Access_C, D.NoOS_Access_U, ['NoOS_A_Surgery', 'NoOS_A_NoSurgery'],
                          [D.PR_NoOS_A_Surgery, (1-D.PR_NoOS_A_Surgery)]],
    'NoOS_A_Surgery': [D.NoOS_A_Surgery_C, D.NoOS_A_Surgery_U, ['NoOS_S_Die', 'NoOS_A_S_Survive'],
                [D.PR_NoOS_S_Die, (1-D.PR_NoOS_S_Die)]],
    'NoOS_A_S_Survive': [D.NoOS_A_S_Survive_C, D.NoOS_A_S_Survive_U, ['NoOS_A_S_S_Comp', 'NoOS_S_S_NoComp'],
                     [D.PR_NoOS_S_S_Comp, (1-D.PR_NoOS_S_S_Comp)]],
    'NoOS_A_S_S_Comp': [D.NoOS_A_S_S_Comp_C, D.NoOS_A_S_S_Comp_U, ['NoOS_A_S_S_C_Major', 'NoOS_S_S_C_Minor'],
                    [D.PR_NoOS_S_S_C_Major, (1-D.PR_NoOS_S_S_C_Major)]],
    'NoOS_A_S_S_C_Major': [D.NoOS_A_S_S_C_Major_C, D.NoOS_A_S_S_C_Major_U, ['NoOS_S_S_C_Major_Die', 'NoOS_S_S_C_Major_Survive'],
                       [D.PR_NoOS_S_S_C_M_Die, (1-D.PR_NoOS_S_S_C_M_Die)]],
    'NoOS_A_NoSurgery': [D.NoOS_A_NoSurgery_C, D.NoOS_A_NoSurgery_U, ['NoOS_NoSurgery_Die', 'NoOS_NoSurgery_Survive'],
                  [D.PR_NoOS_NS_Die, (1-D.PR_NoOS_NS_Die)]],  # likely a dominated strategy
    'NoOS_NoAccess': [D.NoOS_NoAccess_C, D.NoOS_NoAccess_U, ['NoOS_NA_Managua', 'NoOS_NA_Disease'],
                 [D.PR_NoOS_NA_Managua, (1-D.PR_NoOS_NA_Managua)]],
    'NoOS_NA_Managua': [D.NoOS_NA_Managua_C, D.NoOS_NA_Managua_U, ['NoOS_Managua_Die', 'NoOS_NA_M_Survive'],
                [D.PR_NoOS_NA_M_Die, (1-D.PR_NoOS_NA_M_Die)]],
    'NoOS_NA_M_Survive': [D.NoOS_NA_M_Survive_C, D.NoOS_NA_M_Survive_U, ['NoOS_NA_M_S_Comp', 'NoOS_M_S_NoComp'],
                          [D.PR_NoOS_NA_M_Comp, (1-D.PR_NoOS_NA_M_Comp)]],
    'NoOS_NA_M_S_Comp': [D.NoOS_NA_M_S_Comp_C, D.NoOS_NA_M_S_Comp_C, ['NoOS_NA_M_S_C_Major', 'NoOS_M_S_C_Minor'],
                    [D.PR_NoOS_NA_M_Comp_Major, (1-D.PR_NoOS_NA_M_Comp_Major)]],
    'NoOS_NA_M_S_C_Major': [D.NoOS_NA_M_S_C_Major_C, D.NoOS_NA_M_S_C_Major_U, ['NoOS_M_S_C_Major_Die', 'NoOS_M_S_C_Major_Survive'],
                       [D.PR_NoOS_NA_M_C_M_Die, (1-D.PR_NoOS_NA_M_C_M_Die)]],
    'NoOS_NA_Disease': [D.NoOS_NA_Disease_C, D.NoOS_NA_Disease_U, ['NoOS_Disease_Survive', 'NoOS_Disease_Die'],
                   [D.PR_NoOS_NA_D_Die, (1-D.PR_NoOS_NA_D_Die)]]
}

# dictionary for terminal nodes
#               //key:                  cost,                               utility
dictTerminal_OS = {
    'OS_S_Die': [D.OS_S_Die_C, D.OS_S_Die_U],
    'OS_S_S_NoComp': [D.OS_S_S_NoComp_C, D.OS_S_S_NoComp_U],
    'OS_S_S_C_Minor': [D.OS_S_S_Minor_C, D.OS_S_S_Minor_U],
    'OS_S_S_C_Major_Die': [D.OS_S_S_C_Major_Die_C, D.OS_S_S_C_Major_Die_U],
    'OS_S_S_C_Major_Survive': [D.OS_S_S_C_Major_Survive_C, D.OS_S_S_C_Major_Survive_U],
    'NoSurgery_Die': [D.OS_NoSurgery_Die_C, D.OS_NoSurgery_Die_U],
    'NoSurgery_Survive': [D.OS_NoSurgery_Survive_C, D.OS_NoSurgery_Survive_U],
    'OS_Managua_Die': [D.OS_Managua_Die_C, D.OS_Managua_Die_U],
    'OS_M_S_NoComp': [D.OS_M_S_NoComp_C, D.OS_M_S_NoComp_U],
    'OS_M_S_C_Minor': [D.OS_M_S_C_Minor_C, D.OS_M_S_C_Minor_U],
    'OS_M_S_C_Major_Die': [D.OS_M_S_C_Major_Die_C, D.OS_M_S_C_Major_Die_U],
    'OS_M_S_C_Major_Survive': [D.OS_M_S_C_Major_Survive_C, D.OS_M_S_C_Major_Survive_U],
    'OS_Disease_Die': [D.OS_Disease_Die_C, D.OS_Disease_Die_U],
    'OS_Disease_Survive': [D.OS_Disease_Survive_C, D.OS_Disease_Survive_U]}
dictTerminal_NoOS = {
    # NoOpSmile
    'NoOS_S_Die': [D.NoOS_S_Die_C, D.NoOS_S_Die_U],
    'NoOS_S_S_NoComp': [D.NoOS_S_S_NoComp_C, D.NoOS_S_S_NoComp_U],
    'NoOS_S_S_C_Minor': [D.NoOS_S_S_Minor_C, D.NoOS_S_S_Minor_U],
    'NoOS_S_S_C_Major_Die': [D.NoOS_S_S_C_Major_Die_C, D.NoOS_S_S_C_Major_Die_U],
    'NoOS_S_S_C_Major_Survive': [D.NoOS_S_S_C_Major_Survive_C, D.NoOS_S_S_C_Major_Survive_U],
    'NoOS_NoSurgery_Die': [D.NoOS_NoSurgery_Die_C, D.NoOS_NoSurgery_Die_U],
    'NoOS_NoSurgery_Survive': [D.NoOS_NoSurgery_Survive_C, D.NoOS_NoSurgery_Survive_U],
    'NoOS_Managua_Die': [D.NoOS_Managua_Die_C, D.NoOS_Managua_Die_U],
    'NoOS_M_S_NoComp': [D.NoOS_M_S_NoComp_C, D.NoOS_M_S_NoComp_U],
    'NoOS_M_S_C_Minor': [D.NoOS_M_S_C_Minor_C, D.NoOS_M_S_C_Minor_U],
    'NoOS_M_S_C_Major_Die': [D.NoOS_M_S_C_Major_Die_C, D.NoOS_M_S_C_Major_Die_U],
    'NoOS_M_S_C_Major_Survive': [D.NoOS_M_S_C_Major_Survive_C, D.NoOS_M_S_C_Major_Survive_U],
    'NoOS_Disease_Die': [D.NoOS_Disease_Die_C, D.NoOS_Disease_Die_U],
    'NoOS_Disease_Survive': [D.NoOS_Disease_Survive_C, D.NoOS_Disease_Survive_U]
}

# CREATING DECISION NODE
#tree_OS = DT.DecisionNode('d1', dict_decisions=dictDecisions_OS, cum_prob=1, dict_chances=dictChances_OS, dict_terminals=dictTerminal_OS)

#print(tree_OS.get_cost_utility())
#print(tree_OS.get_terminal_prob())
#print(tree_OS.get_OS_cost())
#print(tree_OS.get_OS_utility())

#tree_NoOS = DT.DecisionNode('d2', dict_decisions=dictDecisions_NoOS, cum_prob=1, dict_chances=dictChances_NoOS, dict_terminals=dictTerminal_NoOS)
#print(tree_NoOS.get_cost_utility())
#print(tree_NoOS.get_terminal_prob())
#print(tree_NoOS.get_NoOS_cost())
#print(tree_NoOS.get_NoOS_utility())





