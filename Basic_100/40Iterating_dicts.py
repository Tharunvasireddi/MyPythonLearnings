dict1={"name":"tharun","age":19,"village":"kothamallempeta"}
#using for loop printing keys
print("keys in the dictionary :",end="")
for i in dict1:
    print(i,end=",")
# using for loop for printing values
print()
print("values in the dictonary are :",end="")
for i in dict1:
    print(i,":",dict1[i],end=",")
#printing keys using dictionry.keys() method
print()
print("keys of dictonary are : ",end="")
for key in dict1.keys():
    print(key,end=",")
#printing values using dictionary.values() method
print()
print("vales of dictioonary is :",end="")
for value in dict1.values():
    print(value,end=",")
#printint keys and values as a pair using dictionary.items() method
print()
print("keys and values are : ")
for key,value in dict1.items():
    print(key,"-->",value)