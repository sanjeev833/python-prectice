#Topic:- Types of variable and Lmabda Functions
#Topic:- Types of variable and Lmabda Functions


#Types oF variables

'''
In python there are 2 types of variables

1.Global Variables
2.Local varibales
'''

#Global Variables
'''The variables which are declared outside of function are called global variables.
 These variables can be accessed in all functions of that module'''

'''a = 10 #global V

def f1():
    print(a)

def f2():
    print(a)

f1()
f2()'''

#Local Variables
'''The Varibales which are declared inside a function are called local variables.
Local variables are available only for the functions in which we declared it that is from outside 
of function we cannot access.'''

'''def f1():
    a = 10
    print(a)

def f2():
    print(a)

f1()
f2()'''

#global keyword

'''a = 10

def f1():
    a = 108
    print('f1',a)

def f2():
    print('f2',a)

f1()
f2()'''

'''a = 10


def f1():
    global a
    a = 108
    print('f1',a)

def f2():
    print('f2',a)

f1()
f2()

a = 89
a = 87'''



# Anonymous Functions\lambda Func

'''Sometimes we can declare a function without any name, such type of nameless functions
are called anonymous functions or lambda function'''


#Normal Funs

'''def squre(n):
    return n*n

print(squre(10))'''

#lamnda function
# we can define by using lambda
#syntax

'''variable = lambda parameter_list:statemsnts'''

'''squre = lambda n:n*n
print(squre(10))'''

#Lambda function find sum of 2 given number

'''add = lambda a,b : a+b

print(add(10,20))'''

'''Adv
By using lambda functions we can write very concise code so that readability of 
the program will be improved'''

#lambda function to find biggest of given numbers
'''grt = lambda a,b:a if a>b else b

print(grt(78,67))'''



'''
Notes

1. Lambda functions internally return expression values and we are not required to write
return statements explicity.

2.Sometimes we can pass function as a argument to another functions.
 Insuch cases lambda function are best choice.
 
 we can use lambda function very commonly with filter().map(),reduce
'''
