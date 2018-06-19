#######################################################################################################################
#Costs
#######################################################################################################################
Diag_Cost = 0               #   cost to get diagnosed
Access_Cost =0              #   cost to have access
Surgeon_Cost =0             #   cost to have a surgery
Survive_Cost = 0            #   cost to survive surgery (0 likely)

##IF they get the surgery
Die_Surg_Cost =0            #   cost to die in surgery (0 likely)
Minor_Comp_Cost =0          #   cost of a minor commplication from surgery
No_Comp_Cost =0             #   cost of no complications from surgery (0 likely)
Major_Comp_Cost =0          #   cost of major complications from surgery
Die_Comp_Cost =0            #   cost to die in surgery (0 likely)
Survive_Comp_Cost = 0       #   cost to survive surgery (0 likely)

##If they don't get the surgery
Nonsurgeon_Cost =0          #   cost of a non-surgical procedure
No_Surg_Die_Cost=0          #   cost of dying in a non-surgical procedure (0 likely)
No_Surg_Surv_Cost =0        #   cost to survive a non-surgical procedure (0 likely)
No_S_Min_Comp_Cost = 0      #   cost of minor complications from non-surgical procedure
No_S_No_Comp_Cost=0         #   cost of no  complications from a surgical procedure (0 likely)
No_S_Maj_Comp_Cost=0        #   cost of major complications from a non-surgical procedure
No_S_Maj_Comp_Die_Cost=0    #   cost to die from major complications of a non-surgical procedure (0 likely)
No_S_Maj_Comp_Survive_Cost=0    # cost to survive major complications from a non-surgical procedure (0 likely)

No_Access_Cost=0            #   cost of no access

#######################################################################################################################
#Utilities
######################################################################################################################
Diag_U = 1                  #utility at diagnosis
Access_U = 1                #utility at time of access
Surgeon_U = 1               #utility at time of surgery

#If they get the surgery
Die_Surg_U =0               #utility upon death from surgery (0 likely)
Survive_U=1                 #utility of surviving surgery
Minor_Comp_U =1             #utility of a minor complication from surgery
No_Comp_U=1                 #utility of no complications from surgery
Major_Comp_U=1              #utility of a major complication from surgery
Die_Comp_U=0                #utility of dying from complications (0 likely)
Survive_Comp_U = 1          #utility of surviving a major surgery complication

#If they don't get the surgery
Nonsurgeon_U=0              #utility at the time of non-surgical procedure
No_Surg_Die_U=0             #utility of dying from a nonsurgical procedure
No_Surg_Survive_U=1         #utility of surviving a non-surgical proedure
No_S_Min_Comp_U=1           #utility of minor complications from a non-surgical procedure
No_S_No_Comp_U =1           #utility of no complications from a non-surgical procedure
No_Surg_Maj_Comp_U=0        #utility of major complications from a non-surgical procedure
No_S_Maj_Comp_Die_U=0       #utility of dying from major complications of a non-surgical proedure
No_S_Maj_Comp_Survive_U=1   #utility of surviving complications from a non-surgical procedure


No_Access_U=0               #utility of no access
####################################################################################################################
#Probabilities
###################################################################################################################
Pr_Access = 1               #probability of access
Pr_Surg = 1                 #probability of surgery

#if they get the surgery
Pr_Die = 0                  #probability of dying from surgery
Pr_Maj_Comp = 0             #probability of a major complication from surgery
Pr_Min_Comp = 0             #probability of a minor complication from surgery
Pr_Die_Comp = 0             #probability of dying from a major complication from surgery

#If they don't get the surgery
Pr_NoSurg_Die =0            #probability of dying from a non-surgical procedure
Pr_NoS_Maj_Comp=0           #probability of a major complication from a non-surgical procedure
Pr_NoS_Min_Comp=0           #probability of a minor complication from a non-surgial procedure
Pr_No_S_Maj_Comp_Die=0      #probabilty of dying from a major complication of a non-surgical procedure
Pr_No_A_Die=0               #probability of dying with no access to healthcare
