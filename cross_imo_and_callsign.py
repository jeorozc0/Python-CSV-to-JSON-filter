import json
import sys
if len(sys.argv) < 2:
   print("USAGE: cat <LIST_OF_VESSEL> | {} <IMO_TO_CALLSIGN> ".format( sys.argv[0]))
   sys.exit()
input_filename = sys.argv[1]

imo_callsign = {}
#Reads and creates hashmap
with open(input_filename, 'r') as imo_to_callsign:
   for line in imo_to_callsign:
      imo_type = line.split()
      imo_callsign[imo_type[0]] = imo_type[1]

#Reads from standard input
   for line in sys.stdin:
      vessel = {}
      list_of_fields = line.split(';')
      for field in list_of_fields:
         key, value = field.split('|') #Split again the list of already splited values
         if key == 'IMO number' and value in imo_callsign:
            vessel['Callsign'] = imo_callsign[value] #Compares values in imo_callsign hashmap and adds them in vessel object
         vessel[key] = value
         if key == 'Description' in vessel:
            del vessel['Description']
         if key == 'Seafarers worked on':
            del vessel['Seafarers worked on']
         
      print(json.dumps(vessel))

   

 


        





