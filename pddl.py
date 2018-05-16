
from urllib.request import urlopen
import urllib.request
import json

data = {'domain': open('domain_blocks.pddl', 'r').read(),
        'problem': open('problem_blocks.pddl', 'r').read()}

url = 'http://solver.planning.domains/solve'
req = urllib.request.Request(url)
req.add_header('Content-Type', 'application/json')
json_data = json.dumps(data)
json_data_as_bytes = json_data.encode('utf-8')
req.add_header('Content-Length', len(json_data_as_bytes))
print(json_data_as_bytes)
response = urllib.request.urlopen(req, json_data_as_bytes)

print("some stuff")

result_json = json.load(response)
print(result_json)

with open('output.json', 'w') as outfile:
    json.dump(result_json, outfile)

