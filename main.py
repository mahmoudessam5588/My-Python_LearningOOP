from generator_class import generator_class


def main(args):
    generator_call()
    return 0


def generator_call():
    generator_class
    geni = generator_class()
    geni.first_num(10)
    print("-------")
    rs = geni.first_nums(10)
    print(list(rs))
    print("-------")
    fibi = geni.fibonacci(18)
    print(list(fibi))
    print("-------")
    geni.geni_exp()
    print("-------")
    geni.geni_compri()


if __name__ == '__main__':
    import sys
    main(sys.argv)
