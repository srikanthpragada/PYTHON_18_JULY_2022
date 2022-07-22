# Take qty and price and display net amount

price = int(input("Enter price :"))
qty = int(input("Enter qty : "))

if qty >= 3:
    price = price * .6
elif qty == 2:
    price = price * .7
else:
    price = price * .8

amount = price * qty
print(amount)

