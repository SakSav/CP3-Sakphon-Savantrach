username = input("username : ")
password = input("password : ")

while username != "admin" or password != "1234" :
    print("Try again !")
    username = input("username : ")
    password = input("password : ")

print("Welcome Admin.")