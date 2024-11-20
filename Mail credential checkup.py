
email = input("Enter Email: ")

if len(email)>= 6:                            # topikmulani@gmail.com
    if email.count("@") == 1 and email.count(".") == 1:
        if email[0] != "_":
            if len(email[email.index(".")+1:]):
                    username = email[:email.index("@")]
                    company = email[email.index("@")+1:email.index(".")]
                    domain = email[email.index(".")+1:]
                    p = False
                    for i in username:
                        if i.isalnum():
                            pass
                        elif i == "_":
                            pass
                        else:
                            p = True
                    for j in company:
                        if j.isalnum():
                            pass
                        else:
                            p =True
                    for k in domain:
                        if k.isalpha():
                            pass
                        if k.islower():
                            pass
                        else:
                            p = True
                    if p == False :
                        print("Valid Email Id")
                    else:
                        print("Invalid input 5")
            else:
                print("Invalid input 4")
        else:
            print("Invalid Input 3")
    else:
        print("Invalid Input 2")
else:
    print("Invalid input 1")
