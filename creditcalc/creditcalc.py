import math


def what_to_calculate():
    print('What do you want to calculate?')
    print('type "n" for number of monthly payments,')
    print('type "a" for annuity monthly payment amount,')
    print('type "p" for loan principal:')
    return input()


def period_to_repay():
    print("Enter the loan principal:")
    loan_principal = int(input())
    print("Enter the monthly payment:")
    monthly_pay = int(input())
    print("Enter the loan interest:")
    interest = float(input())
    i = interest / 1200
    period = math.ceil(math.log(monthly_pay / (monthly_pay - i * loan_principal), 1 + i))
    print(period)
    years = math.floor(period / 12)
    months = period % 12
    desc_years = 'year' if years == 1 else 'years'
    desc_months = 'month' if months == 1 else 'months'
    if years > 0 and months > 0:
        print(f"It will take {years} {desc_years} and {months} {desc_months} to repay this loan!")
    elif years == 0 and months > 0:
        print(f"It will take {months} {desc_months} to repay this loan!")
    elif years > 0 and months == 0:
        print(f"It will take {years} {desc_years} to repay this loan!")
    else:
        print("What? Periods = 0?")


def monthly_payment():
    print("Enter the loan principal:")
    loan_principal = int(input())
    print("Enter the number of periods:")
    periods = int(input())
    print("Enter the loan interest:")
    interests = float(input())
    i = interests / 1200
    annuity_payment = math.ceil(loan_principal * ((i * pow(1 + i, periods)) / (pow(1 + i, periods) - 1)))
    print(f"Your monthly payment = {annuity_payment}!")


def mount_to_repay():
    print("Enter the annuity payment:")
    annuity_payment = float(input())
    print("Enter the number of periods:")
    periods = int(input())
    print("Enter the loan interest:")
    interests = float(input())
    i = interests / 1200
    loan_principal = math.trunc(annuity_payment / ((i * pow(1 + i, periods)) / (pow(1 + i, periods) - 1)))
    print(f"Your loan principal = {loan_principal}!")


def output_value(mode):
    if mode == 'n':
        period_to_repay()
    elif mode == 'a':
        monthly_payment()
    elif mode == 'p':
        mount_to_repay()
    else:
        print("Incorrect mode")


def main():
    mode = what_to_calculate()
    output_value(mode)


main()
