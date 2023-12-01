#x is a local variable
#life of x is limited to the function
#scope of x is in the body of function f1() only.
'''def f1():
    x=10
    print(x)
f1()'''
#Global variable
# variables declared outside function and are global variables.
#life of global variable is till the end of program.
'''x=20
def f1():
    print(x)
f1()
print(x)'''
x=20
def f1():
    global x
    x=10 #local Variable
    print(x) #Local variable of x
    d=globals()
    d['x']=30 #To change the value of global variable
    print(d['x'])
f1()
print(x) #global variable of x
print()