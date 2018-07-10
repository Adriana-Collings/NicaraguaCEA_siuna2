import InputDataAC76 as D

# DALY calculation
YLD_major_comp = 5
YLL = 10  # do we need different YLL's?
RD_major_comp = .4
pMajorComp = .2
YLD_minor_comp = 3
pComplications = .6
PST = .9  # probability of successful treatment
YLD_disease = 7
pSurgery = .7
RD_disease = .8
pAccess = .9
DALY = (((((((((YLD_major_comp*(1-RD_major_comp) + (YLL +YLD_major_comp))*pMajorComp) + ((1-pMajorComp)*YLD_minor_comp)) *
       pComplications) * PST) + ((1-PST)* (YLL + YLD_disease))) * pSurgery) +
       (1-pSurgery)*((RD_disease*YLL) + ((1-RD_disease)*YLD_disease))) * pAccess)

DALY2 = ((((((YLD_major_comp*(1-D.PR_OS_S_S_C_Major_Die)+ ((YLL+YLD_major_comp)*D.PR_OS_S_S_C_Major_Die)) *
        D.PR_OS_S_S_C_Major) + ((1-D.PR_OS_S_S_C_Major)*YLD_major_comp)) * D.PR_OS_S_S_Comp) +
        ((1-D.PR_OS_S_S_Comp)*0))* (1-D.PR_OS_S_Die)) + ((D.PR_OS_S_Die)*YLL)
