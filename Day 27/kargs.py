def calculate(n,**kargs):
    # for key,value in kargs.items():
    #     print(key)
    #     print(value)

    n+=kargs["add"]
    n*=kargs["multiple"]
    print(n)







calculate(6,add=3,multiple=10)