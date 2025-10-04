import os
user=input("enter file name")
if os.path.exists(user):
    print("exist file")
else:
    print("not exist")    