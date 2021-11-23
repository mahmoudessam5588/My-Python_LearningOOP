import copy
from typing import NamedTuple
org: int = 5
cpy: int = org  # another variable pointing to same reference no problem with immutable types
cpy: int = 6  # now cpy created new variable in the heap and pointing to it cpy and org are different
print(org, cpy)
# now with immutable types both can change
original_list: list = [1, "moon", 12.5]
copy_list: list = original_list
print(original_list, copy_list)
copy_list[0] = -10
print(original_list, copy_list)  # 2 variables changed
# to use actual copy use built in copy module
# shallow copy one level deep only reference of nested child object
# deep copy full independent copy
cpy = copy.copy(org)
print(cpy)
print(org)
# 3 methods of dealing with lists copy or list() or slicing
original_list = copy.copy(copy_list)
print(original_list, copy_list)
original_list = list(copy_list)
print(original_list, copy_list)
original_list = copy_list[:]
print(original_list, copy_list)
# shallow copy in nested list also worked with dict tuples
org_nested_list: list = [[1, 2, 3], [4, 5, 6], [6, 7, 8]]
cpy_nested_list: list = copy.copy(org_nested_list)
org_nested_list[0][1] = -10
print(org_nested_list, cpy_nested_list)
cpy_nested_list = copy.deepcopy(org_nested_list)
org_nested_list[0][1] = -20
print(org_nested_list, cpy_nested_list)
# in case of custom objects
class Person:
    def __init__(self,name:str,age:int):
        self.name = name
        self.age = age
Person
p1 = Person('alex',27)
p2=p1
print(p2.name,p2.age)
p2.age =30
p2=copy.copy(p1)
print(p2.name,p2.age)        
#but with more nested custom logic it's better to use deep copy
     
