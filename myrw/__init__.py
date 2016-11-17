import json
import os
import myrw

path = os.path.dirname(myrw.__file__) + '/json/province.json'

def hello():
    with open(path) as json_data:
        data = json.load(json_data)
    return json.dumps({'Data': data})