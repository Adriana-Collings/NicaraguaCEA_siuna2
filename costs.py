#data adopted from FINAL MARZO CPEP powerpoint

#training Siuna breakdown
BLS = (57/117)*21060
BLS_instructor = (9/12)*4800
ACLS = (3/6)*1200
code_red = (60/120)*5500
pain_manage = (6/12)*3600
anesthesia = (3/5)*750
prophylaxis = (6/12)*750
safe_surgery = (6/12)*500
surgical_goals = (3/5)*3440
gyno_conference = (5/10)*1500
verification_list = (26/50)*500
trauma = (26/39)*9575
checklist = (20/35)*5000
training_total = float(BLS) + float(BLS_instructor) + float(ACLS)+ float(code_red) + float(pain_manage) + \
                 float(anesthesia) + float(prophylaxis) + float(safe_surgery) + float(surgical_goals) + \
                 float(gyno_conference) + float(verification_list) + float(trauma) + float(checklist)

#Equipment Siuna breakdown
project_cure = 10292.78/2
gradian = (1/2)*42700
arbutus_medical = 4300/2
DRE_med = (5/7)*40000
Casa_teran = (6/10)*31574.27
buhler_pharma = 1*16640
drogueria_nunez = (49/82)*23270.75
MBS_medica = (114/249)*2280.50
Tech_medical = 545.78/2
aesculap = 110232.37/2
fluke_corp = 5033.07/2
madge_tech = 1872.93/2
equipment_supplies_total = float(project_cure) + float(gradian) + float(arbutus_medical) + float(DRE_med) + float(Casa_teran) + \
                  float(buhler_pharma) + float(drogueria_nunez) + float(MBS_medica) + float(Tech_medical) + \
                  float(aesculap) + float(fluke_corp) + float(madge_tech)

#acquired equipment Bonanza
strylker = (4/6)*10000
ZIP_IQ = 1*1200
Ethicon = 1*14386.21
Maxilofacial = 1*180
Uro = (1/2)*1300
McGee = 1*150
Kavorkian = (1/2)*2700 # note that the amount per site cannot be read and so half the cost was taken
Strauss = (1/2)*5600
Cottle = (1/2)*45
Sony = 1*3565
acquired_equipment_total = float(strylker) + float(ZIP_IQ) + float(Ethicon) + float(Maxilofacial) + float(Uro) + \
                          float(McGee) + float(Kavorkian) + float(Strauss) + float(Cottle) + float(Sony)

# infrastructure Bonanaza
infrastructure_breakdown = float(4474.39) + float(181471.08)

infrastructure = infrastructure_breakdown
equipment_donation = 327868.66/2
acquired_equipment = acquired_equipment_total
equipment_supplies = equipment_supplies_total
education_training = float(training_total) + float(67961/2)

total = float(infrastructure) + float(equipment_donation) + float(acquired_equipment) + float(equipment_supplies) + float(education_training)

OpSmile_C = total                    # Cost of Operation Smile Project Implementation
OS_Surgery_C = 0                  # Cost of Surgery with OpSmile
OS_NoSurgery_C = 0                  # Cost of No surgery with OpSmile
#NoOpSmile
NoOS_C = 0                         # Cost of No Operation Smile Project Implementation
NoOS_Surgery_C = 0                  # Cost of NoOpSmile Surgery
NoOS_NoSurgery_C = 0               # Cost no surgery without OpSmile

print(infrastructure)
print(equipment_donation)
print(acquired_equipment)
print(equipment_supplies)
print(education_training)
print(total)