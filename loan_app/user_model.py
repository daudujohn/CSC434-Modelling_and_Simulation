from peewee import DoesNotExist, IntegrityError
from db import User, Staff, db

def login():
        user = None
        try:
            tries = 3
            while tries > 0:
                username = input('Hi there, \nEnter your username: ')
                possible_user = User.get(User.username == username)
                password = input('Enter your password: ')
                if possible_user.password != password:
                    print('Incorrect username or password. Try again')
                else:
                    user = possible_user
                    break
                tries -= 1
        except DoesNotExist:
            try:
                possible_user = Staff.get(Staff.username == username)
                password = input('Enter your password: ')
                if possible_user.password == password:
                    print('Welcome Staff', possible_user.username)
                    return possible_user
            except DoesNotExist:
                pass

            email = input('Enter your email: ')
            password = input('Create your password: ')
            try:
                with db.atomic():
                    user = User.create(username=username, password=password, email=email)
            except IntegrityError:
                return 'Bad or Incomplete Input. '
        return user

def get_users():
    query = User.select()
    users = [user for user in query]
    return users

a = get_users()
print(a)