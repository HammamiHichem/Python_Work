password = input("Entrez votre mot de passe\n")
len_password = len(password)
if len_password <= 9 : 
    print("Passwored is not valide")
elif 8 < len_password <= 12 :
    print("Password meduim")
else :
    print("password is perfect")