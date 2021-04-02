import math
import sys
import argparse


def what_to_calculate(args):
    if args.type == "diff" and args.payment:
        return "error"
    if args.payment and args.payment < 0:
        return "error"
    if args.principal and args.principal < 0:
        return "error"
    if args.periods and args.periods < 0:
        return "error"
    if args.interest and args.interest < 0:
        return "error"

    if args.type == "diff":
        return "diff"
    elif args.type == "annuity":
        if args.principal and args.periods and args.interest:
            return "m_pay"
        elif args.payment and args.periods and args.interest:
            return "total_p"
        elif args.principal and args.payment and args.interest:
            return "p_t_p"
        else:
            return "error"
    else:
        return "error"


def diff_payment(args):
    loan_principal = args.principal
    i = args.interest / 1200
    num_of_payments = args.periods
    total_payment = 0
    for m in range(1, num_of_payments + 1):
        d = math.ceil(loan_principal / num_of_payments + i *
                      (loan_principal - (loan_principal * (m - 1)) / num_of_payments))
        print(f"Month {m}: payment is {d}")
        total_payment += d
    overpayment = math.trunc(total_payment - loan_principal)
    print(f"\nOverpayment = {overpayment}")


def period_to_repay(args):
    loan_principal = args.principal
    monthly_pay = args.payment
    interest = args.interest
    i = interest / 1200
    period = math.ceil(math.log(monthly_pay / (monthly_pay - i * loan_principal), 1 + i))
    years = math.floor(period / 12)
    months = period % 12
    desc_years = 'year' if years == 1 else 'years'
    desc_months = 'month' if months == 1 else 'months'
    overpayment = math.trunc(monthly_pay * period - loan_principal)
    if years > 0 and months > 0:
        print(f"It will take {years} {desc_years} and {months} {desc_months} to repay this loan!")
    elif years == 0 and months > 0:
        print(f"It will take {months} {desc_months} to repay this loan!")
    elif years > 0 and months == 0:
        print(f"It will take {years} {desc_years} to repay this loan!")
    else:
        print("What? Periods = 0?")
    print(f"Overpayment = {overpayment}")


def monthly_payment(args):
    loan_principal = args.principal
    periods = args.periods
    interests = args.interest
    i = interests / 1200
    annuity_payment = math.ceil(loan_principal * ((i * pow(1 + i, periods)) / (pow(1 + i, periods) - 1)))
    overpayment = math.trunc(annuity_payment * periods - loan_principal)
    print(f"Your monthly payment = {annuity_payment}!")
    print(f"Overpayment = {overpayment}")


def total_principal(args):
    annuity_payment = args.payment
    periods = args.periods
    interests = args.interest
    i = interests / 1200
    loan_principal = math.trunc(annuity_payment / ((i * pow(1 + i, periods)) / (pow(1 + i, periods) - 1)))
    overpayment = math.trunc(annuity_payment * periods - loan_principal)
    print(f"Your loan principal = {loan_principal}!")
    print(f"Overpayment = {overpayment}")


def output_value(mode, args):
    if mode == 'diff':
        diff_payment(args)
    if mode == 'p_t_p':
        period_to_repay(args)
    elif mode == 'm_pay':
        monthly_payment(args)
    elif mode == 'total_p':
        total_principal(args)
    else:
        print("Incorrect parameters")


def main():
    parser = argparse.ArgumentParser(description="This program Loan Calculator")
    parser.add_argument("-t", "--type")
    parser.add_argument("-pay", "--payment", type=float)
    parser.add_argument("-pr", "--principal", type=float)
    parser.add_argument("-per", "--periods", type=int)
    parser.add_argument("-int", "--interest", type=float)
    args = parser.parse_args(sys.argv[1:])

    mode = what_to_calculate(args)
    output_value(mode, args)


main()
