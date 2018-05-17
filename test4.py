import re
import json
from pprint import pprint

otPattern = re.compile(r'on-table\s\w')
clPattern = re.compile(r'clear\s\w')
onPattern = re.compile(r'on\s\w\s\w')
afPattern = re.compile(r'arm-free')
ahPattern = re.compile(r'holding')
andPattern = re.compile(r'and')




file_name ='problem_blocks.pddl'

f = open(file_name)
st = f.read()

ot_name = otPattern.findall(st)
cl_name = clPattern.findall(st)
on_name = onPattern.findall(st)
af_name = afPattern.findall(st)
ah_name = ahPattern.findall(st)

init_found = re.search('init(.+?)\n', st).group(1)
init_ot_name = otPattern.findall(init_found)
init_cl_name = clPattern.findall(init_found)
init_on_name = onPattern.findall(init_found)
init_af_name = afPattern.findall(init_found)
init_ah_name = ahPattern.findall(init_found)




def getLastLine(filename, maxLineLength):
    fp= open(filename, "rb")
    fp.seek(-maxLineLength-1, 2) # 2 means "from the end of the file"
    return fp.readlines()[-1]

line = getLastLine(file_name,80)

decoded_line=line.decode('utf-8')
goal_found = decoded_line
goal_ot_name = otPattern.findall(goal_found)
goal_cl_name = clPattern.findall(goal_found)
goal_on_name = onPattern.findall(goal_found)
goal_af_name = afPattern.findall(goal_found)
goal_ah_name = ahPattern.findall(goal_found)
goal_and_name = andPattern.findall(goal_found)
f.close()

init_data = []
goal_data = []
goal_condition =[]
goal_final_data = []
final_problem_json= []

for ot in init_ot_name:
    data_object ={}
    data_object["name"] = ot.split()[0]
    data_object["objectNames"] =[]
    data_object["objectNames"].append(ot.split()[1])
    init_data.append(data_object)
for cl in init_cl_name:
    data_object = {}
    data_object["name"] = cl.split()[0]
    data_object["objectNames"] =[]
    data_object["objectNames"].append(cl.split()[1])
    init_data.append(data_object)
for on in init_on_name:
    data_object = {}
    data_object["name"] = on.split()[0]
    data_object["objectNames"] =[]
    data_object["objectNames"].append(on.split()[1])
    data_object["objectNames"].append(on.split()[2])

    init_data.append(data_object)
for af in init_af_name:
    data_object = {}
    data_object["name"] = af.split()[0]
    if len(af) > 8:
        if af.split()[1] is None:
            data_object["objectNames"] = ["No objects"]
        else:
            data_object["objectNames"] = []
            data_object["objectNames"].append(af.split()[1])

    else:
        data_object["objectNames"] = ["No objects"]
    init_data.append(data_object)
for ah in init_ah_name:
    data_object = {}
    data_object["name"] = ah.split()[0]
    if len(ah) > 8:
        if ah.split()[1] is None:
            data_object["objectNames"] = ["No objects"]

        else:
            data_object["objectNames"] = []
            data_object["objectNames"].append(ah.split()[1])
    else:
        data_object["objectNames"] = ["No objects"]
    init_data.append(data_object)






for val in goal_and_name:
    data_object ={}

    data_object["objectNames"] = []
    data_object["objectNames"].append(val.split()[0])

    goal_condition.append(data_object)
for ot in goal_ot_name:
    data_object ={}

    data_object["name"] = ot.split()[0]
    data_object["objectNames"] = []
    data_object["objectNames"].append(ot.split()[1])
    goal_data.append(data_object)
for cl in goal_cl_name:
    data_object = {}

    data_object["name"] = cl.split()[0]
    data_object["objectNames"] = []
    data_object["objectNames"].append(cl.split()[1])
    goal_data.append(data_object)
for on in goal_on_name:
    data_object = {}

    data_object["name"] = on.split()[0]
    data_object["objectNames"] = []
    data_object["objectNames"].append(on.split()[1])
    data_object["objectNames"].append(on.split()[2])

    goal_data.append(data_object)
for af in goal_af_name:
    data_object = {}

    data_object["name"] = af.split()[0]

    if len(af) > 8:
        if af.split()[1] is None:
            data_object["objectNames"] = ["No objects"]
        else:
            data_object["objectNames"] = []
            data_object["objectNames"].append(af.split()[1])

    else:
        data_object["objectNames"] = ["No objects"]
    goal_data.append(data_object)
for ah in goal_ah_name:
    data_object = {}

    data_object["name"] = ah.split()[0]
    if len(ah) > 8:
        if ah.split()[1] is None:
            data_object["objectNames"] = ["No objects"]

        else:
            data_object["objectNames"] = []
            data_object["objectNames"].append(ah.split()[1])
    else:
        data_object["objectNames"] = ["No objects"]
    goal_data.append(data_object)



goal_data_object ={}
goal_data_object["goal"] = goal_data
goal_data_object["goal-condition"] = goal_condition








for ot in ot_name:
    data_object ={}
    data_object["name"] = ot.split()[0]
    data_object["objectNames"] = []
    data_object["objectNames"].append(ot.split()[1])
    init_data.append(data_object)
for cl in cl_name:
    data_object = {}
    data_object["name"] = cl.split()[0]
    data_object["objectNames"] = []
    data_object["objectNames"].append(cl.split()[1])
    init_data.append(data_object)
for on in on_name:
    data_object = {}
    data_object["name"] = on.split()[0]
    data_object["objectNames"] = []
    data_object["objectNames"].append(on.split()[1])
    data_object["objectNames"].append(on.split()[2])

    init_data.append(data_object)
for af in af_name:
    data_object = {}
    data_object["name"] = af.split()[0]
    if len(af) > 8:
        if af.split()[1] is None:
            data_object["objectNames"] = ["No objects"]
        else:
            data_object["objectNames"] = []
            data_object["objectNames"].append(af.split()[1])

    else:
        data_object["objectNames"] = ["No objects"]
    init_data.append(data_object)
for ah in ah_name:
    data_object = {}
    data_object["name"] = ah.split()[0]
    if len(ah) > 8:
        if ah.split()[1] is None:
            data_object["objectNames"] = ["No objects"]

        else:
            data_object["objectNames"] =[]
            data_object["objectNames"].append(ah.split()[1])
    else:
        data_object["objectNames"] = ["No objects"]
    init_data.append(data_object)

init_data_object = {}
init_data_object["init"] = init_data
final_problem_json.append(init_data_object)
final_problem_json.append(goal_data_object)
pprint(final_problem_json)

with open('pddlproblem.json', 'w') as outfile:
    json.dump(final_problem_json, outfile)

print("PDDL to JSON successful")




