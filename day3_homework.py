
username=input("Enter your username")
password=input("Enter your password")
print("You registered")   

while True:
 rname=input("Enter your username for log in")
 rpass=input("Enter your password for log in")
 if username==rname and password==rpass:
    print("Log in..wait a minute")
    break
 elif username==rname and password!=rpass:
    print("Error!Wrong password,try again")
    continue
 elif username!=rname and password==rpass:
    print("Error!Wrong username,try again")
    continue
 elif username!=rname and password!=rpass:
    print("Error!Wrong password and username,try again")
    continue

"""

 #extra 

username=input("Enter your username")
password=input("Enter your password")
print("Uye oldunuz")
users={
    'name':username,
    'pass':password
    }

while True:
 rname=input("Enter your username for log in")
 rpass=input("Enter your password for log in")
 inf={
    'rname':rname,
    'rpass':rpass
 }
 if users['name']==inf['rname'] and users['pass']==inf['rpass']:
    print("Log in..wait a minute")
    break
 elif users['name']==inf['rname'] and users['pass']!=inf['rpass']:
    print("Error!Wrong password,try again")
    continue
 elif users['name']!=inf['rname'] and users['pass']==inf['rpass']:
    print("Error!Wrong username,try again")
    continue
 elif users['name']!=inf['rname'] and users['pass']!=inf['rpass']:
    print("Error!Wrong password and username,try again")
    continue

"""