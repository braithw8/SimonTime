# Karbach, Kristoph
#
# POS program for MinMax
# v1.0.4
# compatible with Python versions 3.4 - 3.7
# source file:
#

# Defined constants
# Nothing
PRICE_SINGLE = 1.00
PRICE_SMALL = 5.00
PRICE_LARGE = 19.00
UPC_SINGLE = 111111
UPC_SMALL = 666666
UPC_LARGE = 242424
HST_RATE = 0.13


def display_welcome():
    #simple welcome greeting
    x = "Welcome to MinMax!"
    print(x)

def get_barcode():
    prompt = ''
    Q_SINGLES = 0
    Q_SMALLS = 0
    Q_LARGES = 0
    subtotal = 0
    total_tax = 0
    total = 0
    total_rounded = 0

    while prompt != '0':
        prompt = input("Please enter barcode and press enter. Enter 0 when finished. ")

        if int(prompt) == UPC_SINGLE:
            Q_SINGLES = Q_SINGLES + 1
            subtotal = calculate_subtotal(Q_SINGLES, Q_SMALLS, Q_LARGES)
            total_tax, total, total_rounded = calculate_total_bill(subtotal)
        elif int(prompt) == UPC_SMALL:
            Q_SMALLS = Q_SMALLS + 1
            subtotal = calculate_subtotal(Q_SINGLES, Q_SMALLS, Q_LARGES)
            total_tax, total, total_rounded = calculate_total_bill(subtotal)
        elif int(prompt) == UPC_LARGE:
            Q_LARGES = Q_LARGES + 1
            subtotal = calculate_subtotal(Q_SINGLES, Q_SMALLS, Q_LARGES)
            total_tax, total, total_rounded = calculate_total_bill(subtotal)

        elif prompt == '0':
            break
        else:
            print("Not a valid input, please input UPC code.")

    display_total_bill(subtotal, total_tax, total, total_rounded)

    return total_rounded





def calculate_subtotal(number_of_singles: int, number_of_smalls: int, number_of_larges:int ) -> float:
    """Return the subtotal amount of money the customer owes after inputting the number of singles, smalls and larges.
    >>> calculate_subtotal(2, 2, 1)
    31.0
    """
    subtotal_before_tax = (number_of_singles * PRICE_SINGLE) + (number_of_smalls * PRICE_SMALL) + (number_of_larges * PRICE_LARGE)

    return subtotal_before_tax

def calculate_total_bill(subtotal_before_tax: float) -> float:
    """Take the subtotal_before_tax and return the total tax, total bill before rounding
    and the total rounded bill. Print the running total.
    >>> calculate_total_bill(31.0)
    Subtotal is: 31.00
    Tax is: 4.03
    Your total is: 35.03
    Please pay: 35.05
    """
    total_tax = subtotal_before_tax * HST_RATE
    total_before_rounding = subtotal_before_tax + (total_tax)
    total_bill = round(total_before_rounding * 2, 1) / 2.0

    print("Your current total is", format(total_bill, '.2f'))

    return total_tax, total_before_rounding, total_bill

def display_total_bill(sub: float, tax: float, total: float, total_rounded: float) -> str:

    print("Subtotal is:", format(sub, '.2f'))
    print("Tax is:", format(tax, '.2f'))
    print("Your total is:", format(total, '.2f'))
    print("Please pay:", format(total_rounded, '.2f'))

def get_amount_tendered(total):
    cash = 0

    while cash < total:
        cash = float(input("How much cash is given (enter a float)? Enter 0 to quit "))

        if cash == 0.0:
            print ("Thanks for stopping at MinMax, we hope to see you again.")
            break
        elif cash < total:
            print("Sorry insufficient funds, please try again.")

    return cash

def display_change(cash, total):
    change = cash - total

    print("Return this money to the customer:", format(change, '.2f'))
    print("Thanks for shopping at MinMax!")

if __name__ == "__main__":
    display_welcome()
    total_bill = get_barcode()
    amount_tendered = get_amount_tendered(total_bill)

    if amount_tendered != 0.0:
        display_change(amount_tendered, total_bill)
