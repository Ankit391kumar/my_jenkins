node_config = ("node1", "192.168.1.10", 8080)

pos = node_config.index("192.168.1.10")
print(pos)

tags = ("prod", "web", "prod")
coun = tags.count("prod")
print(coun)


versions = ("1.0.0", "1.1.0", "2.0.0")
if versions[0] == "1.0.2":
    print("elm is equal to 1.0.0")
else:
    print("elm not equal to 1.0.0")
    
    
config1 = ("app1", "v1.0")
config2 = ("app1", "v2.0")

if config1 == config2:
    print("both files are same")
else:
    print("both files arn't same")
    
    
resources = (50, 75, 100, 125)
new_resources = (resources[0:5:2])
print(new_resources)

