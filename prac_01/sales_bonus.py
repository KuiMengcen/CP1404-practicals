"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

MINIMUM_SALE = 0
MAXIMUM_SALE = 1000
MINIMUM_DISCOUNT = 0.1
MAXIMUM_DISCOUNT = 0.15


sales = float(input("Enter sales:$"))
while sales >= MINIMUM_SALE:
    if sales < MAXIMUM_SALE:
        bonus = MINIMUM_DISCOUNT
    else:
        bonus = MAXIMUM_DISCOUNT
    print("Bonus = $", int(sales * bonus),sep="")
    sales = float(input("Enter sales:$"))