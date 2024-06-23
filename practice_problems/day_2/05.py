n = int(input("The number of keys you want to have in your dictionary: "))
key1 = []
key2 = []
for i in range (1,n+1):
    k = input(f"Input the key {i} of the dictionary: ")
    key1.append(k)
    v = input(f"Input the value of the key {i} : ")
    key2.append(v)
# k1 = input("Input the 1st key of the dictionary: ")
# k2 = input("Input the 2nd key of the dictionary: ")
mydict = dict(zip(key1,key2))
key = input("Input the key of which you want to print the value: ")
print(mydict)
if (key in mydict.keys()):
    print(mydict[key])
else:
    print("key not found")
