#importing modules
import csv

 # Parent class 
class Item:
     # global attribute accessible to all the methods in class and outside of it...
     #even if accessed through a new object of the class will return the same value...
    pay_rate = 0.8  #payrate after 20% discount
    all = []
    def __init__(self, name: str, price: float, quantity = 0):
         # validations... used to set limits for the instance attributes(all the variables in a function)
         # keyword : 'assert' check if the value given by user is valid or not(prints error message...)
        assert price >= 0, f"Price {price} is not a valid input..."
        assert quantity >= 0, f"Quantity {quantity} is not a vallid input..."

         # Assignment to self object...
        self.__name = name 
        self.price = price 
        self.quantity = quantity

         # actions to execute...
         # for each instance it saves them in a form of list. but it is stack value not very helpful to us...
        Item.all.append(self)

     # property Decorator = Read only Attribute user cant change it 
    @property
    def name(self):
        return self.__name
    
     # if the user wants to save a new value of name attribute...
     # also you can set limits to the setiing attribute...
    @name.setter
    def name(self, value):
        if len(value) > 10:
            raise Exception("name is too long!")
        else:
            self.__name = value

    def calculate_total_price(self):
        return self.price * self.quantity
    
    def apply_discount(self):
         # this will use the instance payrate 
         # use Item .pay_rate to always keep the pay_rate same as defined above...
        self.price *= self.pay_rate 

     # class methods are made using decorator which we add just before the line '@'
     # uses the 'cls' instead of a 'self' parameter passes class reference[Item.instantiate_from_csv()]
    @classmethod
    def instantiate_from_csv(cls):
        '''
          This should also do something that has a relationship with the class,
          but usually, those are used to manipulate different structures of data 
          to instantiate objects, like we have done here with CSV. 
        '''
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        
        for item in items:
            #print(item)
            item(
                name = item.get('name'),
                price = float(item.get('price')),
                quantity = int(item.get('quantity'))
            )

     # static methods object in never sent as the first argument like the normal functions
    @staticmethod
    def is_integer(num):
         '''
           This should do something that has a relationship with the class,
           But not something that must be unique per instance.
         '''
         # we will count out that floats that are point 0
         # for e.g: 5.0 , 10.0
         if isinstance(num, float):
              # Count out the floats that are point zero
            return num.is_integer()
         elif isinstance(num, int):
             return True
         else:
             return False
    
     #magic method(similar to __str__()) to change the list that store objects as stack value to something more user friendly
     # {self.__class__.__name__} this gives back the name of the class from the instance(imp)
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"  # best practice to represent out objects...
    
    '''
     # creating a read only attribute, their values cannot be changed...
    @property
    def read_only_name(self):
        return "AAA"
    '''


'''
sample test case
item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)

 # to print all the attributes... in dictionary format
print(Item.__dict__)  # for class level... return global attributes also
print(item1.__dict__) # for instance level... doesnt return global attributes

 #to alter global attribute for one instance only...
item2.pay_rate = 0.7

 # to print from the list that has stored all the instances// Item.all in the __init__ method
for instance in Item.all:
    print(instance.name)
'''
