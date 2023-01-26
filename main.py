#Assingment Thomas Pauws
#This program shows the orders for each medicine

#json import is needed because Json structure is used
import json
import sys

#Here i open the file with the medicine and create a data dictionary
def get_medicine_list(file_name):
with open(file_name) as f:
medicine = json.load(f)
medicine_list = {}

#Here i define what medicine i can search for
for key, record in medicine["medicine"].items():
medicine_list[record["name"]] = record["rvgnr"]
return medicine_list

#Here i say which medicine is connected to which order list
def get_medicine_order(medicine_name, medicine_list):
if medicine_name in medicine_list:
with open(f"order_{medicine_rvgnr[medicine_name]}.txt", 'r') as f:
print("\n".join(f.readlines()))
else:
print(f"{medicine_name} is not in the listed medicine")

#Here i ask for input and ask if the employee wants to continue
medicine_list = medicine_list('medicine_list.txt')
print("Please tell me the medicine name.")
for query in sys.stdin:
get_medicine_order(query.strip(), medicine_list)
print("Would you like to search for another medicine, otherwise please wwrite exit.")
if query == "exit":
break
#Here I make main more accessible
if __name__ == "__main__":
main()