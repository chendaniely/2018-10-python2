import pandas as pd

class Person(object):
    def __init__(self, fname, lname, dob):
        self.fname = fname
        self.lname = lname
        self.dob = dob
    def __repr__(self):
        return f"My name is {self.fname}"
    def start_job(self):
        self._money = 5
        return self
    def get_paid(self):
        self._money += 10
        return self
    def dob_dt(self):
        return pd.to_datetime(self.dob, format='%Y-%m-%d')
    
    @property
    def money(self):
        return self._money
    
    @money.setter
    def money(self, new_money_value):
        assert isinstance(new_money_value, int)
        self._money = new_money_value