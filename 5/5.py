from functools import wraps
import time
def time_dec(func):
    @wraps(func)
    def wrapper(*arg,**kwarg):
        time1 = time.time()
        func(*arg,**kwarg)
        time2 = time.time()
        print("The time is:%10f"%(time2-time1))
        return func
    return wrapper
    
@time_dec
def numbers(a,b):
    print("a+b=",a+b)
numbers(10,5)

@time_dec
def read_and_write():
    with open('input.txt','r') as file:
        a,b=map(int,file.read().split())
        result=a+b
    with open('output.txt','w') as file:
        file.write(f"a+b={result}")
read_and_write()


