# **kwargs - keyword arguments
# def person(**details):
#     print(details)
#
# person()
# person(name = 'Ram')
# person(name = 'Shyam', sal = 56000, dept = "IT")
# person(id = 101, age = 45, company = 'TCS')

def person(*args, **kwargs):
    print(args)
    print(kwargs)

person('John')
person(1,2,5,6,7)
person('Mac', sal=45000)
