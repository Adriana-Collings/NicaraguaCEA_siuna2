import scr.DecisionTree as DT
import InputData as D

# dictionary for decision nodes
#               // key: cost, utility, [future nodes]
dictDecisions = {'d1': [0,     0,       ['doesnt_seek_care', 'Diagnosed']]};

#           // key:                 cost,   utility,    [future nodes],                     [probabilities]


dictChances = { 'Diagnosed':        [D.Diag_Cost,       D.Diag_U,               ['Access', 'NoAccess'],                \
                                     [D.Pr_Access, (1-D.Pr_Access)]],

                'Access':           [D.Access_Cost,     D.Access_U,             ['Surgeon', 'NonSurgeon'],             \
                                     [D.Pr_Surg,(1-D.Pr_Surg)]],

                'Surgeon':          [D.Surgeon_Cost,    D.Surgeon_U,            ['Die_Surg', 'Survive'],               \
                                     [D.Pr_Die, (1-D.Pr_Die)]],

                'Survive':          [D.Survive_Cost,    D.Survive_U,           ['Major_Comp', 'Minor_Comp', 'No_Comp'],\
                                     [D.Pr_Maj_Comp, D.Pr_Min_Comp, (1-D.Pr_Maj_Comp - D.Pr_Min_Comp)]],

                'Major_Comp':       [D.Major_Comp_Cost, D.Major_Comp_U,         ['Die_Comp', 'Survive_Comp'],          \
                                     [D.Pr_Die_Comp, (1-D.Pr_Die_Comp)]],

                'NonSurgeon':       [D.Nonsurgeon_Cost, D.Nonsurgeon_U,         ['No_Surg_Die', 'No_Surg_Survive'],    \
                                     [D.Pr_NoSurg_Die, (1-D.Pr_NoSurg_Die)]],

                'No_Surg_Survive':  [D.No_Surg_Surv_Cost, D.No_Surg_Survive_U,  ['No_S_Major_Comp', 'No_S_Minor_Comp',\
                                     'No_S_No_Comp'],[D.Pr_NoS_Maj_Comp,D.Pr_NoS_Min_Comp, (1-D.Pr_NoS_Maj_Comp -      \
                                      D.Pr_NoS_Min_Comp)]],

                'No_S_Major_Comp':  [D.No_S_Maj_Comp_Cost, D.No_Surg_Maj_Comp_U, ['No_S_Maj_Comp_Die',                 \
                                     'No_S_Maj_Comp_Survive'], [D.Pr_No_S_Maj_Comp_Die, (1-D.Pr_No_S_Maj_Comp_Die)]],

                'NoAccess':         [D.No_Access_Cost,  D.No_Access_U,           ['No_A_Die', 'No_A_Survive'],         \
                                     [D.Pr_No_A_Die, (1-D.Pr_No_A_Die)]]
                };

# dictionary for terminal nodes
#               //key:                  cost,                               utility

dictTerminals = {   'Die_Surg':              [D.Die_Surg_Cost,                   D.Die_Surg_U],
                    'Minor_Comp':            [D.Minor_Comp_Cost,                 D.Minor_Comp_U],
                    'No_Comp':               [D.No_Comp_Cost,                    D.No_Comp_U],
                    'Die_Comp':              [D.Die_Comp_Cost,                   D.Die_Comp_U],
                    'Survive_Comp':          [D.Survive_Comp_Cost,               D.Survive_Comp_U],
                    'No_Surg_Die':           [D.No_Surg_Die_Cost,                D.No_Surg_Die_U],
                    'No_S_Minor_Comp':       [D.No_S_Min_Comp_Cost,              D.No_S_Min_Comp_U],
                    'No_S_No_Comp':          [D.No_S_No_Comp_Cost,               D.No_S_No_Comp_U],
                    'No_S_Maj_Comp_Die':     [D.No_S_Maj_Comp_Die_Cost,          D.No_S_Maj_Comp_Die_U],
                    'No_S_Maj_Comp_Survive': [D.No_S_Maj_Comp_Survive_Cost,      D.No_S_Maj_Comp_Survive_U],
                    'No_A_Die':              [D.No_Access_Die_Cost,              D.No_Access_Die_U],
                    'No_A_Survive':          [D.No_Access_Survive_Cost,          D.No_Access_Survive_U]
                 }

tree=DT.DecisionNode('d1', cum_prob=1, dict_decisions=dictDecisions, dict_chances=dictChances, dict_terminals=dictTerminals)

##CREATING CHANCE NODES
diagnosed=DT.ChanceNode('Diagnosed', cum_prob=1, dict_chances=dictChances, dict_terminals=dictTerminals)
access=DT.ChanceNode('Access', cum_prob=D.Pr_Access, dict_chances=dictChances, dict_terminals=dictTerminals)
surgeon=DT.ChanceNode('Surgeon', cum_prob=(D.Pr_Access*D.Pr_Surg), dict_chances=dictChances, dict_terminals=dictTerminals)
survive=DT.ChanceNode('Survive', cum_prob=(D.Pr_Access*D.Pr_Surg*(1-D.Pr_Die)), dict_chances=dictChances, \
    dict_terminals=dictTerminals)
major_complication=DT.ChanceNode('Major_Comp', cum_prob=D.Pr_Access*D.Pr_Surg*(1-D.Pr_Die)*D.Pr_Maj_Comp, \
    dict_chances=dictChances, dict_terminals=dictTerminals)
non_surgeon=DT.ChanceNode('NonSurgeon', cum_prob=(D.Pr_Access*(1-D.Pr_Surg)), dict_chances=dictChances, \
    dict_terminals=dictTerminals)
non_surg_survive=DT.ChanceNode('No_Surg_Survive', cum_prob=(D.Pr_Access*(1-D.Pr_Surg)*(1-D.Pr_NoSurg_Die)), \
    dict_chances=dictChances, dict_terminals=dictTerminals)
non_surg_maj_comp=DT.ChanceNode('No_S_Major_Comp', cum_prob=(D.Pr_Access*(1-D.Pr_Surg)*(1-D.Pr_NoSurg_Die)*D.Pr_NoS_Maj_Comp),\
    dict_chances=dictChances, dict_terminals=dictTerminals)
no_access=DT.ChanceNode('NoAccess', cum_prob=(1-D.Pr_Access), dict_chances=dictChances, dict_terminals=dictTerminals)


#CREATING TERMINAL NODES
die_surg=DT.TerminalNode(name='Die_Surg', cum_prob=(D.Pr_Access*D.Pr_Surg*D.Pr_Die), dict_terminals=dictTerminals)
minor_comp=DT.TerminalNode(name='Minor_Comp', cum_prob=(D.Pr_Access*D.Pr_Surg*(1-D.Pr_Die)*D.Pr_Min_Comp),\
    dict_terminals=dictTerminals)
no_comp=DT.TerminalNode(name='No_Comp', cum_prob=(D.Pr_Access*D.Pr_Surg*(1-D.Pr_Die)*(1-D.Pr_Maj_Comp-D.Pr_Min_Comp)),\
    dict_terminals=dictTerminals)
die_comp=DT.TerminalNode(name='Die_Comp', cum_prob=(D.Pr_Access*D.Pr_Surg*(1-D.Pr_Die)*D.Pr_Maj_Comp*D.Pr_Die_Comp),\
    dict_terminals=dictTerminals)
survive_comp=DT.TerminalNode(name='Survive_Comp', cum_prob=(D.Pr_Access*D.Pr_Surg*(1-D.Pr_Die)*D.Pr_Maj_Comp*(1-D.Pr_Die_Comp)),\
    dict_terminals=dictTerminals)
no_surg_die=DT.TerminalNode('No_Surg_Die', cum_prob=(D.Pr_Access*(1-D.Pr_Surg)*D.Pr_NoSurg_Die),\
    dict_terminals=dictTerminals)
no_surg_min_comp=DT.TerminalNode('No_S_Minor_Comp', cum_prob=(D.Pr_Access*(1-D.Pr_Surg)*(1-D.Pr_NoSurg_Die)*D.Pr_NoS_Min_Comp),\
    dict_terminals=dictTerminals)
no_surg_no_comp=DT.TerminalNode('No_S_No_Comp', cum_prob=(D.Pr_Access*(1-D.Pr_Surg)*(1-D.Pr_NoSurg_Die)\
    *(1-D.Pr_NoS_Min_Comp-D.Pr_NoS_Maj_Comp)), dict_terminals=dictTerminals)
no_surg_maj_comp_die=DT.TerminalNode('No_S_Maj_Comp_Die', cum_prob=(D.Pr_Access)*(1-D.Pr_Surg)*(1-D.Pr_NoSurg_Die)\
    *D.Pr_NoS_Maj_Comp*D.Pr_No_S_Maj_Comp_Die, dict_terminals=dictTerminals)
no_surg_maj_comp_surv=DT.TerminalNode('No_S_Maj_Comp_Survive', cum_prob=(D.Pr_Access*(1-D.Pr_Surg)*(1-D.Pr_NoSurg_Die)\
    *D.Pr_NoS_Maj_Comp*(1-D.Pr_No_S_Maj_Comp_Die)), dict_terminals=dictTerminals)
no_access_die=DT.TerminalNode('No_A_Die', cum_prob=((1-D.Pr_Access)*D.Pr_No_A_Die), dict_terminals=dictTerminals)
no_access_survive=DT.TerminalNode('No_A_Survive', cum_prob=((1-D.Pr_Access)*(1-D.Pr_No_A_Die)), dict_terminals=dictTerminals)

DT.create_future_nodes(['diagnosed', 'access', 'surgeon', 'survive', 'major_complication', 'non_surgeon', 'non_surg_survive',\
    'non_surg_maj_comp', 'no_access', 'die_surg', 'minor_comp', 'no_comp', 'die_comp', 'survive_comp', 'no_surg_die'\
    'no_surg_min_comp', 'no_surg_no_comp', 'no_surg_maj_comp_die', 'no_surg_mj_comp_surv', 'no_access_die',\
    'no_access_survive'], dict_terminals=dictTerminals, dict_chances=dictChances)

##CHECK ALL NODES to verify all have been created and all lead to the right nodes


print(diagnosed.get_terminal_prob())
print(tree.get_cost_utility())
print(tree.get_terminal_prob())

DT.graph_outcomes(tree)
