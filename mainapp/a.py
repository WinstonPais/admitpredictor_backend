import json;
def getJsonData(filename):
    return json.load(open(filename,))

data = getJsonData('UniData.json')

print([round((float(item["Rating"])+5)/20,2) for item in data])