amount = int(input())
if amount >= 6769:
    quantity = amount // 6769
    if quantity > 1:
        print(str(quantity) + " sheep")
    else:
        print("1 sheep")
elif amount >= 3848:
    quantity = amount // 3848
    if quantity > 1:
        print(str(quantity) + " cows")
    else:
        print("1 cow")
elif amount >= 1296:
    quantity = amount // 1296
    if quantity > 1:
        print(str(quantity) + " pigs")
    else:
        print("1 pig")
elif amount >= 678:
    quantity = amount // 678
    if quantity > 1:
        print(str(quantity) + " goats")
    else:
        print("1 goat")
elif amount >= 23:
    quantity = amount // 23
    if quantity > 1:
        print(str(quantity) + " chickens")
    else:
        print("1 chicken")
else:
    print("None")