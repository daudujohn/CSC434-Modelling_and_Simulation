from peewee import DoesNotExist, IntegrityError
from db import Loan, db

# TODO: Function to show highest earning month

def get_expected_income():
        query = Loan.select()
        expected_income = [loan.amount_payable for loan in query]
        return expected_income


def get_total_loan():
        query = Loan.select()
        loans = [loan.amount for loan in query]
        return loans

get_expected_income()
