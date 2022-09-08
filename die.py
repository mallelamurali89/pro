from pprint import pprint 
import json
from collections import defaultdict
import pandas as pd

# f = open('2.json')
# payload = json.load(f)
payload = {
    "Products":[
        {"Name":"P1", "Dies":"2", "Shifts":"10","Type": ["M1","M2"],"Demand":"100"},
        {"Name":"P2", "Dies":"2", "Shifts":"10","Type": ["M2","M3"],"Demand":"100"},
        {"Name":"P3", "Dies":"3", "Shifts":"16", "Type": ["M1","M3"],"Demand":"11200"}
        ],
    "Machines":[
        {"Name":"M1","Type":"1", "NoOfMachines":"1"},
        {"Name":"M2","Type":"2", "NoOfMachines":"2"},
        {"Name":"M3","Type":"3", "NoOfMachines":"3"}
    ],
    "Inventory":[{"P1":"500", "P2":"344", "P3":"654"}],
    "Schedules" : {"Days":2,"shiftsperday":3}
    }
MachinesCount = defaultdict(dict)
MachineNames = defaultdict(dict)
Real_Mac_Names = []
for machines_sub in payload['Machines']: 
    MachinesCount[machines_sub['Name']] = int(machines_sub['NoOfMachines'])

for products in payload['Products']: 
    ShiftsCount = 1
    DieCount = products['Dies']
    TotalShifts = products['Shifts']
    j = 0
    while  j < len(products['Type']):
        
        if j < int(DieCount) :
            if MachinesCount[products['Type'][j]] > 0:
                MachineCheck = 0
                k = 1
                while  k <= payload['Schedules']['Days'] * payload['Schedules']['shiftsperday']:
                    if ShiftsCount <= int(TotalShifts):
                        MachineNames[str(str(str(str(products['Name']) + "-Die") + str((j + 1))) + "-") + str(products['Type'][j])]["S" + str(k)] = products['Name']
                        
                        ShiftsCount+=1
                        if MachineCheck == 0:
                            print(j,products['Name'],products['Type'][j],MachinesCount[products['Type'][j]],MachinesCount[products['Type'][j]] - 1)
                            MachinesCount[products['Type'][j]] = MachinesCount[products['Type'][j]] - 1
                        
                        MachineCheck = 1
                    k+=1
                
            else : 
                print(j,products['Name'],len(products['Type']))
                products['Type'][len(products['Type'])] = products['Type'][j + 1]


            
        
        j+=1
# pprint(MachineNames)    
pprint(MachinesCount)    
# pprint(Real_Mac_Names)
# dfs = pd.DataFrame(MachineNames)
# df1_transposed = dfs.T
# # pprint(df1_transposed.index)
# dxy = pd.DataFrame(df1_transposed.values, columns = list(df1_transposed.columns), index = [i[-2:] for i in list(df1_transposed.index)])
# print(dxy)
