#encoding:utf-8
import json
test_dict = {
    "Model": [
        "Tool_a",
        "Tool_b",
        "Tool_c",
    ],
    "Render": [
        "Tool_d",
        "Tool_e",
        "Tool_f",
    ],
    "Rig": [
        "Tool_h",
    ],

}

# dump python object to json string
test_json_str = json.dumps(test_dict)
# write json string into a file
with open("D:/CK_Dev/Maya_Dev/Tool_Dev/笔记/实战课笔记/劲爆羊/test.json","w") as json_file:
    json_file.write(test_json_str)
    print(json_file)

# with open("D:/CK_Dev/Maya_Dev/Tool_Dev/笔记/实战课笔记/劲爆羊/test.json","r") as json_file:
#     json_str = json_file.read()
#     test_dict = json.loads(json_str)
#     print (test_dict)