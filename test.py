from pprint import pprint 
import json

f = open('input.json')
data = json.load(f)
total_no_of_machine_counts = 0
total_no_of_dies = 0
total_no_of_demand_per_schedule = 0
total_no_of_opening_inventory = 0
tot_shifts = 0
for i in data['Machines']:
        total_no_of_machine_counts += i['count']
for i in data['Products']:
        total_no_of_dies += i['Dies']
        total_no_of_demand_per_schedule += i['Demand']
for i in data['Inventory']:
        total_no_of_opening_inventory += i['count']
for i in data['Shifts']:
        tot_shifts += i['Shits']
tot_no_of_shifts = tot_shifts * total_no_of_machine_counts
f.close()


print("total_no_of_machine_counts =>",total_no_of_machine_counts)
print("total_no_of_dies =>",total_no_of_dies)
print("total_no_of_demand_per_schedule =>",total_no_of_demand_per_schedule)
print("tot_no_of_shifts =>",tot_no_of_shifts)
print("total_no_of_opening_inventory =>",total_no_of_opening_inventory)
print("total_days_shifts =>",tot_shifts)
machines_array = []
machines_array_list = {}

for i in data['Machines']:
        if i['count'] == 1:
                # print(i['name'],1)
                temp = "{}{}".format(i['name'],  1)
                machines_array.append(temp)
        elif i['count'] > 1:
                for x in range(i['count']):
                        # print(i['name'],x+1)
                        temp = "{}{}".format(i['name'],  x+1)
                        machines_array.append(temp)
print(machines_array)

for i, val in enumerate(machines_array):
        machines_array_list[val]=["" for column in range(tot_shifts)]
        # machines_array_list[val]=[{column+1:"0"} for column in range(tot_shifts)]
       
pprint(machines_array_list)

if total_no_of_dies <= total_no_of_machine_counts:
        dies_count = total_no_of_dies
else:
        dies_count = total_no_of_machine_counts
        diff_of_die_and_machines = total_no_of_dies-total_no_of_machine_counts
# print("diff_of_die_and_machines =>",diff_of_die_and_machines)
print("heloooooooooooooooooooooooooooooooooooo")
pro_dies = {}
dict1={}
for i in data['Products']:
        # temp1 = int(i['NShifts']/i['Dies'])
        for x in range(i['Dies']):
                # print(i['name'],"d",x+1)
                tem = "{} d{}".format(i['name'],x+1)
                for key,val in machines_array_list.items():
                        # pass
                        print(val)
                        # print(machines_array_list[key])
                        # print(len(val))
                        # print(machines_array_list[str(val)])
                        for xkey,xvalue in enumerate(val):
                                print(xkey)
                                # machines_array_list[val][xkey]=str(tem)
                                # print(machines_array_list[key][xkey])
                                # pass
                                # machines_array_list[key].append()
                                # print(machines_array_list[key])
                        #       machines_array_list[key][val][xkey]=str(tem)  


                
                # pro_dies[tem] = temp1
# print(machines_array_list)

