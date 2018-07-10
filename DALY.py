import InputDataAC76 as D

# DALY calculation
YLD_major_comp = 5
YLL = 10  # do we need different YLL's?
YLD_minor_comp = 3
YLD_disease = 7

DALY_OS= ((((((((((YLD_major_comp*(1-D.PR_OS_S_S_C_Major_Die)+ ((YLL+YLD_major_comp)*D.PR_OS_S_S_C_Major_Die)) *
        D.PR_OS_S_S_C_Major) + ((1-D.PR_OS_S_S_C_Major)*YLD_major_comp)) * D.PR_OS_S_S_Comp) +
        ((1-D.PR_OS_S_S_Comp)*0))* (1-D.PR_OS_S_Die)) + ((D.PR_OS_S_Die)*YLL)) * D.PR_OS_A_Surgery) +
        ((1-D.PR_OS_A_Surgery)*((YLD_disease*(1-D.PR_OS_A_NoSurgery_Die)) + (YLL*D.PR_OS_A_NoSurgery_Die))))*D.PR_OS_Access) +\
                (((((((((((YLD_major_comp*(1-D.PR_OS_M_S_C_Major_Die)) + ((YLL+YLD_major_comp)*D.PR_OS_M_S_C_Major_Die)) *
                   D.PR_OS_M_S_C_Major) + ((1-D.PR_OS_M_S_C_Major)*YLD_minor_comp)) * D.PR_OS_M_S_Comp) +
                    ((1-D.PR_OS_M_S_Comp)*0)) * (1-D.PR_OS_Managua_Die)) + (D.PR_OS_Managua_Die*YLL)) * D.PR_OS_Managua) +
                   ((1-D.PR_OS_Managua)*((YLD_disease*(1-D.PR_NoOS_NA_D_Die))+((YLL + YLD_disease)*D.PR_NoOS_NA_D_Die)))) *
                    (1-D.PR_OS_Access))


print(DALY_OS)

