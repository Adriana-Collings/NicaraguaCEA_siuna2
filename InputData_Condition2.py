# DALY calculation
YLD_major_comp = 5
YLL = 10  # do we need different YLL's?
YLD_minor_comp = 3
YLD_disease = 7

########################################################################################################################
########################################################################################################################
# CHANCE NODES
########################################################################################################################
########################################################################################################################
# costs
########################################################################################################################
#OpSmile
OpSmile_C = 5000
OS_Access_C = 200
OS_A_Surgery_C = 700
OS_A_S_Survive_C = 80
OS_A_S_S_Comp_C = 2000
OS_A_S_S_C_Major_C = 5000
OS_A_NoSurgery_C = 20
OS_NoAccess_C = 0
OS_NA_Managua_C = 10000
OS_NA_M_Survive_C = 300
OS_NA_M_S_Comp_C = 200
OS_NA_M_S_C_Major_C = 300
OS_NA_Disease_C = 20
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
OpSmile_U = 5
OS_Access_U = 10
OS_A_Surgery_U = 20
OS_A_S_Survive_U = 15
OS_A_S_S_Comp_U = 12
OS_A_S_S_C_Major_U = 1
OS_A_NoSurgery_U = 10
OS_NoAccess_U = 2
OS_NA_Managua_U = 1
OS_NA_M_Survive_U = 10
OS_NA_M_S_Comp_U = 3
OS_NA_M_S_C_Major_U = 1
OS_NA_Disease_U = 4
#NoOpSmile
NoOS_U = 10
NoOS_Access_U = 10
NoOS_A_Surgery_U = 10
NoOS_A_S_Survive_U = 80
NoOS_A_S_S_Comp_U = 0
NoOS_A_S_S_C_Major_U = 0
NoOS_A_NoSurgery_U = 10
NoOS_NoAccess_U = 10
NoOS_NA_Managua_U = 10
NoOS_NA_M_Survive_U = 300
NoOS_NA_M_S_Comp_U = 200
NoOS_NA_M_S_C_Major_U = 300
NoOS_NA_Disease_U = 20

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
PR_NoOS_Access = .5
PR_NoOS_A_Surgery = .5
PR_NoOS_S_Die = .5
PR_NoOS_S_S_Comp = .5
PR_NoOS_S_S_C_Major = .5
PR_NoOS_S_S_C_M_Die = .5
PR_NoOS_NS_Die = .5
PR_NoOS_NA_Managua = .5
PR_NoOS_NA_M_Die = .5
PR_NoOS_NA_M_Comp = .5
PR_NoOS_NA_M_Comp_Major = .5
PR_NoOS_NA_M_C_M_Die = .5
PR_NoOS_NA_D_Die = .5

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
# OpSmile
OS_S_Die_U = 10
OS_S_S_NoComp_U = 10
OS_S_S_Minor_U = 10
OS_S_S_C_Major_Die_U = 10
OS_S_S_C_Major_Survive_U = 10
OS_NoSurgery_Die_U = 10
OS_NoSurgery_Survive_U = 10
OS_Managua_Die_U = 10
OS_M_S_NoComp_U = 10
OS_M_S_C_Minor_U = 10
OS_M_S_C_Major_Die_U = 10
OS_M_S_C_Major_Survive_U = 10
OS_Disease_Die_U = 10
OS_Disease_Survive_U = 10
# NoOpSmile
NoOS_S_Die_U = 10
NoOS_S_S_NoComp_U = 10
NoOS_S_S_Minor_U = 10
NoOS_S_S_C_Major_Die_U = 10
NoOS_S_S_C_Major_Survive_U = 10
NoOS_NoSurgery_Die_U = 10
NoOS_NoSurgery_Survive_U = 10
NoOS_Managua_Die_U = 10
NoOS_M_S_NoComp_U = 10
NoOS_M_S_C_Minor_U = 10
NoOS_M_S_C_Major_Die_U = 10
NoOS_M_S_C_Major_Survive_U = 10
NoOS_Disease_Die_U = 10
NoOS_Disease_Survive_U = 10

