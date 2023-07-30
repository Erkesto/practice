'''
 this file is not supposed to be run but is instead for learning the best practices for
 OOPs in python 
 what is the main difference between class methods and static methods?
  the static methods are not passing the madator object reference as the first
  argument in the background.
OOPs four key principles:
Encapsulation : restricting direct access to the some of the attributes...
Abstraction : hiding unnecessary details of a functions working 
Inheritence :allows us to reuse codes accross our classes to reduce redundency
Polymorphism :use of a single type entity to represent different type in different situations

to make a attribute read only you chaneg it from price -> __price...
and add a @property decorator {def price(self): return self.__price}
''' 
'''
******************************
* Getters and Setters
******************************
'''

from item import Item 

item1 = Item("MyItem", 750)
item1.name = "OtherItem"

print(item1.name)
