def tax(x):
    if x > 100000:
        tax = x*15 / 100
    elif x > 50000 and x <= 100000:
        tax = x*10 / 100
    else:
        tax = x*5 / 100

    return int(tax)


price = int(input("Enter the bike price : "))

print(f"the amount of tax to be paid is {tax(price)}")
