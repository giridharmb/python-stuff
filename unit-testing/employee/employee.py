class Employee:
    """An Employee Class"""
    
    rasie_amount = 2
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        
    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first,self.last)
    
    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        new_pay = int(self.pay * self.rasie_amount)
        self.pay = new_pay