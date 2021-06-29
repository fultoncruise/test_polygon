def simply_interest(n):
    def interest(x):
        return x*(100 + n)/100
    return interest

normale_rate = simply_interest(1.0)
extra_rate = simply_interest(2.5)
credit_card = simply_interest(10.0)

load = float(input("Please enter your desire load: "))
print(normale_rate(load))
print(extra_rate(load))
print(credit_card(load))
