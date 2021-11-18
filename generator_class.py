class generator_class:
    """function that return an object that can be iterated they generate it lazly same syntax as normal function but with yeild key word instead of return"""
    def my_generator():
        yield 1
        yield 2
        yield 3
    g = my_generator()
    for i in g:
        print (i)
    # value = next(g)
    # print (value)            
    #different syntax and lazy loading between normal ,ethod and generators
    def first_num(self,n):
        nums = []
        num = 0
        while num < n:
            nums.append(num)
            num +=1
            return nums
    def first_nums(self,n1):
        num=0
        while num < n1:
            yield num
            num +=1
        return num
    def  fibonacci(self,limit):
        a,b = 0,1
        while a < limit:
            yield a
            a,b=b,a+b
    #generator expression shorter syntax
    def geni_exp(self):
        generator_exp = (i for i in range(10) if i%2==0)
        print(list(generator_exp))
    #list comprehension
    def geni_compri(self):
        compri_list = [i for i in range(10) if i%2==0]
        print(compri_list)                        