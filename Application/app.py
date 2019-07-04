users = []
posts = []

def loginSuccess(email):
    print("""
    1. Post Something
    2. View Profile
    3. Edit Profile
    4. Delete Profile
    """)

def post(email):
    p = {"post":"Hello this is ram","date":'12/2/3',"email":email}
    posts.append(p)

def viewProfile(email):
    pass

def editProfile(email):
    pass

def updateProfile(email):
    pass

def deleteProfile(email):
    pass

def login():
    email = input("Enter email : ")
    pwd = input("Enter password : ")
    for i in range(len(users)):
        if users[i]['email'] == email and pwd == users[i]['pwd']:
            print("Login Success")
            loginSuccess(email)
            break
    else:
        print("Login Failed..")

def register():
    name = input("Enter your name : ")
    flag = True
    while flag:
        email = input("Enter your email : ")
        if len(users) >= 1:
            for i in range(len(users)):
                if users[i]['email'] == email:
                    print("EmailID Already Exist")
                    break
            else:
                flag = False
        else:
            flag = False

    pwd = input("Enter your pwd : ")
    city = input("Enter your city : ")

    user = {"name":name,"email":email,"pwd":pwd,"city":city}
    users.append(user)
    for item in users:
        print(item)

def main():
    print("""
    1. Login
    2. Register
    """)
    ch = input("Enter your choice : ")
    todo = {
        "1" : login,
        "2" : register
    }
    todo.get(ch)()

while True:
    main()