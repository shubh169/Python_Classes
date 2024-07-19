""" *args: many positional arguments."""
# def add(*args):
#     sum = 0
#     for n in args:
#         sum += n
#     print(sum)
#     print(type(args))
#
#
# add(1, 2, 3, 4, 5, 6)


""" **kargs: many keyword arguments."""

def calculate(n,**kargs):
    print(type(kargs))
    # for key,value in kargs.items():
    #     print(key,value)
    n+=kargs['add']
    n*=kargs['multiply']
    print(n)


calculate(10,add=10,multiply=5)