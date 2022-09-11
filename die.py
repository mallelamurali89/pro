from pprint import pprint 
import json
from collections import defaultdict
import pandas as pd

# f = open('2.json')
# payload = json.load(f)
# payload = {
#     "Products":[
#         {"Name":"P1", "Dies":"2", "Shifts":"10","Type":{0:"M1",1:"M2"},"Demand":"8000"},
#         {"Name":"P2", "Dies":"2", "Shifts":"10","Type":{0:"M2",1:"M3"},"Demand":"4500"},
#         {"Name":"P3", "Dies":"3", "Shifts":"16","Type":{0:"M1",1:"M3"},"Demand":"5000"}
#         ],
#     "Machines":[
#         {"Name":"M1","Type":"1", "NoOfMachines":"1"},
#         {"Name":"M2","Type":"2", "NoOfMachines":"2"},
#         {"Name":"M3","Type":"3", "NoOfMachines":"3"}
#     ],
#     "Inventory":[{"P1": "150","P2": "250","P3": "350"}],
#     "dispatch": [{"P1": "700","P2": "500","P3": "850"}],
#     "Schedules" : {"Days":2,"shiftsperday":3}
# }
# payload = {
#     "Products":[
#         {"Name":"P1", "Dies":"1", "Shifts":"17","Type":{0:"M1",1:"M2"},"Demand":"2200"},
#         {"Name":"P2", "Dies":"2", "Shifts":"7","Type":{0:"M2",1:"M3"},"Demand":"2800"},
#         {"Name":"P3", "Dies":"2", "Shifts":"25", "Type":{0:"M3",1:"M1"},"Demand":"5800"},
#         {"Name":"P4", "Dies":"2", "Shifts":"21", "Type":{0:"M1",1:"M2",2:"M3"},"Demand":"3850"},
#         {"Name":"P5", "Dies":"1", "Shifts":"15", "Type":{0:"M1",1:"M2"},"Demand":"4200"},
#         {"Name":"P6", "Dies":"2", "Shifts":"22", "Type":{0:"M2",1:"M3"},"Demand":"4950"},
#         {"Name":"P7", "Dies":"1", "Shifts":"12", "Type":{0:"M1",1:"M3"},"Demand":"3450"},
#         {"Name":"P8", "Dies":"3", "Shifts":"23", "Type":{0:"M1",1:"M2",2:"M3"},"Demand":"5200"},
#         {"Name":"P9", "Dies":"1", "Shifts":"8", "Type":{0:"M1",1:"M2"},"Demand":"4000"},
#         {"Name":"P10", "Dies":"2", "Shifts":"26", "Type":{0:"M2",1:"M3"},"Demand":"3500"}
#         ],
#     "Machines":[
#         {"Name":"M1","Type":"1", "NoOfMachines":"4"},
#         {"Name":"M2","Type":"2", "NoOfMachines":"2"},
#         {"Name":"M3","Type":"3", "NoOfMachines":"3"}
#     ],
#     "Inventory":[{
#         "P1": "500",
#         "P2": "400",
#         "P3": "200",
#         "P4": "500",
#         "P5": "400",
#         "P6": "300",
#         "P7": "600",
#         "P8": "700",
#         "P9": "500",
#         "P10": "100"
#     }],
#     "dispatch": [
#         {
#             "P1": "100",
#             "P2": "100",
#             "P3": "50",
#             "P4": "150",
#             "P5": "100",
#             "P6": "200",
#             "P7": "50",
#             "P8": "100",
#             "P9": "200",
#             "P10": "100"
#         }
#     ],
#     "Schedules" : {"Days":7,"shiftsperday":3}
# }
# payload = {
#     "Products":[
#         {"Name":"P1", "Dies":"1", "Shifts":"19","Type":{0:"M1",1:"M2"},"Demand":"2350"},
#         {"Name":"P2", "Dies":"2", "Shifts":"28","Type":{0:"M2",1:"M3"},"Demand":"4800"},
#         {"Name":"P3", "Dies":"2", "Shifts":"33","Type":{0:"M3",1:"M4"},"Demand":"6450"},
#         {"Name":"P4", "Dies":"4", "Shifts":"53","Type":{0:"M1",1:"M4"},"Demand":"11200"},
#         {"Name":"P5", "Dies":"3", "Shifts":"26","Type":{0:"M1",1:"M3"},"Demand":"5000"},
#         {"Name":"P6", "Dies":"2", "Shifts":"32","Type":{0:"M2",1:"M4"},"Demand":"5050"}
#         ],
#     "Machines":[
#         {"Name":"M1","Type":"1", "NoOfMachines":"2"},
#         {"Name":"M2","Type":"2", "NoOfMachines":"2"},
#         {"Name":"M3","Type":"3", "NoOfMachines":"3"},
#         {"Name":"M4","Type":"4", "NoOfMachines":"4"}
#     ],
#     "Inventory":[{
#         "P1": "500",
#         "P2": "250",
#         "P3": "200",
#         "P4": "500",
#         "P5": "500",
#         "P6": "100"
#     }],
#     "dispatch": [
#         {
#             "P1": "100",
#             "P2": "200",
#             "P3": "150",
#             "P4": "250",
#             "P5": "100",
#             "P6": "200"
#         }
#     ],
#     "Schedules" : {"Days":7,"shiftsperday":3}
# }

payload = {
    "Products":[
        {"Name":"P1", "Dies":"1", "Shifts":"13","Type":{0:"M1",1:"M2"},"Demand":"8000"},
        {"Name":"P2", "Dies":"2", "Shifts":"22","Type":{0:"M2",1:"M3"},"Demand":"4500"},
        {"Name":"P3", "Dies":"1", "Shifts":"15","Type":{0:"M1",1:"M3"},"Demand":"5000"},
        {"Name":"P4", "Dies":"2", "Shifts":"25","Type":{0:"M1",1:"M2",2:"M3"},"Demand":"5000"}
        ],
    "Machines":[
        {"Name":"M1","Type":"1", "NoOfMachines":"1"},
        {"Name":"M2","Type":"2", "NoOfMachines":"2"},
        {"Name":"M3","Type":"3", "NoOfMachines":"2"}
    ],
    "Inventory":[{"P1": "150","P2": "250","P3": "350"}],
    "dispatch": [{"P1": "700","P2": "500","P3": "850"}],
    "Schedules" : {"Days":5,"shiftsperday":3}
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
    EPM = ""
    FPM = ""
    
    for Mkey,Mvalue in products['Type'].items() :
        if (MachinesCount[Mvalue] == 0) :
            EPM = Mkey
    
        if (MachinesCount[Mvalue] > 1) :
            FPM = Mkey
    


    if (EPM != "" and FPM != "") :
        products['Type'][EPM] = products['Type'][FPM]

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
                            MachinesCount[products['Type'][j]] = MachinesCount[products['Type'][j]] - 1
                        
                        MachineCheck = 1
                    k+=1
                
            # else : 
                # print(j,products['Name'],len(products['Type']),products['Type'][j + 1],products['Type'][len(products['Type'])])
                # products['Type'][len(products['Type'])] = products['Type'][j + 1]
        j+=1

dfs = pd.DataFrame(MachineNames)
df1_transposed = dfs.T
dxy = pd.DataFrame(df1_transposed.values, columns = list(df1_transposed.columns), index = [i[-2:] for i in list(df1_transposed.index)])
print(dxy)
