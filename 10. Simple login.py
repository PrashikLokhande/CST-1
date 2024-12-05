data_stores = {
    "rajveer_banna": "7773",
    "rv": "1234"
}

username = input("Enter your username: ")
password = input("Enter your password: ")

if username in data_stores and password == data_stores[username]:
   print("Login succesful!")
else:
   print("Wrong password. ")
       