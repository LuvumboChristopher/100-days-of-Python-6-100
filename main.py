username = input("what is your username? :")
password = input("what is your password? :")

realUsername = "admin"
realPassword = "azertyuiop"

if username == realUsername and password == realPassword:
  print("Welcome", username)
elif username != realUsername:
  print("Unknow username")
elif username == realUsername and password != realPassword:
  print("Wrong password, try again")
else:
  print("Please enter a alid username and password")
