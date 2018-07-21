

# DALY calculation
K = 0               # modulates age weight inclusion (1 or 0)
C = 0.1658          # mathematical constant
r_YLL = 0             # discount rate (0%, 3%, or 6%)
a_YLL = 55              # age at death (randomize?)
b = 0.04            # parameter from age weighting function (0.04)
e = 2.72            # natural logarithm root (2.72)
L_YLL = 78              # life expectancy (randomize for condition or keep constant for country?)

#K = 0               # modulates age weight inclusion (1 or 0)
#C = 0.1658          # mathematical constant
r_YLD = 0.03            # discount rate (0%, 3%, or 6%)
a_YLD = 5              # age at ONSET (randomize?)
#b = 0.04            # parameter from age weighting function (0.04)
#e = 2.72            # natural logarithm root (2.72)
L_YLD = 7              # years lived with disability (randomize for condition or keep constant for country?)
D = .78             # disability weight


YLD_major_comp = YLD
YLL = YLL  # do we need different YLL's?
YLD_minor_comp = DALY.YLD
YLD_disease = DALY.YLD

########################################################################################################################
########################################################################################################################
# CHANCE NODES
########################################################################################################################
########################################################################################################################
# costs
########################################################################################################################
#OpSmile
OpSmile_C = 0
OS_Access_C = 0
OS_A_Surgery_C = 0
OS_A_S_Survive_C = 0
OS_A_S_S_Comp_C = 0
OS_A_S_S_C_Major_C = 0
OS_A_NoSurgery_C = 0
OS_NoAccess_C = 0
OS_NA_Managua_C = 0
OS_NA_M_Survive_C = 0
OS_NA_M_S_Comp_C = 200
OS_NA_M_S_C_Major_C = 0
OS_NA_Disease_C = 0
#NoOpSmile
NoOS_C = 10
NoOS_Access_C = 10
NoOS_A_Surgery_C = 10
NoOS_A_S_Survive_C = 80
NoOS_A_S_S_Comp_C = 2000
NoOS_A_S_S_C_Major_C = 5000
NoOS_A_NoSurgery_C = 10
NoOS_NoAccess_C = 10
NoOS_NA_Managua_C = 10
NoOS_NA_M_Survive_C = 300
NoOS_NA_M_S_Comp_C = 200
NoOS_NA_M_S_C_Major_C = 300
NoOS_NA_Disease_C = 20
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
PR_OpSmile = .5
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
PR_NoOS_Access = .05
PR_NoOS_A_Surgery = .05
PR_NoOS_S_Die = .05
PR_NoOS_S_S_Comp = .05
PR_NoOS_S_S_C_Major = .05
PR_NoOS_S_S_C_M_Die = .05
PR_NoOS_NS_Die = .05
PR_NoOS_NA_Managua = .05
PR_NoOS_NA_M_Die = .05
PR_NoOS_NA_M_Comp = .05
PR_NoOS_NA_M_Comp_Major = .05
PR_NoOS_NA_M_C_M_Die = .05
PR_NoOS_NA_D_Die = .05

########################################################################################################################
########################################################################################################################
# TERMINAL NODES
########################################################################################################################
########################################################################################################################
# costs
########################################################################################################################
#OpSmile
OS_S_Die_C = 100
OS_S_S_NoComp_C = 100
OS_S_S_Minor_C = 100
OS_S_S_C_Major_Die_C = 100
OS_S_S_C_Major_Survive_C = 100
OS_NoSurgery_Die_C = 100
OS_NoSurgery_Survive_C = 100
OS_Managua_Die_C = 100
OS_M_S_NoComp_C = 100
OS_M_S_C_Minor_C = 100
OS_M_S_C_Major_Die_C = 100
OS_M_S_C_Major_Survive_C = 100
OS_Disease_Die_C = 100
OS_Disease_Survive_C = 100
# NoOpSmile
NoOS_S_Die_C = 0
NoOS_S_S_NoComp_C = 0
NoOS_S_S_Minor_C = 0
NoOS_S_S_C_Major_Die_C = 0
NoOS_S_S_C_Major_Survive_C = 000
NoOS_NoSurgery_Die_C = 0
NoOS_NoSurgery_Survive_C = 0
NoOS_Managua_Die_C = 0
NoOS_M_S_NoComp_C = 0
NoOS_M_S_C_Minor_C = 0
NoOS_M_S_C_Major_Die_C = 0
NoOS_M_S_C_Major_Survive_C = 0
NoOS_Disease_Die_C = 0
NoOS_Disease_Survive_C = 0

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

