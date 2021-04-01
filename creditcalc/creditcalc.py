import math


def what_to_calculate():
    print('What do you want to calculate?')
    print('type "m" - for number of monthly payments,')
    print('type "p" - for the monthly payment:')
    return input()


def mount_to_repay(loan_principal):
    print("Enter the monthly payment:")
    monthly_pay = int(input())
    period = math.ceil(loan_principal / monthly_pay)
    description = 'month' if period == 1 else 'months'
    print(f"\nIt will take {period} {description} to repay the loan")


def monthly_payment(loan_principal):
    print("Enter the number of months:")
    periods = int(input())
    regular_pay = math.ceil(loan_principal / periods)
    last_pay = loan_principal - (periods - 1) * regular_pay
    if regular_pay == last_pay:
        print(f'Your monthly payment = {regular_pay}')
    else:
        print(f'Your monthly payment = {regular_pay} and the last payment = {last_pay}.')


def output_value(mode, loan_principal):
    if mode == 'm':
        mount_to_repay(loan_principal)
    elif mode == 'p':
        monthly_payment(loan_principal)
    else:
        print("Incorrect mode")


def main():
    print("Enter the loan principal:")
    loan_principal = int(input())
    mode = what_to_calculate()
    output_value(mode, loan_principal)


main()
