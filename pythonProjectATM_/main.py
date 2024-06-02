"""
The customer must pass authentication before withdrawing money.
Authentication is performed by checking a PIN.
The PIN can be correct or not.
Unsuccessful attempts are counted.
If the counter exceeds a limit, then the customer is rejected.
If the account balance is zero, then the account is closed.
"""
import correct
from tensorflow.python.data.experimental.ops import counter
from tensorflow.python.ops.init_ops_v2 import zero

opening_balance = 2000
current_pin = 1234
def display_balance():
    print('Your balance is ${}'.format(opening_balance))

def pass_authentication():
    print('Type your authentication: ')
def check_PIN():
    print('Type your pin number: ')
def check_correct_pin(pin=None):
    if not current_pin == current_pin:
        print("Invalid pin. please try again")
def Unsuccessful_attempts(attempts=None):
    if attempts > 3:
        print('customer is rejected')

def counter_exceeds_limit(exceeds=None):
    if counter > exceeds:
        print('customer is rejected')

def account_balance_zero(balance=None):
    if balance == zero:
        print('the account is closed')
def cash_withdrew(withdrawal_amount):
    global opening_balance
    print('Your balance is ${}'.format(opening_balance))
    opening_balance = opening_balance - withdrawal_amount
    print('Your update balance is ${}'.format(opening_balance))
choice = None
amount = None


def cash_withdraw():
    pass


def check_pin():
    pass


while True:
    print("""Welcome
    1. Check balance
    2. authentication
    3. checking PIN
    4. check the correct pin
    5. Unsuccessful attempts
    6. the counter exceeds a limit
    7. the account balance is zero""")
    choice = int(input("Please Enter Choice: "))
    if choice == 1:
        display_balance()
    elif choice == 2:
        amount = int(input("Please check your authentication: "))
        cash_withdraw()
    elif choice == 3:
        pin = int(input("Enter to check pin: "))
        check_pin()
    elif choice == 4:
        check_attempts = int(input("please check the correct pin: "))
    elif choice == 5:
         Unsuccessful_attempts= int(input("Please check Unsuccessful attempts: "))
    elif choice == 6:
        counter_exceeds_limit= int(input("Please check the counter exceeds a limit: "))
    elif choice == 7:
        balance_zero = int(input({"Please the account balance is zero: "}))
    else:
        print("Invalid choice")
    break







