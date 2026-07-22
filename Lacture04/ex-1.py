print("KPH\tMPH")
print("------------------")

for KPH in (60,70,80,130):
    
    MPH = KPH*0.6214
    print(KPH,"\t",MPH)
    
print()    
for MPH in (37.3,43.5,49.7,80.8):
    KPH = MPH//0.6214
    print(KPH,"\t",MPH)
