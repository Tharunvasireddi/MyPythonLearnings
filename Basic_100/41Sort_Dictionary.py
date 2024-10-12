dict1={"t":1,"a":0,"v":5,"r":2,"b":7,"d":8}
sort_dict=dict(sorted(dict1.items(),key=lambda item:item[1]))
print("sorted dicttionary is : ",sort_dict)