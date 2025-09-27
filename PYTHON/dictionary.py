# dictionary 
# store the data in pairs forms in keys and values form 

# dictional store in key and values form 
# dictionary are unordered 3.7 before but after that version dictionary are ordered 
# dictionary are mutable 
# dynamic -
# dictionary create
# dict_keys([...]) ek view hai jo dictionary ke keys ko dikhata hai, list nahi.

a1={}  # empty string
a={"name":"shashank","age":23,"fruits":["apple","kela"]} # key values pair in strings  
# mutable 
a['price']=100 # iska mtlb hai hmm price name ka ek key bana rehe hai jiske under hmmm value 100 store kar rehe hai 
print(a)

# updated teh values 
a["name"]="krishna"
print(a)
# delete the items 
del a['name']
print(a)

# methods 
profile={
    "name":"shashank","age":25,"salary":50000
    }
# dict.get() gives the values 
age=profile.get("age")
print(age)
# only wants keys 
keys =profile.keys()
print(keys)
# only wants values
values=profile.values()
print(values)

# items
print(profile.items())
# pop methods 
print(profile.pop("salary"))
print(profile)

# popitem 
popitem=profile.popitem()
print(popitem)
print(profile)

# clear 
clear=profile.clear()
print(profile)
# dict comprehension 
squares={x:x*x for x in range(1,6)}
print(squares)
# nested dictionary 
pro={
    "name":"shashank",
    "age":{"age":25,"color":"red"},
}
profiles={
    "name":"shashanksuman",
    "age":24,
    "salary":25000,
    "savings":240000
}
for k in profiles.values(): # k only gives us keys 
    print(k)
for k in profiles.keys():
    print(k)
for k in profiles.items():
    print(k)     
    