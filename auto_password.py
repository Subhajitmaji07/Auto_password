import random
import string

pass_len=int(input("Enter the length of  password: "))
#creating the password
lower=string.ascii_lowercase
upper=string.ascii_uppercase
num=string.digits
symbol=string.punctuation


all= lower+upper+num+symbol

temp=random.sample(all,pass_len)
password="".join(temp)
print(password)

#save password in text file
save=input("Save password to file?(y/n): ")

if save=="y":
    web=input("Enter the website name: ")
    
    with open("password.txt","a") as f:
        f.write(str(web)+"\t\t\t")
        f.write(str(password))
        f.write("\n")
        print("password save to 'password.txt'file") 