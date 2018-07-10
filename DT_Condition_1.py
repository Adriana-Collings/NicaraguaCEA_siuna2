import DT as DT
import InputData_Condition1 as D

# dictionary for decision nodes
#               // key: cost, utility, [future nodes]
dictDecisions = {'d1': [5, 5, ['OpSmile', 'NoOS_OpSmile']]}

#           // key: cost, utility, [future nodes], [probabilities]
dictChances = {
    'OpSmile': [D.OpSmile_C, D.OpSmile_U, ['Access', 'NoAccess'], [D.PR_OS_Access, (1-D.PR_OS_Access)]],
    'Access': [D.OpSmileAccess_C, D.OpSmileAccess_U, ['Surgery', 'NoSurgery'],
                          [D.PR_OS_A_Surgery, (1-D.PR_OS_A_Surgery)]],
    'Surgery': [D.OpSmileSurgery_C, D.OpSmileSurgery_U, ['OS_S_Die', 'OS_S_Survive'],
                [D.PR_OS_S_Die, (1-D.PR_OS_S_Die)]],
    'OS_S_Survive': [D.OS_S_Survive_C, D.OS_S_Survive_U, ['OS_S_S_Comp', 'OS_S_S_NoComp'],
                     [D.PR_OS_S_S_Comp, (1-D.PR_OS_S_S_Comp)]],
    'OS_S_S_Comp': [D.OS_S_S_Comp_C, D.OS_S_S_Comp_U, ['OS_S_S_C_Major', 'OS_S_S_C_Minor'],
                    [D.PR_OS_S_S_C_Major, (1-D.PR_OS_S_S_C_Major)]],
    'OS_S_S_C_Major': [D.OS_S_S_C_Major_C, D.OS_S_S_C_Major_U, ['OS_S_S_C_Major_Die', 'OS_S_S_C_Major_Survive'],
                       [D.PR_OS_S_S_C_Major_Die, (1-D.PR_OS_S_S_C_Major_Die)]],
    'NoSurgery': [D.OpSmileAccess_NoSurgery_C, D.OpSmileAccess_NoSurgery_U, ['NoSurgery_Die', 'NoSurgery_Survive'],
                  [D.PR_OS_A_NoSurgery_Die, (1-D.PR_OS_A_NoSurgery_Die)]],
    'NoAccess': [D.OpSmileNoAccess_C, D.OpSmileNoAccess_U, ['OS_Managua', 'OS_Disease'],
                 [D.PR_OS_Managua, (1-D.PR_OS_Managua)]],
    'OS_Managua': [D.OpSmile_Managua_C, D.OpSmile_Managua_U, ['OS_Managua_Die', 'OS_Managua_Survive'],
                [D.PR_OS_Managua_Die, (1-D.PR_OS_Managua_Die)]],
    'OS_Managua_Survive': [D.OS_Managua_Survive_C, D.OS_Managua_Survive_U, ['OS_M_S_Comp', 'OS_M_S_NoComp'],
                          [D.PR_OS_M_S_Comp, (1-D.PR_OS_M_S_Comp)]],
    'OS_M_S_Comp': [D.OS_M_S_Comp_C, D.OS_M_S_Comp_U, ['OS_M_S_C_Major', 'OS_M_S_C_Minor'],
                    [D.PR_OS_M_S_C_Major, (1-D.PR_OS_M_S_C_Major)]],
    'OS_M_S_C_Major': [D.OS_M_S_C_Major_C, D.OS_M_S_C_Major_U, ['OS_M_S_C_Major_Die', 'OS_M_S_C_Major_Survive'],
                       [D.PR_OS_M_S_C_Major_Die, (1-D.PR_OS_M_S_C_Major_Die)]],
    'OS_Disease': [D.OS_Disease_C, D.OS_Disease_U, ['OS_Disease_Survive', 'OS_Disease_Die'],
                   [D.PR_OS_Disease_Die, (1-D.PR_OS_Disease_Die)]],
    # no opsmile
    'NoOS_OpSmile': [D.OpSmile_C, D.OpSmile_U, ['NoOS_Access', 'NoOS_NoAccess'], [D.PR_OS_Access, (1-D.PR_OS_Access)]],
    'NoOS_Access': [D.OpSmileAccess_C, D.OpSmileAccess_U, ['NoOS_Surgery', 'NoOS_NoSurgery'],
                          [D.PR_OS_A_Surgery, (1-D.PR_OS_A_Surgery)]],
    'NoOS_Surgery': [D.OpSmileSurgery_C, D.OpSmileSurgery_U, ['NoOS_OS_S_Die', 'NoOS_OS_S_Survive'],
                [D.PR_OS_S_Die, (1-D.PR_OS_S_Die)]],
    'NoOS_OS_S_Survive': [D.OS_S_Survive_C, D.OS_S_Survive_U, ['NoOS_OS_S_S_Comp', 'NoOS_OS_S_S_NoComp'],
                     [D.PR_OS_S_S_Comp, (1-D.PR_OS_S_S_Comp)]],
    'NoOS_OS_S_S_Comp': [D.OS_S_S_Comp_C, D.OS_S_S_Comp_U, ['NoOS_OS_S_S_C_Major', 'NoOS_OS_S_S_C_Minor'],
                    [D.PR_OS_S_S_C_Major, (1-D.PR_OS_S_S_C_Major)]],
    'NoOS_OS_S_S_C_Major': [D.OS_S_S_C_Major_C, D.OS_S_S_C_Major_U, ['NoOS_OS_S_S_C_Major_Die', 'NoOS_OS_S_S_C_Major_Survive'],
                       [D.PR_OS_S_S_C_Major_Die, (1-D.PR_OS_S_S_C_Major_Die)]],
    'NoOS_NoSurgery': [D.OpSmileAccess_NoSurgery_C, D.OpSmileAccess_NoSurgery_U, ['NoOS_NoSurgery_Die', 'NoOS_NoSurgery_Survive'],
                  [D.PR_OS_A_NoSurgery_Die, (1-D.PR_OS_A_NoSurgery_Die)]],  # likely a dominated strategy
    'NoOS_NoAccess': [D.OpSmileNoAccess_C, D.OpSmileNoAccess_U, ['NoOS_OS_Managua', 'NoOS_OS_Disease'],
                 [D.PR_OS_Managua, (1-D.PR_OS_Managua)]],
    'NoOS_OS_Managua': [D.OpSmile_Managua_C, D.OpSmile_Managua_U, ['NoOS_OS_Managua_Die', 'NoOS_OS_Managua_Survive'],
                [D.PR_OS_Managua_Die, (1-D.PR_OS_Managua_Die)]],
    'NoOS_OS_Managua_Survive': [D.OS_Managua_Survive_C, D.OS_Managua_Survive_U, ['NoOS_OS_M_S_Comp', 'NoOS_OS_M_S_NoComp'],
                          [D.PR_OS_M_S_Comp, (1-D.PR_OS_M_S_Comp)]],
    'NoOS_OS_M_S_Comp': [D.OS_M_S_Comp_C, D.OS_M_S_Comp_U, ['NoOS_OS_M_S_C_Major', 'NoOS_OS_M_S_C_Minor'],
                    [D.PR_OS_M_S_C_Major, (1-D.PR_OS_M_S_C_Major)]],
    'NoOS_OS_M_S_C_Major': [D.OS_M_S_C_Major_C, D.OS_M_S_C_Major_U, ['NoOS_OS_M_S_C_Major_Die', 'NoOS_OS_M_S_C_Major_Survive'],
                       [D.PR_OS_M_S_C_Major_Die, (1-D.PR_OS_M_S_C_Major_Die)]],
    'NoOS_OS_Disease': [D.OS_Disease_C, D.OS_Disease_U, ['NoOS_OS_Disease_Survive', 'NoOS_OS_Disease_Die'],
                   [D.PR_OS_Disease_Die, (1-D.PR_OS_Disease_Die)]]
}

# dictionary for terminal nodes
#               //key:                  cost,                               utility
dictTerminal = {
    'OS_S_Die': [D.OS_S_Die_C, D.OS_S_Die_U],
    'OS_S_S_NoComp': [D.OS_S_S_NoComp_C, D.OS_S_S_NoComp_U],
    'OS_S_S_C_Minor': [D.OS_S_S_Minor_C, D.OS_S_S_Minor_U],
    'OS_S_S_C_Major_Die': [D.OS_S_S_C_Major_Die_C, D.OS_S_S_C_Major_Die_U],
    'OS_S_S_C_Major_Survive': [D.OS_S_S_C_Major_Survive_C, D.OS_S_S_C_Major_Survive_U],
    'NoSurgery_Die': [D.OpSmile_NoSurgery_Die_C, D.OpSmile_NoSurgery_Die_U],
    'NoSurgery_Survive': [D.OpSmile_NoSurgery_Survive_C, D.OpSmile_NoSurgery_Survive_U],
    'OS_Managua_Die': [D.OS_Managua_Die_C, D.OR_Managua_Die_U],
    'OS_M_S_NoComp': [D.OS_M_S_NoComp_C, D.OS_M_S_NoComp_U],
    'OS_M_S_C_Minor': [D.OS_M_S_C_Minor_C, D.OR_M_S_C_Minor_U],
    'OS_M_S_C_Major_Die': [D.OS_M_S_C_Major_Die_C, D.OS_M_S_C_Major_Die_U],
    'OS_M_S_C_Major_Survive': [D.OS_M_S_C_Major_Survive_C, D.OS_M_S_C_Major_Survive_U],
    'OS_Disease_Die': [D.OS_Disease_Die_C, D.OS_Disease_Die_U],
    'OS_Disease_Survive': [D.OS_Disease_Survive_C, D.OS_Disease_Survive_U],
    # NoOpSmile
    'NoOS_OS_S_Die': [D.OS_S_Die_C, D.OS_S_Die_U],
    'NoOS_OS_S_S_NoComp': [D.OS_S_S_NoComp_C, D.OS_S_S_NoComp_U],
    'NoOS_OS_S_S_C_Minor': [D.OS_S_S_Minor_C, D.OS_S_S_Minor_U],
    'NoOS_OS_S_S_C_Major_Die': [D.OS_S_S_C_Major_Die_C, D.OS_S_S_C_Major_Die_U],
    'NoOS_OS_S_S_C_Major_Survive': [D.OS_S_S_C_Major_Survive_C, D.OS_S_S_C_Major_Survive_U],
    'NoOS_NoSurgery_Die': [D.OpSmile_NoSurgery_Die_C, D.OpSmile_NoSurgery_Die_U],
    'NoOS_NoSurgery_Survive': [D.OpSmile_NoSurgery_Survive_C, D.OpSmile_NoSurgery_Survive_U],
    'NoOS_OS_Managua_Die': [D.OS_Managua_Die_C, D.OR_Managua_Die_U],
    'NoOS_OS_M_S_NoComp': [D.OS_M_S_NoComp_C, D.OS_M_S_NoComp_U],
    'NoOS_OS_M_S_C_Minor': [D.OS_M_S_C_Minor_C, D.OR_M_S_C_Minor_U],
    'NoOS_OS_M_S_C_Major_Die': [D.OS_M_S_C_Major_Die_C, D.OS_M_S_C_Major_Die_U],
    'NoOS_OS_M_S_C_Major_Survive': [D.OS_M_S_C_Major_Survive_C, D.OS_M_S_C_Major_Survive_U],
    'NoOS_OS_Disease_Die': [D.OS_Disease_Die_C, D.OS_Disease_Die_U],
    'NoOS_OS_Disease_Survive': [D.OS_Disease_Survive_C, D.OS_Disease_Survive_U]
}

# CREATING DECISION NODE
#tree=DT.DecisionNode('d1', dict_decisions=dictDecisions, cum_prob=1, dict_chances=dictChances, dict_terminals=dictTerminal)

#print(tree.get_cost_utility())
#print(tree.get_terminal_prob())







