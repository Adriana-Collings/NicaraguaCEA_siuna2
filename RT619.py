import scr.DecisionTree as DT
import InputData as D

# dictionary for decision nodes
#               // key: cost, utility, [future nodes]
dictDecisions = {'d1': [0,     0,       ['doesnt_seek_care', 'diagnosed']]};

#           // key:                 cost,   utility,    [future nodes],                     [probabilities]


dictChances = { 'diagnosed':        [D.Diag_Cost,       D.Diag_U,               ['Access', 'NoAccess'],                \
                                     [D.Pr_Access, (1-D.Pr_Access)]],

                'Access':           [D.Access_Cost,     D.Access_U,             ['Surgeon', 'NonSurgeon'],             \
                                     [D.Pr_Surg,(1-D.Pr_Surg)]],

                'Surgeon':          [D.Surgeon_Cost,    D.Surgeon_U,            ['Die_Surg', 'Survive'],               \
                                     [D.Pr_Die, (1-D.Pr_Die)]],

                'Survive':          [D.Survive_Cost,    D.Survive_U,            ['Major_Comp', 'Minor_Comp', 'No_Comp'],\
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
                 }
