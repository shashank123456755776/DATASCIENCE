# list is datastructure jisme mutiple values alag alag data types store kar sakte hai  
# list is mutable means we can change the values 
# dynamic is nature means we can add or remove the values 
# list is ordered means we can acces the values by index 
# list is indexed i.e all have postion start from indexing 
# list is iterable 

# use 
# jaha data chnage hote rehe hai waha use karte hai list ka 
a =["shashank",23,45.6,True] #diffrent data types
print(a)

# list constructor 
list1=list(("shashank",23,45.6,True)) # double paranthesis and list keyword use kar to ye lsit constructor hai 
print(list1)

# list comprehension and range function 
list2=[i for i in range(1,11)] # ye 1 se 10 tak ke numbers ko list mai store kar dega 
print(list2) 
# range  function 
list3 =list(range(1,11)) # ye bhi 1 se 10 tak ke numbers ko list mai store kar dega 
print(list3)


# list accessing 
print(a[0]) # postive indexing 
# updated the values  menas mutable
a[0]="suman"
print(a)
a[0:3]=2,3,4
print(a)
# concatination of list 
x=[1,2,3]
y=[4,5,6]
print(x+y)
# repeat the list 
print(a*3) # elements ko 3 bar repeat kar ke store ka dega same list mai 
# membership operators # ko bhi elements list mai hai ya ni 
# check =int(input("enter a number to check in list:"))
# if print(check in a):
#    print("found")
# else:
#    print("not found")
#   aliasing of list 
k=[1,2,3,34,5]
m=k  # dono same list ko point kar reha hai 
print(m)
m[0]=100 
print(m) 
print(k)

# isliye we use copy method beacuse change in one does not affect on others 
m=k.copy()
m[0]=2
print(m)
print(k)

# append methods 
k.append(45) # ye last mai 45 ko add kar dega  
# extend methods 
k.extend([5,5,6]) # ye lastv mai 5,5,6 ko add kar dega 
# insert methods 
k.insert(2,100) # particular index mai value ko add kar dega 
print(k)
# remove methods 
k.remove(5) # no need to give index ye directly remove kar dega 
# pop methods  
k.pop(0) # isme indexing pass karna hota hai ye index ke accxording remove karta hai 
k.pop() # ye last wala remove kar dega 
print(k)

# remove and pop diffrences 
# remove mai hmm data pasa karte hai aur pop mai index pass karye hai 

# clear methods 
k.clear() # ye list ko empty kar dega 
# index methods 
e=[1,2,3,4,5,5,5]
print(e.index(5)) # ye first ka index dega ,hmm elemnts pass karte hai 
# count methods 
print(e.count(5)) # ye 5 kitni bar wo bata dega 
# sort methods 
d=[3,1,-1,0,54,25]
d.sort()
print(d)

# sort methods  acending mai list ko change karta dega 
# sorted methods ek naya list bana kar dega 
s=sorted(d)
print(s)

# sort() → original list ko badal deta hai, None return karta hai.

# sorted() → ek nayi list return karta hai, original list same rehti hai.

# reverse methods 
d.reverse() 
print(d)

# finding minimum and maximum values 
a=[2,3,4,5,6,7,8]
print(min(a))
print(max(a))

# finding common elements 
b=[1,2,3]
c=[3,4,5]
set1=set(b) # gives unique values 
set2=set(c)
f=set1.intersection(set2)
print(list(f))

# nested list 
w=[1,2,3,[4,5,6,[7,8,9]]]
print(w)

# list comprehension 
squares =[i**2 for i in range(1,11) if i%2==0]
print(squares)