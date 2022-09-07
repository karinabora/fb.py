
print("create a face book account::")
n1=input("enter first name::")
n2=input("enter middle name::")
n3=input("enter last name::")
if n1>='a' and n1<='z' or n1>='A' and n1<='Z' or n2>='a'and n2<='z' or n2>='A'and n2<='Z'or n3>='a'and n3<='z'or n3>='A'and n3<='Z':
    print("ok")
    print("cklick on next")
    m=input("enter the mail::")
    if m=='digit'or 'special character'or 'alphabet':
        print(m+"@gmail.com")
        print("ok")
        print("click on next")
        ph=int(input("enter the phone number::"))
        if ph>=1000000000 and ph<=9999999999:
            print("correct")
            print("ok")
            print("click on next")
            g=input("enter the gender::")
            if g=="male" or "female":
                print("click on next")
                d=input("enter the date of birth::")
                if d=='digit' or 'special character':
                    print("ok")
                    print("click on next")
                    p=input("enter the password::")
                    if p=='digit' or 'special character' or 'alphabet':
                        print("confirm password")
                        print("ok")
                        privacy=input("enter the privacy terms::")
                        if privacy=="i agree" or privacy=="no":
                            print("ok")
                            print("your gmail account has craeted")
                        else:
                            print("disagree")
                    else:
                        print("not defined")
                else:
                    print("enter correct date of birth")
            else:
                print("custom")
        else:
            print("enter valid phone number")
    else:
        print("enter valid mail id")
else:
    print("enter valid name")


# https://docs.google.com/document/d/1Gf8i_7WRxQfGtI-MDZepCm2vrE8RwnEzVwe9UJc32mg/edit