for x in range(int(input())):
    rate, amount = float(input()), float(input())
    pretax_price = amount / (1.0 + rate/100)
    #tax_amount = pretax_price * rate

    print(f"On your ${amount:.2f} purchase, the tax amount was ${round(amount - pretax_price, 2):.2f}")
