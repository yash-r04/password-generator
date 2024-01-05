import random 

print ("---random password generator-----")

alphac=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
alphal =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
digit = ['0','1','2','3','4','5','6','7','8','9']
special_char=['!','@','#','$','%','&','*','-','_']

length = int(input("enter the length of the password: "))

def password_gen(lenght):
    all_characters = alphac + alphal+ digit + special_char
    
    password = ''.join(random.choice(all_characters) for _ in range(length))
    print("generated password is"  + password)
    
password_gen(length) 