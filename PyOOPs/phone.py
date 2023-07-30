from item import Item

'''
******************************
* INHERITANCE
******************************
'''
# child class Phone of class Items
# class child_class_name(parent_classs_name):
class Phone(Item):
    
    def __init__(self, name: str, price: float, quantity = 0, broken_phones = 0):
    
         #call to super function to have access to all attributes/ methods of parent class...
        super().__init__(
            name, price, quantity
        ) 
         # validations... 
        '''
        from the parent class so can be accessed using the super keyword
        assert price >= 0, f"Price {price} is not a valid input..."
        assert quantity >= 0, f"Quantity {quantity} is not a vallid input..."
        '''
        assert broken_phones>= 0, f"Price {broken_phones} is not a valid input..."

         # Assignment to self object...
        '''
        attributes of parent class so can be accessed using the super keyword in __init__ function
        self.name = name 
        self.price = price 
        self.quantity = quantity
        '''
        self.broken_phones = broken_phones

         # actions to execute...
         # for each instance it saves them in a form of list. but it is stack value not very helpful to us...
         # Phone.all.append(self)
         # no need for this as the super function takes care of it...

'''
sample test cases
phone1 = Phone("jscPhonev10", 500, 5, 1)
phone2 = Phone("jscPhonev20", 700, 5, 1)
'''
