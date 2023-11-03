age = int(input("how older are you\n"))
question = input("Do you want pop corne\n").lower()
# print("(Yes)\n (No)")
price = 7
price2 = 12
pop_corn = 5
total_price_popcorne = (price + pop_corn)
total_price2_popcorne = (price2 + pop_corn) 
if age <= 16 and question == ("yes"): 
    print (f"You must pay : {total_price_popcorne}")
elif age <= 16 and question == ("no"): 
    print (f"You must pay : {price} ")
elif age > 16 and question == ("yes"): 
    print (f"You must pay : {total_price2_popcorne}")
else : 
    print (f"You must pay : {price2} ")