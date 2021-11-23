result = 5*7
print(result)
power_result = 5**2  # 2(**)means power of
print(power_result)
zero = [0]*10
print(zero)
sy = "ab"*10  # repetition(tuples,strings,list)
print(sy)


def tuple_arg_dict_kwargs(a, b, *args, **kwargs):
    for i in args:
        print(i)
    for key in kwargs:
        print(key, kwargs[key])


tuple_arg_dict_kwargs(1, 2, 44, 55, 66, 88, 89, abs=30, forearm=90)


def last_Must_key_argument(x, y, *, z):
    print(x, y, z)


last_Must_key_argument(11, 22, z=[900, 66, 44])
# list unpacking


def packed_list(a, b, c, d):
    print(a, b, c, c, d)


unpacking = [1, 2, 3, 4]


packed_list(*unpacking)


def Unpacked_dict_function(a, b, c):
    print(a, b, c)


packed_dict = {'a': 22, 'b': 67, 'c': 90}
Unpacked_dict_function(**packed_dict)
#versal (packing)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
*first, last = numbers
print(first)
print(last)  # always pack into list
#merging
my_tuple =(1,2,3,4)
my_list = [1,2,3,4]
new_list =[*my_tuple,*my_list]
print(new_list)


class Test:
	def __init__(self, a, b):
		self.a = a
		self.b = b

	def __repr__(self):
		return " a:%s b:%s" % (self.a, self.b)

	def __str__(self):
		return " a is %s," \
			"b is %s" % (self.a, self.b)

# Driver Code	
t = Test(1234, 5678)
print(t) # This calls __str__()
print([t]) # This calls __repr__()
