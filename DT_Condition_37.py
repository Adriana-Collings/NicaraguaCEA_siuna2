import DT as DT
#import SimParameters as SP
import numpy
from numpy.random import choice
import random as random
import DisabilityWeights as DWpy
import distributions as dist
import probabilities as PR
import costs as Co

# biliary disease

# YLL & YLD -> DALY calculation
K = 0               # modulates age weight inclusion (1 or 0)
C = 0.1658          # mathematical constant
r_YLL = 0.0             # discount rate (0%, 3%, or 6%)
b = 0.04            # parameter from age weighting function (0.04)
e = 2.72            # natural logarithm root (2.72)
L_YLL = 75              # life expectancy

r_YLD = 0.0            # discount rate (0%, 3%, or 6%)
a_YLD = dist.Age_biliary             # age at ONSET (randomize?)
a_YLL = random.randint(round(a_YLD, 0), 75)  # age at death
L_YLD = a_YLL - a_YLD              # years lived with disability (randomize for condition or keep constant for country?)
DW = DWpy.DW_biliary            # disability weight

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

YLD_disease = YLD
########################################################################################################################
########################################################################################################################
# probabilities
########################################################################################################################
########################################################################################################################
PR_OS_Surgery = PR.gall_os_s
PR_OS_NoSurgery = 1-PR_OS_Surgery

PR_NoOS_Surgery = PR.gall_noos_s
PR_NoOS_NoSurgery = 1-PR_NoOS_Surgery
########################################################################################################################
DALY = (YLD_disease)

def get_DALY(self):
    return DALY


########################################################################################################################
# costs
########################################################################################################################
#OpSmile
OpSmile_C = Co.OpSmile_C                   # Cost of Operation Smile Project Implementation
OS_Surgery_C = Co.OS_Surgery_C                   # Cost of Surgery with OpSmile
OS_NoSurgery_C = Co.OS_NoSurgery_C              # Cost of No surgery with OpSmile
#NoOpSmile
NoOS_C = Co.NoOS_C                         # Cost of No Operation Smile Project Implementation
NoOS_Surgery_C = Co.NoOS_Surgery_C               # Cost of NoOpSmile Surgery
NoOS_NoSurgery_C = Co.NoOS_NoSurgery_C               # Cost no surgery without OpSmile
########################################################################################################################
# utilities
########################################################################################################################
#OpSmile_U = 0
OS_Surgery_U = 0
OS_NoSurgery_U = DALY
#NoOS_U = 0
NoOS_Surgery_U = 0
NoOS_NoSurgery_U = DALY
########################################################################################################################

# dictionary for decision nodes
#               // key: cost, utility, [future nodes]
dictDecisions_OS = {'d1': [Co.OpSmile_C  , 5, ['OpSmile', 'toss']]}
dictDecisions_NoOS = {'d2': [Co.NoOS_C , 5, ['NoOS', 'toss2']]}

# dictionary for terminal nodes
#               //key:           cost, utility
dictTerminal_OS = {'OS_Surgery': [OS_Surgery_C, OS_Surgery_U],
                   'OS_NoSurgery': [OS_NoSurgery_C, OS_NoSurgery_U],
                   }

dictTerminal_NoOS = {'NoOS_Surgery': [NoOS_Surgery_C, NoOS_Surgery_U],
                   'NoOS_NoSurgery': [NoOS_NoSurgery_C, NoOS_NoSurgery_U]}