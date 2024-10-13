def key_present_or_not(my_dict,key):
    if key in my_dict:
        return True
    else :
        return False
dict1={"t":1,"a":0,"v":5,"r":2,"b":7,"d":8}
if key_present_or_not(dict1,"k"):
    print("key is present ")
else :
    print("key is not present ")