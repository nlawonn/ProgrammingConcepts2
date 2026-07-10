class Bank_Acct:
    #Initializes state names and data types
    def __init__(self, name, acct_num, amount, int_rate):
        self.name = name
        self.acct_num = acct_num
        self.amount = float(amount)
        self.int_rate = float(int_rate)

    #Allows for the adjustment of the interest rate
    def adj_int(self, new_rate):
        self.int_rate = float(new_rate)
        pass

    #Deposits funds to the account, positive numbers only
    def deposit(self, amount):
        amt = float(amount)
        if amt <=0:
            raise ValueError("Deposit amount must be positive.")
        self.amount += amt
        pass

    #Withdraws funds from the account. Displays an error if
    #withdrawl exceeds balance
    def withdraw(self, amount):
        amt = float(amount)
        if amt <= 0:
            raise ValueError("Withdrawl amount must be positive.")
        if amt > self.amount:
            raise ValueError("Withdrawl amount exceeds available balance.")
        self.amount -= amt
        pass

    #Shows account balance after transaction
    def show_balance(self):
        return self.amount

    #Calculates interest earned
    def calc_interest(self, days):
        d = float(days)
        if d < 0:
            raise ValueError("Days cannot be negative.")
        return self.amount * self.int_rate * (d / 365)
        pass

    #Displays final information
    def __str__(self):
        interest_365 = self.calc_interest(365)
        return (
            f"Account #{self.acct_num}\n"
            f"Name: {self.name}\n"
            f"Balance ${self.amount:.2f}\n"
            f"Interest (365 days): ${interest_365:.2f}\n"
            f"Interest rate: {self.int_rate * 100:.2f}%"
        )

#Sample bank account transactions with set amounts
def test_bank_acct():
    acct = Bank_Acct("Telemachus", 1776, 2000, 0.25)

    print("=== Initial ===")
    print(acct)

    print("\n=== Adjust Interest ===")
    acct.adj_int(0.10)
    print(acct)

    print("\n=== Deposit $500 ===")
    acct.deposit(500)
    print(acct)

    print("\n=== Withdraw $300 ===")
    acct.withdraw(300)
    print(acct)

    print("\n=== Overdraft Error ===")
    try:
        acct.withdraw(9999)
    except ValueError as e:
        print("Withdrawl error:", e)

    print("\n=== Interest for 30 days ===")
    print("Interest (30 days):", f"${acct.calc_interest(30):.2f}")

test_bank_acct()