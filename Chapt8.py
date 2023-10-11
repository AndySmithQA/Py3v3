def mydef():
    print("This will be null")
    return None


def add(x,y):
    return x + y

def make_list(val, times):
    res = str(val) * times
    return res

result = make_list(5,10)

print(result)

def print_vat(*,gross, vatpc=20, message="Summary: "):
    net = gross / (1 + (vatpc)/100)
    vat = gross - net
    print(message, "Net: {0:5.2f} Vat {1:5.2f}".format(net,vat))

print_vat(gross=0.45)

def my_func(file, dir, user='root'):
    print('file: {:}, dir: {:}, to: {:}'.format(file,dir,user))

my_func('one', 'two', 'three')
my_func('one', 'two')
my_func(file='one', dir='two', user="Admin")


def myfunc(a,b,c):
    print(a,b,c)

mytup = 23,45,67

myfunc(*mytup)


def vari(dir, *args): #*args - Always returns a tuple
    print("dir: ", dir, "files: ", args)

vari("c:/stuff", "file1.txt", "file2.txt", "file3.txt")

def print_vat(**kwargs) : #kwargs returns a dictionary
    print(kwargs)


print_vat(vatpc=20,vat=23, gross=34, message="Hi")


result = 3

def scopetest():
    """
     My function calls in the global result
    :return:  None
    """
    global result
    result = 42
    print(result)

print(result)
scopetest()
print(result) #final global

def outer():
    num = 42

    def inner():
        print(num, "in inner")

    inner()
    print(num, "in outer")

outer()
inner()


result = 3

def my_funct():
    result = 12
    def scope_test():
        nonlocal result
        if result < 45:
            result += 1
            scope_test()
    scope_test()
    print(result, "From within my_funct")

my_funct()
print(result, "From Main")

compare = lambda a,b: -1 if a < b else (+1 if a > b else 0)

x = 300
y = 300

print("a>b?",compare(x,y))

countries = []

for line in open('country.txt'):
    countries.append(line.split(','))

countries.sort(key=lambda c: int(c[1]))

for line in countries:
    print(','.join(line), end='')

help(scopetest)