""" -the difference between arguments and parameters
    -Positional and keyword arguments
    -default arguments
    -variable length arguments(*Args,**kwargs)
    -container unpacking into function arguments
    -local vs global arguments
    -parameter passing (by value or by reference)
"""
def print_name(name):
    print(name)#name is a parameter 
print_name('Alex')#alex is an argument    
#positional argument
def foo (a,b,c):
    print(a,b,c)
foo('as',12,12.56) 
# or explicit specify the argument (arrangment not needed)
foo(c=12.56,a='as',b='12')
#default argument is
def fobs(a,b,c,d=4):
    print(a,b,c,d) 
fobs('ahmed',33,28)
#variable length arguments
def fool(a,b,*args, **kwargs):
    print(a,b)
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key,kwargs[key])
#print(1,44,5,7,9,10,400,hello=6,hi=7)
def jake(a,b,c):
    print(a,b,c)
my_list = [0,1,2]
jake(*my_list)
my_dict = {'a':20,'b':30,'c':40}
jake(**my_dict)    
                  