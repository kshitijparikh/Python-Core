class CreditClass:
    def __init__(self,customer,bank, acnt, limit):
        self._customer=customer
        self._bank=bank
        self._account=acnt
        self._limit=limit
        self._balance=0
        
    def get_customer(self):
        return self._customer
    def get_bank(self):
        return self._get_bank
    def get_account(self):
        return self._account
    def get_limit(self):
        return self._limit
    def get_balance(self):
        return self._balance
    
    def charge(self, price):
        if self._balance + price >self._limit:
            return False
        else:
            self._balance += price 
            return True        
        
    def make_payment(self,amount):
        self._balance -= amount