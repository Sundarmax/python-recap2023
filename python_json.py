import json
# loads - > convert json object to python object (dict)
# dumps - > convert python object to json string
# JSON string: 

# Multi-line string 
data = """{ 
    "Name": "Jennifer Smith", 
    "Contact Number": 7867567898, 
    "Email": "jen123@gmail.com", 
    "Hobbies":["Reading", "Sketching", "Horse Riding"] 
    }"""

print(type(data))
out = json.loads(data)
print(type(out))
json_out = json.dumps(out)
print(json_out,type(json_out))

# load  -> take input file object and convert to python dict
# dump  -> convert python object to json and store it in the file object

dic = {"name": "sundar"}
with open("data.json","w") as file_obj:
    json.dump(dic,file_obj)

with open("data.json","r") as file_obj:
    print(json.load(file_obj))
