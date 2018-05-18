#This python file aims to finish step 3 in our solution

import re
import json
from pprint import pprint


# Clean a string
def removeUnusedChar(actionList,actionLen):
    cleanActionList = []
    for x in range(0, actionLen):
        effectElement = actionList[x]['action']
        s = (effectElement[effectElement.index("effect") + len("effect"):])[:-1] #Remove the last line because it's useless
        cleanActionList.append(s)
    return cleanActionList

# Contains substring
def containsSub(actionString,actionSubString):
    if actionSubString in actionString:
        return True
    else:
        return False

# Getting the initial predicates
fileName1 ='pddlproblem.json'
with open(fileName1) as f1:
    init = json.load(f1,encoding = 'utf-8')
initStage = init[0]['init']

#Getting the api solution
fileName2 = 'output.json'
with open(fileName2) as f2:
    solutionJson = json.load(f2,encoding = 'utf-8')

#Getting the list of Actions
actionList = solutionJson['result']['plan']
actionLen = len(actionList)
cleanActionList = removeUnusedChar(actionList,actionLen)

#Patterns that will be used for matching
otPattern = re.compile(r'on-table\s\w')
clPattern = re.compile(r'clear\s\w')
onPattern = re.compile(r'on\s\w\s\w')
afPattern = re.compile(r'arm-free')
ahPattern = re.compile(r'holding\s\w')

content=[]
result = {}
for x in range(0, actionLen):

    checkList = []
    addActionList = {}
    addActionList['add'] = []
    removeActionList = {}
    removeActionList['remove'] = []
    ot_name = otPattern.findall(cleanActionList[x])
    cl_name = clPattern.findall(cleanActionList[x])
    on_name = onPattern.findall(cleanActionList[x])
    af_name = afPattern.findall(cleanActionList[x])
    ah_name = ahPattern.findall(cleanActionList[x])

    for ot in ot_name:
        data_object = {}
        data_object["name"] = ot.split()[0]
        data_object["objectNames"] = []
        data_object["objectNames"].append(ot.split()[1])
        checkList.append(data_object)
    for cl in cl_name:
        data_object = {}
        data_object["name"] = cl.split()[0]
        data_object["objectNames"] = []
        data_object["objectNames"].append(cl.split()[1])
        checkList.append(data_object)
    for on in on_name:
        data_object = {}
        data_object["name"] = on.split()[0]
        data_object["objectNames"] = []
        data_object["objectNames"].append(on.split()[1])
        data_object["objectNames"].append(on.split()[2])
        checkList.append(data_object)
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
        checkList.append(data_object)
    for ah in ah_name:
        data_object = {}
        data_object["name"] = ah.split()[0]
        data_object["objectNames"] = []
        data_object["objectNames"].append(ah.split()[1])
        checkList.append(data_object)

    for var in checkList:
        if containsSub(initStage,var) :
            removeActionList['remove'].append(var)
        else:
            addActionList['add'].append(var)

    result['item']=initStage
   # result['remove'] = removeActionList
   # result['add'] = addActionList
    content.append(result)
    content.append(removeActionList)
    content.append(addActionList)

    for addVar in addActionList['add']:
        initStage.append(addVar)
    for rmVar in removeActionList['remove']:
        initStage.remove(rmVar)


pprint(content)
with open('task3.json', 'w') as outfile:
    json.dump(content, outfile)

print("JSON file created successfully")
