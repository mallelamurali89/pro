from django.shortcuts import render,HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from testapp.serializers import NameSerializer
from collections import defaultdict
import pandas as pd
import json
from django.http import JsonResponse

# Create your views here.
class TestAPIView(APIView):
    def get(self,request,pk=None,*args,**kwargs):
        print(pk)
        return Response({'msg':'Hi Welcome'})
    def post(self,request,*args,**kwargs):
        serializer=NameSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.data.get('name')
        return Response({'my name is ':name})
class ProAPIView(APIView):
    def get(self,request,*args,**kwargs):
        # data = open('templates/testapp/2.json').read() #opens the json file and saves the raw contents
        # jsonData = json.dumps(data) #converts to a json structure
        # with open("templates/testapp/2.json", 'r') as jsonfile:
        # s1 = json.dump(data)
        # payload = json.load(data)
        # f = open('templates/testapp/2.json')
        # payload = json.load(f)
    # quit()
        # return JsonResponse(jsonData)
        # print(data)
        payload = {
            "Products":[
                {"Name":"P1", "Dies":"2", "Shifts":"10","Type":{0:"M1",1:"M2"},"Demand":"8000"},
                {"Name":"P2", "Dies":"2", "Shifts":"10","Type":{0:"M2",1:"M3"},"Demand":"4500"},
                {"Name":"P3", "Dies":"3", "Shifts":"16","Type":{0:"M1",1:"M3"},"Demand":"5000"}
                ],
            "Machines":[
                {"Name":"M1","Type":"1", "NoOfMachines":"1"},
                {"Name":"M2","Type":"2", "NoOfMachines":"2"},
                {"Name":"M3","Type":"3", "NoOfMachines":"3"}
            ],
            "Inventory":[{"P1": "150","P2": "250","P3": "350"}],
            "dispatch": [{"P1": "700","P2": "500","P3": "850"}],
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

        # dfs = pd.DataFrame(MachineNames)
        # df1_transposed = dfs.T
        # parsed = json.loads(df1_transposed)
        return Response(MachineNames)
        # dxy = pd.DataFrame(df1_transposed.values, columns = list(df1_transposed.columns), index = [i[-2:] for i in list(df1_transposed.index)])
        # geeks_object = dxy.to_html()
        # return render(request,'testapp/app.html',{'form':dxy.to_html()})
        # return HttpResponse(geeks_object)