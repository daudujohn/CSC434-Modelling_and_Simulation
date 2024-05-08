from peewee import SqliteDatabase, Model, CharField, ForeignKeyField, TextField, DateTimeField, BooleanField, FloatField, DateField
import datetime

db = SqliteDatabase('loan.db', pragmas={'journal_mode': 'wal', 'cache_size': -64 * 1000,'synchronous': 0}) 

class BaseModel(Model):
    class Meta:
        database = db

class User(BaseModel):
    email = CharField(unique=True, primary_key=True)
    username = CharField(unique=True)
    password = CharField()
    balance = FloatField(null=True)

class Staff(BaseModel):
    email = CharField(unique=True, primary_key=True)
    username = CharField(unique=True)
    password = CharField()
    role = CharField(choices=[('admin', 'admin'), ('staff', 'staff'), ('manager', 'manager')])

class Loan(BaseModel):
    user = ForeignKeyField(User, backref='loans')
    amount = FloatField()
    amount_payable = FloatField()
    annual_interest_rate = FloatField()
    start_date = DateField()
    balance = FloatField()
    status = CharField(choices=[('paid', 'paid'), ('active', 'active')])
    created_date = DateTimeField(default=datetime.datetime.now)
    is_published = BooleanField(default=True)

class LoanPayment(BaseModel):
    user = ForeignKeyField(User, backref='loanpayments')
    loan = ForeignKeyField(Loan, backref='loanpayments')
    amount_paid = FloatField()
    created_date = DateTimeField(default=datetime.datetime.now)
    is_published = BooleanField(default=True)

def create_tables():
    with db.atomic():
        db.create_tables([User, Loan, LoanPayment])

create_tables()
