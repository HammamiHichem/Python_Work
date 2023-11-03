wallet = 5000
ordinateur_price = 1000
new_wallet = wallet - ordinateur_price
if ordinateur_price > 1500: 
    print("Je ne peux pas acheter l'ordinateur")
else : 
    print("je peux acheter l'ordinateur")
print(f"Reste dans mon porte monais : {new_wallet} €")
text = ("L'achat est possible", "l'achat n'est pas possible")[ordinateur_price <= 1800]
print(text)