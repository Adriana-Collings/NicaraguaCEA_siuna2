import DT as DT
#import SimParameters as SP
import numpy
from numpy.random import choice
import random as random
import DisabilityWeights as DWpy
import distributions as dist

# infectious disease

# YLL & YLD -> DALY calculation
K = 0               # modulates age weight inclusion (1 or 0)
C = 0.1658          # mathematical constant
r_YLL = 0.03             # discount rate (0%, 3%, or 6%)
a_YLL = random.randint(5,75)                # age at death (randomize?)
b = 0.04            # parameter from age weighting function (0.04)
e = 2.72            # natural logarithm root (2.72)
L_YLL = 75              # life expectancy

r_YLD = 0.03            # discount rate (0%, 3%, or 6%)
a_YLD = dist.Age_infect            # age at ONSET (randomize?)
L_YLD = a_YLL - a_YLD              # years lived with disability (randomize for condition or keep constant for country?)
DW = DWpy.DW_infect            # disability weight

if r_YLL == 0:
    YLL = ((K * C * (e ** (-(b * a_YLL)))) / (b ** 2)) * \
          (e ** (-b * L_YLL) * (-b * (L_YLL + a_YLL) - 1) * ((-b * a_YLL) - 1)) + ((1 - K) * L_YLL)

if r_YLL != 0:
    YLL = ((K * C * (e ** (r_YLL * a_YLL))) / ((r_YLL + b) ** 2)) * \
          (e ** (-(r_YLL + b) * (L_YLL + a_YLL)) * (-(r_YLL + b) * (L_YLL + a_YLL) - 1) * (
                      e ** (-(r_YLL + b) * a_YLL)) * (-(r_YLL + b) * (a_YLL - 1))) + \
          (((1 - K) / r_YLL) * (1 - e ** (-r_YLL * L_YLL)))

if r_YLD == 0:
    YLD = DW * (((K * C * (e ** (-(b * a_YLD)))) / (b ** 2)) *
                 (e ** (-b * L_YLD) * (-b * (L_YLD + a_YLD) - 1) * ((-b * a_YLD) - 1)) + (
                             (1 - K) * L_YLD))

if r_YLD != 0:
    YLD = DW * ((K * C * (e ** (r_YLD * a_YLD))) / ((r_YLD + b) ** 2)) * \
          (e ** (-(r_YLD + b) * (L_YLD + a_YLD)) * (-(r_YLD + b) * (L_YLD + a_YLD) - 1) * (
                      e ** (-(r_YLD + b) * a_YLD)) * (-(r_YLD + b) * (a_YLD - 1))) + \
          (((1 - K) / r_YLD) * (1 - e ** (-r_YLD * L_YLD)))

# for now
YLD_major_comp = 30
YLD_minor_comp = 20
YLD_disease = 10


########################################################################################################################
########################################################################################################################
# CHANCE NODES
########################################################################################################################
########################################################################################################################
# costs
########################################################################################################################
#OpSmile
OpSmile_C = 20000
OS_Access_C = 0
OS_A_Surgery_C = 9719
OS_A_S_Survive_C = 0
OS_A_S_S_Comp_C = 0
OS_A_S_S_C_Major_C = 500
OS_A_NoSurgery_C = 0
OS_NoAccess_C = 0
OS_NA_Managua_C = 10000
OS_NA_M_Survive_C = 0
OS_NA_M_S_Comp_C = 0
OS_NA_M_S_C_Major_C = 300
OS_NA_Disease_C = 0

# NoOpSmile
NoOS_C = 0
NoOS_Access_C = 0
NoOS_A_Surgery_C = 9719
NoOS_A_S_Survive_C = 0
NoOS_A_S_S_Comp_C = 0
NoOS_A_S_S_C_Major_C = 5000
NoOS_A_NoSurgery_C = 0
NoOS_NoAccess_C = 0
NoOS_NA_Managua_C = 10000
NoOS_NA_M_Survive_C = 0
NoOS_NA_M_S_Comp_C = 0
NoOS_NA_M_S_C_Major_C = 300
NoOS_NA_Disease_C = 0

########################################################################################################################
# utilities
########################################################################################################################
OpSmile_U = 0               # all equal to zero when utility is DALY's because there are not terminal nodes
OS_Access_U = 0
OS_A_Surgery_U = 0
OS_A_S_Survive_U = 0
OS_A_S_S_Comp_U = 0
OS_A_S_S_C_Major_U = 0
OS_A_NoSurgery_U = 0
OS_NoAccess_U = 0
OS_NA_Managua_U = 0
OS_NA_M_Survive_U = 0
OS_NA_M_S_Comp_U = 0
OS_NA_M_S_C_Major_U = 0
OS_NA_Disease_U = 0
#NoOpSmile
NoOS_U = 0
NoOS_Access_U = 0
NoOS_A_Surgery_U = 0
NoOS_A_S_Survive_U = 0
NoOS_A_S_S_Comp_U = 0
NoOS_A_S_S_C_Major_U = 0
NoOS_A_NoSurgery_U = 0
NoOS_NoAccess_U = 0
NoOS_NA_Managua_U = 0
NoOS_NA_M_Survive_U = 0
NoOS_NA_M_S_Comp_U = 0
NoOS_NA_M_S_C_Major_U = 0
NoOS_NA_Disease_U = 0

########################################################################################################################
########################################################################################################################
# probabilities
########################################################################################################################
########################################################################################################################
PR_OpSmile = .9
PR_NoOpSmile = .5

PR_OS_Access = .5
PR_OS_A_Surgery = .5
PR_OS_S_Die = .5
PR_OS_S_S_Comp = .5
PR_OS_S_S_C_Major = .5
PR_OS_S_S_C_Major_Die = .5
PR_OS_A_NoSurgery_Die = .5
PR_OS_Managua = .5
PR_OS_Managua_Die = .5
PR_OS_M_S_Comp = .5
PR_OS_M_S_C_Major = .5
PR_OS_M_S_C_Major_Die = .5
PR_OS_Disease_Die = .5
# noOS
PR_NoOS_Access = .57
PR_NoOS_A_Surgery = .57
PR_NoOS_S_Die = .57
PR_NoOS_S_S_Comp = .57
PR_NoOS_S_S_C_Major = .57
PR_NoOS_S_S_C_M_Die = .57
PR_NoOS_NS_Die = .57
PR_NoOS_NA_Managua = .57
PR_NoOS_NA_M_Die = .7
PR_NoOS_NA_M_Comp = .57
PR_NoOS_NA_M_Comp_Major = .57
PR_NoOS_NA_M_C_M_Die = .57
PR_NoOS_NA_D_Die = .57

########################################################################################################################
########################################################################################################################
# TERMINAL NODES
########################################################################################################################
########################################################################################################################
# costs
########################################################################################################################
#OpSmile
OS_S_Die_C = 0
OS_S_S_NoComp_C = 0
OS_S_S_Minor_C = 100
OS_S_S_C_Major_Die_C = 0
OS_S_S_C_Major_Survive_C = 300
OS_NoSurgery_Die_C = 0
OS_NoSurgery_Survive_C = 100
OS_Managua_Die_C = 0
OS_M_S_NoComp_C = 0
OS_M_S_C_Minor_C = 100
OS_M_S_C_Major_Die_C = 0
OS_M_S_C_Major_Survive_C = 1000
OS_Disease_Die_C = 0
OS_Disease_Survive_C = 100
# NoOpSmile
NoOS_S_Die_C = 0
NoOS_S_S_NoComp_C = 0
NoOS_S_S_Minor_C = 100
NoOS_S_S_C_Major_Die_C = 0
NoOS_S_S_C_Major_Survive_C = 300
NoOS_NoSurgery_Die_C = 0
NoOS_NoSurgery_Survive_C = 100
NoOS_Managua_Die_C = 0
NoOS_M_S_NoComp_C = 0
NoOS_M_S_C_Minor_C = 100
NoOS_M_S_C_Major_Die_C = 0
NoOS_M_S_C_Major_Survive_C = 1000
NoOS_Disease_Die_C = 0
NoOS_Disease_Survive_C = 100

########################################################################################################################
# utilities
########################################################################################################################
#OpSmile
OS_S_Die_U=YLL
OS_S_S_NoComp_U=0
OS_S_S_Minor_U= YLD_minor_comp + YLL
OS_S_S_C_Major_Die_U= YLL
OS_S_S_C_Major_Survive_U= YLD_major_comp + YLL
OS_NoSurgery_Die_U= YLL
OS_NoSurgery_Survive_U= YLD_disease + YLL
OS_Managua_Die_U= YLL
OS_M_S_NoComp_U=0
OS_M_S_C_Minor_U=YLD_disease + YLL
OS_M_S_C_Major_Die_U=YLL
OS_M_S_C_Major_Survive_U= YLD_major_comp + YLL
OS_Disease_Die_U= YLL
OS_Disease_Survive_U=YLD_disease + YLL
#NoOpSmile
NoOS_S_Die_U= YLL
NoOS_S_S_NoComp_U= 0
NoOS_S_S_Minor_U= YLD_minor_comp + YLL
NoOS_S_S_C_Major_Die_U= YLL
NoOS_S_S_C_Major_Survive_U= YLD_major_comp + YLL
NoOS_NoSurgery_Die_U= YLL
NoOS_NoSurgery_Survive_U=YLD_disease + YLL
NoOS_Managua_Die_U= YLL
NoOS_M_S_NoComp_U= 0
NoOS_M_S_C_Minor_U= YLD_disease + YLL
NoOS_M_S_C_Major_Die_U= YLL
NoOS_M_S_C_Major_Survive_U=YLD_major_comp + YLL
NoOS_Disease_Die_U= YLL
NoOS_Disease_Survive_U= YLD_disease + YLL


# dictionary for decision nodes
#               // key: cost, utility, [future nodes]
dictDecisions_OS = {'d1': [5, 5, ['OpSmile', 'toss']]}
dictDecisions_NoOS = {'d2': [5, 5, ['NoOS', 'toss2']]}

#           // key: cost, utility, [future nodes], [probabilities]
dictChances_OS = {
    'OpSmile': [OpSmile_C, OpSmile_U, ['Access', 'NoAccess'], [PR_OS_Access, (1-PR_OS_Access)]],
    'Access': [OS_Access_C, OS_Access_U, ['Surgery', 'NoSurgery'],
                          [PR_OS_A_Surgery, (1-PR_OS_A_Surgery)]],
    'Surgery': [OS_A_Surgery_C, OS_A_Surgery_U, ['OS_S_Die', 'OS_S_Survive'],
                [PR_OS_S_Die, (1-PR_OS_S_Die)]],
    'OS_S_Survive': [OS_A_S_Survive_C, OS_A_S_Survive_U, ['OS_S_S_Comp', 'OS_S_S_NoComp'],
                     [PR_OS_S_S_Comp, (1-PR_OS_S_S_Comp)]],
    'OS_S_S_Comp': [OS_A_S_S_Comp_C, OS_A_S_S_Comp_U, ['OS_S_S_C_Major', 'OS_S_S_C_Minor'],
                    [PR_OS_S_S_C_Major, (1-PR_OS_S_S_C_Major)]],
    'OS_S_S_C_Major': [OS_A_S_S_C_Major_C, OS_A_S_S_C_Major_U, ['OS_S_S_C_Major_Die', 'OS_S_S_C_Major_Survive'],
                       [PR_OS_S_S_C_Major_Die, (1-PR_OS_S_S_C_Major_Die)]],
    'NoSurgery': [OS_A_NoSurgery_C, OS_A_NoSurgery_U, ['NoSurgery_Die', 'NoSurgery_Survive'],
                  [PR_OS_A_NoSurgery_Die, (1-PR_OS_A_NoSurgery_Die)]],
    'NoAccess': [OS_NoAccess_C, OS_NoAccess_U, ['OS_Managua', 'OS_Disease'],
                 [PR_OS_Managua, (1-PR_OS_Managua)]],
    'OS_Managua': [OS_NA_Managua_C, OS_NA_Managua_U, ['OS_Managua_Die', 'OS_Managua_Survive'],
                [PR_OS_Managua_Die, (1-PR_OS_Managua_Die)]],
    'OS_Managua_Survive': [OS_NA_M_Survive_C, OS_NA_M_Survive_U, ['OS_M_S_Comp', 'OS_M_S_NoComp'],
                          [PR_OS_M_S_Comp, (1-PR_OS_M_S_Comp)]],
    'OS_M_S_Comp': [OS_NA_M_S_Comp_C, OS_NA_M_S_Comp_U, ['OS_M_S_C_Major', 'OS_M_S_C_Minor'],
                    [PR_OS_M_S_C_Major, (1-PR_OS_M_S_C_Major)]],
    'OS_M_S_C_Major': [OS_NA_M_S_C_Major_C, OS_NA_M_S_C_Major_U, ['OS_M_S_C_Major_Die', 'OS_M_S_C_Major_Survive'],
                       [PR_OS_M_S_C_Major_Die, (1-PR_OS_M_S_C_Major_Die)]],
    'OS_Disease': [OS_NA_Disease_C, OS_NA_Disease_U, ['OS_Disease_Survive', 'OS_Disease_Die'],
                   [PR_OS_Disease_Die, (1-PR_OS_Disease_Die)]]}
dictChances_NoOS = {
    # no opsmile
    'NoOS': [NoOS_C, NoOS_U, ['NoOS_Access', 'NoOS_NoAccess'], [PR_NoOS_Access, (1-PR_NoOS_Access)]],
    'NoOS_Access': [NoOS_Access_C, NoOS_Access_U, ['NoOS_A_Surgery', 'NoOS_A_NoSurgery'],
                          [PR_NoOS_A_Surgery, (1-PR_NoOS_A_Surgery)]],
    'NoOS_A_Surgery': [NoOS_A_Surgery_C, NoOS_A_Surgery_U, ['NoOS_S_Die', 'NoOS_A_S_Survive'],
                [PR_NoOS_S_Die, (1-PR_NoOS_S_Die)]],
    'NoOS_A_S_Survive': [NoOS_A_S_Survive_C, NoOS_A_S_Survive_U, ['NoOS_A_S_S_Comp', 'NoOS_S_S_NoComp'],
                     [PR_NoOS_S_S_Comp, (1-PR_NoOS_S_S_Comp)]],
    'NoOS_A_S_S_Comp': [NoOS_A_S_S_Comp_C, NoOS_A_S_S_Comp_U, ['NoOS_A_S_S_C_Major', 'NoOS_S_S_C_Minor'],
                    [PR_NoOS_S_S_C_Major, (1-PR_NoOS_S_S_C_Major)]],
    'NoOS_A_S_S_C_Major': [NoOS_A_S_S_C_Major_C, NoOS_A_S_S_C_Major_U, ['NoOS_S_S_C_Major_Die', 'NoOS_S_S_C_Major_Survive'],
                       [PR_NoOS_S_S_C_M_Die, (1-PR_NoOS_S_S_C_M_Die)]],
    'NoOS_A_NoSurgery': [NoOS_A_NoSurgery_C, NoOS_A_NoSurgery_U, ['NoOS_NoSurgery_Die', 'NoOS_NoSurgery_Survive'],
                  [PR_NoOS_NS_Die, (1-PR_NoOS_NS_Die)]],  # likely a dominated strategy
    'NoOS_NoAccess': [NoOS_NoAccess_C, NoOS_NoAccess_U, ['NoOS_NA_Managua', 'NoOS_NA_Disease'],
                 [PR_NoOS_NA_Managua, (1-PR_NoOS_NA_Managua)]],
    'NoOS_NA_Managua': [NoOS_NA_Managua_C, NoOS_NA_Managua_U, ['NoOS_Managua_Die', 'NoOS_NA_M_Survive'],
                [PR_NoOS_NA_M_Die, (1-PR_NoOS_NA_M_Die)]],
    'NoOS_NA_M_Survive': [NoOS_NA_M_Survive_C, NoOS_NA_M_Survive_U, ['NoOS_NA_M_S_Comp', 'NoOS_M_S_NoComp'],
                          [PR_NoOS_NA_M_Comp, (1-PR_NoOS_NA_M_Comp)]],
    'NoOS_NA_M_S_Comp': [NoOS_NA_M_S_Comp_C, NoOS_NA_M_S_Comp_C, ['NoOS_NA_M_S_C_Major', 'NoOS_M_S_C_Minor'],
                    [PR_NoOS_NA_M_Comp_Major, (1-PR_NoOS_NA_M_Comp_Major)]],
    'NoOS_NA_M_S_C_Major': [NoOS_NA_M_S_C_Major_C, NoOS_NA_M_S_C_Major_U, ['NoOS_M_S_C_Major_Die', 'NoOS_M_S_C_Major_Survive'],
                       [PR_NoOS_NA_M_C_M_Die, (1-PR_NoOS_NA_M_C_M_Die)]],
    'NoOS_NA_Disease': [NoOS_NA_Disease_C, NoOS_NA_Disease_U, ['NoOS_Disease_Survive', 'NoOS_Disease_Die'],
                   [PR_NoOS_NA_D_Die, (1-PR_NoOS_NA_D_Die)]]
}

# dictionary for terminal nodes
#               //key:                  cost,                               utility
dictTerminal_OS = {
    'OS_S_Die': [OS_S_Die_C, OS_S_Die_U],
    'OS_S_S_NoComp': [OS_S_S_NoComp_C, OS_S_S_NoComp_U],
    'OS_S_S_C_Minor': [OS_S_S_Minor_C, OS_S_S_Minor_U],
    'OS_S_S_C_Major_Die': [OS_S_S_C_Major_Die_C, OS_S_S_C_Major_Die_U],
    'OS_S_S_C_Major_Survive': [OS_S_S_C_Major_Survive_C, OS_S_S_C_Major_Survive_U],
    'NoSurgery_Die': [OS_NoSurgery_Die_C, OS_NoSurgery_Die_U],
    'NoSurgery_Survive': [OS_NoSurgery_Survive_C, OS_NoSurgery_Survive_U],
    'OS_Managua_Die': [OS_Managua_Die_C, OS_Managua_Die_U],
    'OS_M_S_NoComp': [OS_M_S_NoComp_C, OS_M_S_NoComp_U],
    'OS_M_S_C_Minor': [OS_M_S_C_Minor_C, OS_M_S_C_Minor_U],
    'OS_M_S_C_Major_Die': [OS_M_S_C_Major_Die_C, OS_M_S_C_Major_Die_U],
    'OS_M_S_C_Major_Survive': [OS_M_S_C_Major_Survive_C, OS_M_S_C_Major_Survive_U],
    'OS_Disease_Die': [OS_Disease_Die_C, OS_Disease_Die_U],
    'OS_Disease_Survive': [OS_Disease_Survive_C, OS_Disease_Survive_U]}
dictTerminal_NoOS = {
    # NoOpSmile
    'NoOS_S_Die': [NoOS_S_Die_C, NoOS_S_Die_U],
    'NoOS_S_S_NoComp': [NoOS_S_S_NoComp_C, NoOS_S_S_NoComp_U],
    'NoOS_S_S_C_Minor': [NoOS_S_S_Minor_C, NoOS_S_S_Minor_U],
    'NoOS_S_S_C_Major_Die': [NoOS_S_S_C_Major_Die_C, NoOS_S_S_C_Major_Die_U],
    'NoOS_S_S_C_Major_Survive': [NoOS_S_S_C_Major_Survive_C, NoOS_S_S_C_Major_Survive_U],
    'NoOS_NoSurgery_Die': [NoOS_NoSurgery_Die_C, NoOS_NoSurgery_Die_U],
    'NoOS_NoSurgery_Survive': [NoOS_NoSurgery_Survive_C, NoOS_NoSurgery_Survive_U],
    'NoOS_Managua_Die': [NoOS_Managua_Die_C, NoOS_Managua_Die_U],
    'NoOS_M_S_NoComp': [NoOS_M_S_NoComp_C, NoOS_M_S_NoComp_U],
    'NoOS_M_S_C_Minor': [NoOS_M_S_C_Minor_C, NoOS_M_S_C_Minor_U],
    'NoOS_M_S_C_Major_Die': [NoOS_M_S_C_Major_Die_C, NoOS_M_S_C_Major_Die_U],
    'NoOS_M_S_C_Major_Survive': [NoOS_M_S_C_Major_Survive_C, NoOS_M_S_C_Major_Survive_U],
    'NoOS_Disease_Die': [NoOS_Disease_Die_C, NoOS_Disease_Die_U],
    'NoOS_Disease_Survive': [NoOS_Disease_Survive_C, NoOS_Disease_Survive_U]
}


DALY_OS=((((((((((YLD_major_comp*(1-PR_OS_S_S_C_Major_Die)+((YLL+YLD_major_comp)*PR_OS_S_S_C_Major_Die))*
    PR_OS_S_S_C_Major)+((1-PR_OS_S_S_C_Major)*YLD_major_comp))*PR_OS_S_S_Comp)+
    ((1-PR_OS_S_S_Comp)*0))*(1-PR_OS_S_Die))+((PR_OS_S_Die)*YLL))*PR_OS_A_Surgery)+
    ((1-PR_OS_A_Surgery)*((YLD_disease*(1-PR_OS_A_NoSurgery_Die))+(YLL*PR_OS_A_NoSurgery_Die))))*PR_OS_Access)+\
    (((((((((((YLD_major_comp*(1-PR_OS_M_S_C_Major_Die))+((YLL+YLD_major_comp)*PR_OS_M_S_C_Major_Die))*
    PR_OS_M_S_C_Major)+((1-PR_OS_M_S_C_Major)*YLD_minor_comp))*PR_OS_M_S_Comp)+
    ((1-PR_OS_M_S_Comp)*0))*(1-PR_OS_Managua_Die))+(PR_OS_Managua_Die*YLL))*PR_OS_Managua)+
    ((1-PR_OS_Managua)*((YLD_disease*(1-PR_OS_Disease_Die))+((YLL+YLD_disease)*PR_OS_Disease_Die))))*
    (1-PR_OS_Access))

DALY_NoOS=((((((((((YLD_major_comp*(1-PR_NoOS_S_S_C_M_Die)+((YLL+YLD_major_comp)*PR_NoOS_S_S_C_M_Die))*
    PR_NoOS_S_S_C_Major)+((1-PR_NoOS_S_S_C_Major)*YLD_major_comp))*PR_NoOS_S_S_Comp)+
    ((1-PR_OS_S_S_Comp)*0))*(1-PR_NoOS_S_Die))+((PR_NoOS_S_Die)*YLL))*PR_NoOS_A_Surgery)+
    ((1-PR_NoOS_A_Surgery)*((YLD_disease*(1-PR_NoOS_NS_Die))+(YLL*PR_NoOS_NS_Die))))*PR_NoOS_Access)+\
    (((((((((((YLD_major_comp*(1-PR_NoOS_NA_M_C_M_Die))+((YLL+YLD_major_comp)*PR_NoOS_NA_M_C_M_Die))*
    PR_NoOS_NA_M_Comp_Major)+((1-PR_NoOS_NA_M_Comp_Major)*YLD_minor_comp))*PR_NoOS_NA_M_Comp)+
    ((1-PR_NoOS_NA_M_Comp)*0))*(1-PR_NoOS_NA_M_Die))+(PR_NoOS_NA_M_Die*YLL))*PR_NoOS_NA_Managua)+
    ((1-PR_NoOS_NA_Managua)*((YLD_disease*(1-PR_NoOS_NA_D_Die))+((YLL+YLD_disease)*PR_NoOS_NA_D_Die))))*
    (1-PR_NoOS_Access))


DALY = DALY_OS - DALY_NoOS

def get_DALY(self):
    return DALY
