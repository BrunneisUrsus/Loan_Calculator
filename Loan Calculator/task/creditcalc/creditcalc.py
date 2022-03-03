import argparse
import math

parser = argparse.ArgumentParser(description="This program is loan calculator")
parser.add_argument("-a1", "--type")
parser.add_argument("-a2", "--payment")
parser.add_argument("-a3", "--principal")
parser.add_argument("-a4", "--periods")
parser.add_argument("-a5", "--interest")
args = parser.parse_args()

user_data = [args.type, args.payment, args.principal, args.periods, args.interest]
num_user_data = [args.type, args.payment, args.principal, args.periods, args.interest]
del num_user_data[0]

year = 12
counter = 0
negative = 0
amount = 0
period = 0
principal = 0
annuity_pay = 0

for i in user_data:
    if i is None:
        counter += 1
for i in num_user_data:
    if i is not None:
        if float(i) < 0:
            negative += 1
if counter > 1 or negative > 0:
    print("Incorrect parameters")
elif args.interest is None:
    print("Incorrect parameters")
else:
    if args.type != "annuity" and args.type != "diff":
        print("Incorrect parameters")
    elif args.type == "annuity":
        if args.periods is None:
            principal = int(args.principal)
            annuity_pay = int(args.payment)
            interest = float(args.interest)
            i = interest / (year * 100)
            num_pay = math.log((annuity_pay / (annuity_pay - i * principal)), 1 + i)
            period = math.ceil(num_pay)
            a = period / year
            b = period // year
            month = period % year
            if a == b:
                if a > 1:
                    print(f"It will take {int(a)} years to repay the loan!")
                else:
                    print("It will take 1 year to repay the loan")
            elif a > 1 and month > 1:
                print(f"It will take {int(b)} years and {month} months to repay the loan!")
            elif a > 1 and month == 1:
                print(f"It will take {int(b)} years and 1 month to repay the loan!")
            else:
                if month > 1:
                    print(f"It will take {month} months to repay the loan!")
                else:
                    print(f"It will take 1 month to repay the loan!")
        elif args.payment is None:
            principal = int(args.principal)
            period = int(args.periods)
            interest = float(args.interest)
            i = interest / (year * 100)
            annuity_pay = principal * i * pow((1 + i), period) / (pow((1 + i), period) - 1)
            print(f"Your annuity payment = {math.ceil(annuity_pay)}!")
        elif args.principal is None:
            annuity_pay = float(args.payment)
            period = int(args.periods)
            interest = float(args.interest)
            i = interest / (year * 100)
            principal = (annuity_pay
                         / (i * pow((1 + i), period))
                         * (pow((1 + i), period) - 1))
            print(f"Your loan principal = {math.ceil(principal)}!")
        overpay = period * math.ceil(annuity_pay) - principal
        print(f"Overpayment = {math.ceil(overpay)}")
    elif args.type == "diff":
        if args.payment:
            print("Incorrect parameters")
        else:
            principal = int(args.principal)
            period = int(args.periods)
            interest = float(args.interest)
            i = interest / (year * 100)
            for m in range(1, period + 1):
                payment = (principal / period) + i * (principal - principal * (m - 1) / period)
                amount += math.ceil(payment)
                print(f"Month 1: payment is {math.ceil(payment)}")
            overpay = amount - principal
            print(f"Overpayment = {overpay}")
