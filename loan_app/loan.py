# from matplotlib import pyplot as plt
from db import User, Loan, LoanPayment
from user_model import login

user = login()

def repayment_loan():
    try:
        loan = float(input("Enter your loan amount: $"))
        rate = float(input("Enter annual percentage interest percentage: "))/100
    except ValueError: 
        return 'Type a number'
    # (p * (1 + i)**n) - p
    data = []
    paymentArr = []
    month = 0
    balance = 0
    loan = loan * ((1 + (rate/12))**12)

    while loan > 0:
        month += 1
        amount_paid = float(input(f"Enter amount to be paid in month {month}: $"))
        paymentArr.append(amount_paid)
        loan -= amount_paid

        if loan < 0:
            amount_paid += loan
            data.append([month, 0, amount_paid])
            balance = -loan
            break
        else: 
            data.append([month, loan, amount_paid])

    for item in data:
        print(item, 'rate =', format(rate, '.4f'))
    print('You paid a total of', format(sum(paymentArr), '.2f'))
    print('You have a balance of', format(balance, '.2f'))
    print('Congratulations, you have paid off your loan')

    monthly_range = range(1, month + 1)
    loan_balance = [loan - sum(paymentArr[:i]) for i in monthly_range]
    # plt.plot(monthly_range, loan_balance, marker='o', linestyle='-')
    # plt.xlabel('Months')
    # plt.ylabel('Loan Balance')
    # plt.title('Loan Repayment Schedule')
    # plt.grid(True)
    # plt.show()

if user:
    a = repayment_loan()
    print(a)
