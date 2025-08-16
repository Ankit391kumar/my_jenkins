# append

data = ["ankit", "shlok", "Rajat"] # data list
data.append("akansh") # an element
print(data)
# extend
data = ["ankit", "shlok", "Rajat"] # data list
data.extend(["akansh", "kannu"]) # to add multiple element we need to define in the ([])
print(data)
# remove
data = ["ankit", "shlok", "Rajat"] # data list
data.remove("ankit") # an element
print(data)

# insert
data = ["ankit", "shlok", "Rajat"] # data list
data.insert(0, 2) # we need to pass index and the element
print(data)


# del===> used for remove all elements from the list
data = ["ankit", "shlok", "Rajat",] # data list
# del data[1:2]
# data.clear()
data = None
print(data)
# index
data = [ 1, 3, 5 ,4, 5, 6]
data_index = data.index(5)
print(data_index)
# count ===> print the no of timens velue is repeated
data = [ 1, 3, 5 ,4, 5, 6]
data_count = data.count(5)
print("data_count of 5 is :", data_count)
# sort # sort(reverse = True)
values = [1, 4, 5, 7, 8, 3, 5, 7,]
values.sort()
print("sort():", values)
values.sort(reverse=True)
print("sort():", values)
verv = sorted(values)
print(verv)
# reverse
data = ["abc", "def","ghi"]
data.reverse()
print("reverse():", data)
#copy #reverse a shallo copy of the list
data = ["abc", "def","ghi"]
print(id(data))
data.copy()
print("copy()", data)
print(id(data))
#print(type(data_copy))
# deep copy

versions = ["1.0", "1.1", "1.2"]
versions.clear()
print(versions)


event = ["start", "stop", "restart", "terminate"]
event.remove("terminate")
print(event)


resources = [ 50, 100, 250]
if resources[0] == 100:
    print("first element equals to 50")
else:
    print("not equal to 50")

# logs = ["error.log", "access.log"]
# copy_logs = logs.copy()
# print(copy_logs)


# tasks = ["deploy", "test", "monitor"]
# positions= tasks.index("deploy")
# print(positions)

regions1 = ["us-east", "us-west"]
regions2 = ["eu-central"]
regions1.append(regions2)
print(regions1)


metrics = [100, 200, 100, 300, 100]
cou = metrics.count(100)
print(cou)


nodes = ["node1", "node2", "node3"]
nodes.insert(0, "node0")
print(nodes)


ports = [80, 443, 8080]
ports.pop(1)
print(ports)


servers = ["web1", "web2"]
servers.append("web0")
print(servers)



