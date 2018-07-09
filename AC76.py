import scr.DecisionTree as DT
import InputDataAC76 as D

# dictionary for decision nodes
#               // key: cost, utility, [future nodes]
dictDecisions = {'d1': [5, 5, ['OpSmile', 'noOpSmile']]}

#           // key: cost, utility, [future nodes], [probabilities]
dictChances_OS = {
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
                  [D.PR_OS_A_NoSurgery_Die, (1-D.PR_OS_A_NoSurgery_Die)]],  # likely a dominated strategy
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
                   [D.PR_OS_Disease_Die, (1-D.PR_OS_Disease_Die)]]}  # this would be the dominator
    # no opsmile
dictChances_NoOS = {
    'noOpSmile': [D.NoOpSmile_C, D.NoOpSmile_U, ['NoOpSmile_Access', 'NoOpSmile_NoAccess'],
                  [D.PR_NoOpSmile_Access, (1-D.PR_NoOpSmile_Access)]],
    'NoOpSmile_Access': [D.NoOpSmile_Access_C, D.NoOpSmile_Access_U, ['NoOS_Surgery', 'NoOS_NoSurgery'],
                         [D.PR_NoOpSmile_Surgery, (1-D.PR_NoOpSmile_Surgery)]],
    'NoOS_Surgery': [D.NoOS_Surgery_C, D.NoOS_Surgery_U, ['NoOS_Surgery_Die', 'NoOS_Surgery_Survive'],
                     [D.PR_NoOS_Surgery_Die, (1-D.PR_NoOS_Surgery_Die)]],
    'NoOS_Surgery_Survive': [D.NoOS_Surgery_Survive_C, D.NoOS_Surgery_Survive_U, ['NoOS_S_S_Comp', 'NoOS_S_S_NoComp'],
                             [D.PR_NoOS_S_S_Comp, (1-D.PR_NoOS_S_S_Comp)]],
    'NoOS_S_S_Comp': [D.NoOS_S_S_Comp_C, D.NoOS_S_S_Comp_U, ['NoOS_S_S_C_Major', 'NoOS_S_S_C_Minor'],
                      [D.PR_NoOS_S_S_C_Major, (1-D.PR_NoOS_S_S_C_Major)]],
    'NoOS_S_S_C_Major': [D.NoOS_S_S_C_Major_C, D.NoOS_S_S_C_Major_U, ['NoOS_S_S_C_M_Die', 'NoOS_S_S_C_M_Survive'],
                         [D.PR_NoOS_S_S_C_M_Die, (1-D.PR_NoOS_S_S_C_M_Die)]],
    'NoOS_NoSurgery': [D.NoOS_NoSurgery_C, D.NoOS_NoSurgery_U, ['NoOS_NS_Die', 'NoOS_NS_Survive'],
                       [D.PR_NoOS_NS_Die, (1-D.PR_NoOS_NS_Die)]],
    'NoOpSmile_NoAccess': [D.NoOpSmile_NoAccess_C, D.NoOpSmile_NoAccess_U, ['NoOS_NA_Managua', 'NoOS_NA_Disease'],
                           D.PR_NoOS_NA_Managua, (1-D.PR_NoOS_NA_Managua)],
    'NoOS_NA_Managua': [D.NoOS_NA_Managua_C, D.NoOS_NA_Managua_U, ['NoOS_NA_M_Die', 'NoOS_NA_M_Survive'],
                        [D.Pr_NoOS_NA_M_Die, (1-D.Pr_NoOS_NA_M_Die)]],
    'NoOS_NA_M_Survive': [D.NoOS_NA_M_Survive_C, D.NoOS_NA_M_Survive_U, ['NoOS_NA_M_Comp', 'NoOS_NA_M_NoComp'],
                        [D.Pr_NoOS_NA_M_Comp, (1-D.Pr_NoOS_NA_M_Comp)]],
    'NoOS_NA_M_Comp': [D.NoOS_NA_M_Comp_C, D.NoOS_NA_M_Comp_U, ['NoOS_NA_M_Comp_Major', 'NoOS_NA_M_Comp_Minor'],
                       [D.PR_NoOS_M_Comp_Major, (1-D.PR_NoOS_M_Comp_Major)]],
    'NoOS_NA_M_Comp_Major': [D.NoOS_NA_M_Comp_Major_C, D.NoOS_NA_M_C_Major_U, ['NoOS_NA_M_C_M_Die',
                                                                               'NoOS_NA_M_C_M_Survive'],
                             [D.PR_NoOS_NA_M_C_M_Die, (1-D.PR_NoOS_NA_M_C_M_Die)]],
    'NoOS_NA_Disease': [D.NoOS_NA_Disease_C, D.NoOS_NA_Disease_U, ['NoOS_NA_D_Die', 'NoOS_NA_D_Survive'],
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
    'NoSurgery_Die': [D.OpSmile_NoSurgery_Die_C, D.OpSmile_NoSurgery_Die_U],
    'NoSurgery_Survive': [D.OpSmile_NoSurgery_Survive_C, D.OpSmile_NoSurgery_Survive_U],
    'OS_Managua_Die': [D.OS_Managua_Die_C, D.OR_Managua_Die_U],
    'OS_M_S_NoComp': [D.OS_M_S_NoComp_C, D.OS_M_S_NoComp_U],
    'OS_M_S_C_Minor': [D.OS_M_S_C_Minor_C, D.OR_M_S_C_Minor_U],
    'OS_M_S_C_Major_Die': [D.OS_M_S_C_Major_Die_C, D.OS_M_S_C_Major_Die_U],
    'OS_M_S_C_Major_Survive': [D.OS_M_S_C_Major_Survive_C, D.OS_M_S_C_Major_Survive_U],
    'OS_Disease_Die': [D.OS_Disease_Die_C, D.OS_Disease_Die_U],
    'OS_Disease_Survive': [D.OS_Disease_Survive_C, D.OS_Disease_Survive_U] }
    # NoOpSmile
dictTerminal_noOS = {
    'NoOS_Surgery_Die': [D.NoOS_Surgery_Die_C, D.NoOS_Surgery_Die_U],
    'NoOS_S_S_NoComp': [D.NoOS_S_S_NoComp_C, D.NoOS_S_S_NoComp_U],
    'NoOS_S_S_C_Minor': [D.NoOS_S_S_C_Minor_C, D.NoOS_S_S_C_Minor_U],
    'NoOS_S_S_C_M_Die': [D.NoOS_S_S_C_M_Die_C, D.NoOS_S_S_C_M_Die_U],
    'NoOS_S_S_C_M_Survive': [D.NoOS_S_S_C_M_Survive_C, D.NoOS_S_S_C_M_Survive_U],
    'NoOS_NA_M_Die': [D.NoOS_NA_M_Die_C, D.NoOS_NA_M_Die_U],
    'NoOS_NA_M_NoComp': [D.NoOS_NA_M_NoComp_C, D.NoOS_NA_M_NoComp_U],
    'NoOS_NA_M_Comp_Minor': [D.NoOS_NA_M_Comp_Minor_C, D.NoOS_NA_M_Comp_Minor_U],
    'NoOS_NA_M_C_M_Die': [D.NoOS_NA_M_C_M_Die_C, D.NoOS_NA_M_C_M_Die_U],
    'NoOS_NA_M_C_M_Survive': [D.NoOS_NA_M_C_M_Survive_C, D.NoOS_NA_M_C_M_Survive_U],
    'NoOS_NS_Die': [D.NoOS_NS_Die_C, D.NoOS_NS_Die_U],
    'NoOS_NS_Survive': [D.NoOS_NS_Survive_C, D.NoOS_NS_Survive_U],
    'NoOS_NA_D_Die' : [D.NoOS_NA_D_Die_C, D.NoOS_NA_D_Die_U],
    'NoOS_NA_D_Survive' : [D.NoOS_NA_D_Survive_C, D.NoOS_NA_D_Survive_U]
}

# CREATING DECISION NODE
tree=DT.DecisionNode('d1', dict_decisions=dictDecisions, dict_chances=dictChances_NoOS, dict_terminals=dictTerminal_noOS)


print(tree.get_cost_utility())
print(tree.get_terminal_prob())


# i dont understand github

